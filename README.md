# Insurance Recommender App

An interactive Streamlit application providing personalized insurance product recommendations, life-stage analysis, and comprehensive customer and product management.

---

## Features

- **Customer Profile Management:** Add, view, update, delete customer profiles capturing detailed demographic, financial, and risk information.
- **Insurance Product Management:** Add, edit, delete, and compare insurance products.
- **Personalized Recommendations:** Hybrid recommendation engine offering tailored insurance plans based on customer data and life events.
- **Life Stage & Financial Goal Planning:** Analyze and plan life and financial goals with interactive tools and simulations.
- **Rich Interactive UI:** Dynamic dashboards with search, charts, forms, and downloadable reports.
- **Risk Tolerance Questionnaire:** Integrated quiz to quantify customer risk profiles for better recommendations.

---

## Project Structure

.
├── app.py # Main application entry and homepage
├── data/ # CSV data storage for customers and products
├── models/ # Placeholder for ML or other models
├── pages/ # Streamlit multipage directory with all feature pages
│ ├── 0_Product_Management.py # Product CRUD and management
│ ├── 1_Customer_Management.py # Customer CRUD and management
│ ├── 2_Recommendations.py # Insurance product recommendations
│ ├── 5_Product_Comp.py # Product comparison visualizations
│ ├── 6_Log_Life_Event.py # Customer life event logging
│ ├── 7_Life_Goal_Planning.py # Life and financial goal management
│ ├── 8_Multi_Profile_Management.py # Management of multiple customer profiles
│ ├── 9_What_If_Analysis.py # What-if scenario analysis tool
│ ├── 10_Savings_Calculator.py # Savings and benefit calculation
│ └── 11_Interactive_Charts.py # Interactive charts and analytics
├── utils/ # Helper functions and utilities
│ ├── file_manager.py # Data loading/saving utilities
│ ├── life_stage.py # Life stage analysis logic
│ ├── logger.py # Application event logging
│ ├── needs_analysis.py # Needs and prioritization analysis
│ └── recommendation.py # Recommendation engine algorithms
├── venv/ # Python virtual environment (optional)
├── requirements.txt # Python dependencies list
└── README.md # This documentation file

text

---

## Setup Instructions

1. **Clone the repository:**

git clone <repository-url>
cd INSURANCE_RECOMMENDER2

text

2. **(Optional) Create and activate a virtual environment:**

python -m venv venv

Windows
venv\Scripts\activate

macOS/Linux
source venv/bin/activate

text

3. **Install dependencies:**

pip install -r requirements.txt

text

4. **Run the app:**

streamlit run app.py


## Key Features Explained

- **Customer Management:** Add/edit detailed customer profiles including demographics, financials, health and risk scores.
- **Product Management:** Add/edit insurance products with premium, coverage, and description fields; compare products visually.
- **Recommendations:** Hybrid collaborative/filtering model offering ranked insurance products with explanations.
- **Life Stage & Needs Analysis:** Categorizes users based on life events to tailor recommendations.
- **Interactive Tools:** Savings calculators, charts, risk quizzes, and scenario planners for informed decision-making.
- **Data Persistence:** Uses CSV files for easy inspection and portability; designed for future DB integration.

---

## Technologies Used

- Python 3.8+
- Streamlit for interactive UI
- Pandas for data processing
- CSV files for data storage

---

## Future Improvements

- Integrate a database backend (e.g., PostgreSQL)
- Add secure password hashing and OAuth support
- Embed machine learning recommendation models
- Provide multi-language UI support
- Enhance frontend with advanced visualizations and real-time updates
- Deploy on a cloud platform with CI/CD pipelines

---

## Contribution Guidelines

Contributions are welcome! Please fork the repo and create a pull request with clear descriptions.

---

## Contact and Support

For questions, feature requests, or help, please open an issue on GitHub or contact the maintainers.

---

Enjoy personalized insurance planning with the Insurance Recommender App!  
🛡️🚀
