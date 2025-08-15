import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Product Management", layout="wide")
st.title("🛠️ Manage Insurance Products")

PRODUCTS_CSV = "data/products.csv"

def load_products():
    # Always read fresh to avoid cache update issues
    if not os.path.exists(PRODUCTS_CSV):
        df = pd.DataFrame(columns=[
            "product_id", "product_name", "product_type",
            "premium_range", "coverage_type", "sum_assured", "description"
        ])
        df.to_csv(PRODUCTS_CSV, index=False)
    return pd.read_csv(PRODUCTS_CSV)

def save_products(df):
    df.to_csv(PRODUCTS_CSV, index=False)

products_df = load_products()

st.sidebar.header("Select Action")
action = st.sidebar.radio("Choose:", ["View Products", "Add Product", "Modify Product", "Delete Product"])

st.sidebar.write("---")
st.sidebar.write(f"Current number of products: {len(products_df)}")

if action == "View Products":
    st.subheader("All Products")
    st.dataframe(products_df)

elif action == "Add Product":
    st.subheader("Add a New Product")
    with st.form("add_form"):
        product_id = st.text_input("Product ID (must be unique)")
        product_name = st.text_input("Product Name")
        product_type = st.text_input("Product Type")
        premium_range = st.text_input("Premium Range")
        coverage_type = st.text_input("Coverage Type")
        sum_assured = st.text_input("Sum Assured")
        description = st.text_area("Description")
        submitted = st.form_submit_button("Add Product")
        if submitted:
            if product_id in products_df['product_id'].astype(str).values:
                st.error("Product ID already exists.")
            else:
                new_product = {
                    "product_id": product_id,
                    "product_name": product_name,
                    "product_type": product_type,
                    "premium_range": premium_range,
                    "coverage_type": coverage_type,
                    "sum_assured": sum_assured,
                    "description": description
                }
                products_df = pd.concat([products_df, pd.DataFrame([new_product])], ignore_index=True)
                save_products(products_df)
                st.success(f"Product '{product_name}' added.")
                st.rerun()

elif action == "Modify Product":
    st.subheader("Modify Existing Product")
    # Always re-load for up-to-date UI
    products_df = load_products()
    product_ids = products_df['product_id'].astype(str).tolist()
    selected_id = st.selectbox("Select Product ID to Modify", product_ids)
    if selected_id:
        product_rows = products_df[products_df['product_id'].astype(str) == selected_id]
        if not product_rows.empty:
            p = product_rows.iloc[0]
            with st.form("modify_form"):
                product_name = st.text_input("Product Name", p['product_name'])
                product_type = st.text_input("Product Type", p['product_type'])
                premium_range = st.text_input("Premium Range", p['premium_range'])
                coverage_type = st.text_input("Coverage Type", p['coverage_type'])
                sum_assured = st.text_input("Sum Assured", str(p.get('sum_assured', '')))
                description = st.text_area("Description", str(p.get('description', '')))
                submitted = st.form_submit_button("Update Product")
                if submitted:
                    # Update the correct row
                    idx = product_rows.index[0]
                    products_df.at[idx, 'product_name'] = product_name
                    products_df.at[idx, 'product_type'] = product_type
                    products_df.at[idx, 'premium_range'] = premium_range
                    products_df.at[idx, 'coverage_type'] = coverage_type
                    products_df.at[idx, 'sum_assured'] = sum_assured
                    products_df.at[idx, 'description'] = description
                    save_products(products_df)
                    st.success(f"Product '{product_name}' updated.")
                    st.rerun()
        else:
            st.error("Selected product not found in data.")

elif action == "Delete Product":
    st.subheader("Delete a Product")
    # Always re-load for up-to-date UI
    products_df = load_products()
    product_ids = products_df['product_id'].astype(str).tolist()
    selected_id = st.selectbox("Select Product ID to Delete", product_ids)
    if selected_id:
        product_rows = products_df[products_df['product_id'].astype(str) == selected_id]
        if not product_rows.empty:
            p = product_rows.iloc[0]
            st.write(f"Selected: **{p['product_name']}** (ID: {p['product_id']})")
            if st.button("Delete"):
                products_df = products_df[products_df['product_id'].astype(str) != selected_id]
                save_products(products_df)
                st.success(f"Product '{p['product_name']}' deleted.")
                st.rerun()
        else:
            st.error("Selected product not found in data.")
