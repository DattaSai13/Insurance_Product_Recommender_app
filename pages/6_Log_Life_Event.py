import streamlit as st
from utils.file_manager import load_customers, update_customer
from utils.file_manager import load_products
from utils.recommendation import hybrid_recommendation




st.title("📅 Log Major Life Event & Update Recommendations")

customers_df = load_customers()
products_df = load_products()

if customers_df.empty:
    st.info("No customers found. Please add a customer first.")
    st.stop()

customer_id = st.selectbox("Select Customer ID to Log Event", customers_df['customer_id'])
customer = customers_df[customers_df['customer_id'] == customer_id].iloc[0].to_dict()

st.write(f"Current Life Event: {customer.get('life_events', 'None')}")

event_options = ["None", "Marriage", "Child Birth", "Job Change", "Property Purchase"]
new_event = st.selectbox("Select Life Event to Log", event_options)

if st.button("Log Event"):
    # Update customer life event
    customer['life_events'] = new_event
    update_customer(customer_id, customer)
    st.success(f"Life event '{new_event}' logged for Customer ID {customer_id}.")

    # Recompute recommendations
    recommended_df = hybrid_recommendation(customer, customers_df, products_df)

    st.subheader(f"Updated Recommendations for Customer {customer_id}")
    for _, row in recommended_df.head(5).iterrows():
        st.markdown(f"### {row['product_name']}")
        st.markdown(f"- Confidence: **{row.get('confidence', 'N/A')}%**")
        st.markdown(f"- Why: {row.get('explanation', 'No explanation')}")
        st.markdown(f"- Premium: {row['premium_range']}")
        st.markdown(f"- Coverage: {row['coverage_type']}")
        st.markdown("---")
