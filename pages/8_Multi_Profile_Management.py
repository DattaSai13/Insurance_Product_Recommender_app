import streamlit as st
from utils.file_manager import load_customers, load_products
from utils.recommendation import hybrid_recommendation




st.title("👨‍👩‍👧‍👦 Multi-profile (Family) Management & Bundled Recommendations")

customers_df = load_customers()
products_df = load_products()

if customers_df.empty:
    st.info("No customer profiles found. Please add members first.")
    st.stop()

# Show all profiles, optional relation column (add to your customer records)
st.subheader("Current Family Member Profiles")
st.dataframe(customers_df)

selected_members = st.multiselect("Select Members for Bundle Recommendation", customers_df['customer_id'])

if selected_members:
    st.subheader("Recommended Packages for Selected Members")
    for cid in selected_members:
        member = customers_df[customers_df['customer_id'] == cid].iloc[0].to_dict()
        recs = hybrid_recommendation(member, customers_df, products_df)
        st.markdown(f"#### Recommendations for {member.get('name', f'ID {cid}')}")
        for _, row in recs.head(2).iterrows():
            st.markdown(f"- **{row['product_name']}** | Confidence: {row.get('confidence', 'N/A')}%")
            st.markdown(f"  - Coverage: {row['coverage_type']}")
            st.markdown(f"  - Premium: {row['premium_range']}")
            st.markdown(f"  - Description: {row['description']}")
        st.markdown("---")
    st.info("Combine top suggestions across all members for a family insurance bundle.")

# To allow adding members, include a name & relation in your Add New Customer page.
