import streamlit as st
from utils.file_manager import load_customers, load_products
from utils.recommendation import hybrid_recommendation
import copy




st.title("🔮 What If Analysis: Adjust Your Profile")

customers_df = load_customers()
products_df = load_products()

if customers_df.empty:
    st.info("No customers found. Please add a customer first.")
    st.stop()

# Select the customer to simulate
customer_id = st.selectbox("Select Customer ID for What If Analysis", customers_df['customer_id'])
original_customer = customers_df[customers_df['customer_id'] == customer_id].iloc[0].to_dict()

st.subheader("Base Profile")
st.write({
    "Age": original_customer['age'],
    "Health Score": original_customer['health_score'],
    "Risk Score": original_customer['risk_score'],
})

st.sidebar.header("Modify Profile Parameters")

# Create a copy for modifying
modified_customer = copy.deepcopy(original_customer)

# Interactive sliders/inputs for key parameters
modified_customer['age'] = st.sidebar.slider("Age", 18, 100, value=int(original_customer['age']))
modified_customer['health_score'] = st.sidebar.slider("Health Score (0=Poor, 1=Excellent)", 0.0, 1.0,
                                                     value=float(original_customer['health_score']), step=0.01)
modified_customer['risk_score'] = st.sidebar.slider("Risk Score (0=Low, 1=High)", 0.0, 1.0,
                                                   value=float(original_customer['risk_score']), step=0.01)

st.write("### Adjusted Profile")
st.write({
    "Age": modified_customer['age'],
    "Health Score": modified_customer['health_score'],
    "Risk Score": modified_customer['risk_score'],
})

# Compute recommendations for adjusted profile
recommended_df = hybrid_recommendation(modified_customer, customers_df, products_df)

st.subheader("Updated Insurance Recommendations")

if recommended_df.empty:
    st.info("No recommendations available for this adjusted profile.")
else:
    for _, row in recommended_df.head(5).iterrows():
        st.markdown(f"### {row['product_name']}")
        st.markdown(f"- Confidence: **{row.get('confidence', 'N/A')}**")
        st.markdown(f"- Explanation: {row.get('explanation', 'N/A')}")
        st.markdown(f"- Premium: {row['premium_range']}")
        st.markdown(f"- Coverage: {row['coverage_type']}")
        st.markdown(f"- Description: {row['description']}")
        st.markdown("---")
