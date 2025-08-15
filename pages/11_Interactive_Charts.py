import streamlit as st
import pandas as pd
from utils.file_manager import load_customers, load_products
from utils.recommendation import hybrid_recommendation
import re




st.title("📊 Personalized Insurance Plan Charts")

customers_df = load_customers()
products_df = load_products()
if customers_df.empty or products_df.empty:
    st.info("Customer or product data missing.")
    st.stop()

customer_id = st.selectbox("Select Customer", customers_df['customer_id'])
customer = customers_df[customers_df['customer_id'] == customer_id].iloc[0].to_dict()

# Get recommended products for this customer
recommended_df = hybrid_recommendation(customer, customers_df, products_df)
if recommended_df.empty:
    st.info("No recommended plans for this customer.")
    st.stop()

def extract_premium(x):
    nums = re.findall(r"\d+\.?\d*", str(x).replace(',', ''))
    return float(nums[0]) if nums else 0.0

premium_col = recommended_df['premium_range'].apply(extract_premium)
sum_assured_col = recommended_df.get('sum_assured', pd.Series([0]*len(recommended_df)))

chart_df = pd.DataFrame({
    'Product': recommended_df['product_name'],
    'Premium': premium_col,
    'SumAssured': sum_assured_col,
    'Coverage': recommended_df['coverage_type'],
    'Confidence': recommended_df.get('confidence', pd.Series(['N/A']*len(recommended_df))),
})

st.subheader(f"Premium vs Sum Assured for {customer.get('name', customer_id)}")
st.bar_chart(chart_df.set_index("Product")[["Premium", "SumAssured"]])

st.subheader("Coverage Type Distribution")
cover_types = chart_df['Coverage'].value_counts()
st.write(cover_types)
st.bar_chart(cover_types)

st.subheader("Recommendation Confidence")
chart_df_tmp = chart_df.copy()
chart_df_tmp['Confidence%'] = chart_df_tmp['Confidence'].apply(
    lambda x: float(str(x).replace('%','')) if str(x) != 'N/A' and str(x).replace('%','').replace('.','',1).isdigit() else 0)
st.bar_chart(chart_df_tmp.set_index("Product")[["Confidence%"]])
