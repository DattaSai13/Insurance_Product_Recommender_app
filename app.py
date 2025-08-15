import streamlit as st
import pandas as pd

st.set_page_config(page_title="Insurance Recommender 🎉", layout="wide")

# Project Introduction
st.markdown("# 🛡️ Insurance Product Recommender Engine")
st.markdown("""
Welcome to the intelligent Insurance Recommender system! This app helps you discover the most suitable insurance products based on your life stage, unique needs, and real-time data.

---
""")

with st.expander("ℹ️ About the Project"):
    st.write("""
    **The Insurance Recommender app leverages state-of-the-art analytics and your personal data to suggest insurance plans truly right for you. 
    Whether you're starting your career, growing your family, or planning retirement—this tool adapts as your needs evolve.**
    """)

# Workflow Section with Emojis and Clear Steps
st.markdown("## 🚦 How It Works")
st.markdown("""
1️⃣ **Customer Data** ➡️  
2️⃣ **Life Stage Analysis** 🚸 ➡️  
3️⃣ **Needs Assessment** 🎯 ➡️  
4️⃣ **Product Matching** 🧩 ➡️  
5️⃣ **Ranked Recommendations** ⭐

- **Customer Data:** Demographics, goals, life events  
- **Life Stage Analysis:** Determines your current situation  
- **Needs Assessment:** Calculates financial and protection needs  
- **Product Matching:** Finds the best-fit insurance solutions  
- **Ranked Recommendations:** Shows you the top matches with transparent explanations
""")

with st.expander("✨ Example Workflow"):
    st.markdown("""
    - Anna (30, newly married, thinking about a baby) logs her life event.
    - The app recalculates insurance needs for family, health, and child's education.
    - Anna receives clear recommendations with confidence scores and reasons.
    """)

# Show top 10 insurance plans with table and chart (robust for missing columns)
products_df = pd.read_csv("data/products.csv")
top_10 = products_df.head(10)

preferred_cols = ['product_name', 'product_type', 'premium_range', 'coverage_type', 'sum_assured']
cols_to_show = [col for col in preferred_cols if col in top_10.columns]

st.markdown("## 🏆 Top 10 Insurance Products")
st.dataframe(top_10[cols_to_show])



# Customer Benefits Section
st.markdown("## 🎁 Customer Benefits")
benefits = [
    "Instant, data-driven, personalized recommendations",
    "Confidence score for each product",
    "Adjustment and 'What If' analysis for future planning",
    "Protection for every life stage (young, married, retirement, etc.)",
    "Clear explanations—know *why* a product is suggested",
    "Easy, beautiful dashboard with charts and downloads"
]
for b in benefits:
    st.markdown(f"- ✅ {b}")

st.markdown("## 📝 More About The App")
with st.expander("🔍 Major Features"):
    st.write("""
    - Life Events Logging: adapts with major life changes (marriage, birth, job change).
    - Goal-Oriented Planning: updates with retirement and savings goals.
    - Multi-User Access: Admins can see all data; users see their own.
    - Interactive Visuals: coverage distribution, premium vs benefit charts.
    - Easy Export: download your recommendations.
    """)

with st.expander("🧬 Tech Behind The Scenes"):
    st.write("""
    - Python, Pandas, Streamlit
    - Modular recommendation pipeline
    - Rule-based and hybrid scoring
    - Role-based data access
    - Modular and extensible codebase
    """)

st.markdown("---")
st.markdown("### 📥 Download Sample Product List")
if not top_10.empty:
    st.download_button(
        label="Download Sample Products CSV",
        data=top_10[cols_to_show].to_csv(index=False),
        file_name="sample_products.csv",
        mime="text/csv"
    )
