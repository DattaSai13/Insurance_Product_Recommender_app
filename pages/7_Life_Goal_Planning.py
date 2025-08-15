# pages/6_Life_Goal_Planning.py



import streamlit as st
from utils.file_manager import load_customers, update_customer, load_products
from utils.recommendation import hybrid_recommendation
import json

st.title("🎯 Life Goal Planning")

customers_df = load_customers()
products_df = load_products()

if customers_df.empty:
    st.info("No customers found. Please add a customer first.")
    st.stop()

customer_id = st.selectbox("Select Customer ID for Goal Planning", customers_df['customer_id'])
customer = customers_df[customers_df['customer_id'] == customer_id].iloc[0].to_dict()

with st.form("goal_form"):
    retirement_age = st.number_input("Desired Retirement Age", min_value=40, max_value=80, value=60)
    child_education_goal = st.checkbox("Saving for Child's Higher Education?")
    house_goal = st.checkbox("Planning to buy a house?")
    travel_goal = st.checkbox("International Travel Plans?")
    others = st.text_input("Other financial goals")
    submitted = st.form_submit_button("Save Goals & Get Tailored Recommendations")

if submitted:
    goals = {
        "retirement_age": retirement_age,
        "child_education": child_education_goal,
        "house": house_goal,
        "travel": travel_goal,
        "other_goals": others
    }
    customer['financial_goals'] = json.dumps(goals)
    update_customer(customer_id, customer)
    st.success("Goals saved! Tailoring recommendations now...")
    recommended_df = hybrid_recommendation(customer, customers_df, products_df)
    for _, row in recommended_df.head(5).iterrows():
        st.markdown(f"### {row['product_name']}")
        st.markdown(f"- Confidence: **{row.get('confidence', 'N/A')}**")
        st.markdown(f"- Explanation: {row.get('explanation', 'No explanation')}")
        st.markdown(f"- Premium: {row['premium_range']}")
        st.markdown(f"- Coverage: {row['coverage_type']}")
        st.markdown(f"- Description: {row['description']}")
        st.markdown("---")
