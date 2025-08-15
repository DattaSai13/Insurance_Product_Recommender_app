import streamlit as st
import pandas as pd
from utils.file_manager import load_customers, load_products
from utils.recommendation import hybrid_recommendation




st.header("🏆 Top 3 Insurance Product Comparison")

# Load customer and product data
customers_df = load_customers()
products_df = load_products()

# Select a customer for recommendation
if customers_df.empty:
    st.info("No customers found. Please add a customer first.")
    st.stop()

customer_id = st.selectbox("Select Customer ID for Comparison", customers_df['customer_id'])
customer = customers_df[customers_df['customer_id'] == customer_id].iloc[0].to_dict()

# Get recommendations
recommended_df = hybrid_recommendation(customer, customers_df, products_df)
top3_df = recommended_df.head(3)

st.subheader("🆚 Product Comparison Table (Top 3 Recommendations)")

if not top3_df.empty:
    # Exclusions: use '' if not present in your products data
    columns = ["product_name", "premium_range", "coverage_type", "description"]
    if "exclusions" in top3_df.columns:
        columns.append("exclusions")
    else:
        top3_df["exclusions"] = ""

    table_md = "| Policy Name | Premium | Coverage | Key Benefits | Exclusions |\n"
    table_md += "|-------------|---------|----------|--------------|------------|\n"
    for _, row in top3_df.iterrows():
        table_md += f"| {row['product_name']} | {row['premium_range']} | {row['coverage_type']} | {row['description']} | {row['exclusions']} |\n"
    st.markdown(table_md)
else:
    st.info("No products to compare for this customer.")

st.markdown("---")
st.write("Choose a customer above to view top 3 recommended policies side-by-side. The table helps you compare premiums, coverage, benefits, and exclusions quickly.")
