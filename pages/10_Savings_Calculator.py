import streamlit as st
from utils.file_manager import load_products




st.title("💰 Savings Calculator")

products_df = load_products()
if products_df.empty:
    st.info("No products found.")
    st.stop()

product_id = st.selectbox("Select Insurance Policy", products_df['product_id'])
product = products_df[products_df['product_id'] == product_id].iloc[0].to_dict()
st.markdown(f"**Product:** {product['product_name']}")
premium = st.number_input("Annual Premium (₹)", min_value=0, value=10000)
years = st.number_input("Investment Duration (years)", min_value=1, value=10)
expected_rate = st.slider("Expected Return (%)", 2.0, 12.0, value=6.0, step=0.1)

# Calculate simple future value (doesn't include tax saving, etc.):
future_value = premium * ((1 + expected_rate / 100) ** years)

st.info(f"Projected savings after {years} years: **₹{future_value:,.2f}**")
st.markdown("""*This is a simplified estimate. Actual maturity values may vary by policy.*""")
