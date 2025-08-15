import streamlit as st
from utils.file_manager import load_customers, load_products
from utils.recommendation import hybrid_recommendation




st.title("🛡️ Insurance Product Recommendations")

customers_df = load_customers()
products_df = load_products()

if customers_df.empty:
    st.info("No customers found. Please add a customer first.")
    st.stop()

customer_id = st.selectbox("Select Customer ID for Recommendations", customers_df['customer_id'])
customer = customers_df[customers_df['customer_id'] == customer_id].iloc[0].to_dict()

recommended_df = hybrid_recommendation(customer, customers_df, products_df)

st.subheader(f"Top Recommendations for Customer {customer_id}:")

if recommended_df.empty:
    st.info("No recommendations available for this customer.")
else:
    for _, row in recommended_df.head(5).iterrows():
        st.markdown(f"### {row['product_name']}")
        confidence = row.get('confidence', None)
        if confidence is not None:
            st.markdown(f"**Confidence:** {confidence}")
        explanation = row.get('explanation', '')
        if explanation:
            st.markdown(f"**Explanation:** {explanation}")
        st.markdown(f"- Premium: {row['premium_range']}")
        st.markdown(f"- Coverage: {row['coverage_type']}")
        st.markdown(f"- Description: {row['description']}")
        st.markdown("---")
