Insurance Recommender App 🛡️🚀

An interactive Streamlit application that provides personalized insurance product recommendations, life-stage analysis, and comprehensive customer and product management — all in one platform.

🌟 Features

🔐 Role-Based Authentication – Secure login for Admin and User roles with access control.

👤 Customer Profile Management – Add, view, update, and delete profiles with demographic, financial, and risk data.

📦 Insurance Product Management – Admins can manage insurance products and compare them visually.

🎯 Personalized Recommendations – Hybrid recommendation engine tailored to each customer’s life stage and profile.

📊 Life Stage & Goal Planning – Tools for financial goal setting, simulations, and what-if analysis.

📈 Interactive Dashboards – Charts, forms, product comparisons, and downloadable reports.

📝 Risk Tolerance Questionnaire – Integrated quiz to assess customer risk profile.

📂 Project Structure
.
├── app.py                     # Main app entry point & homepage
├── data/                      # CSV storage for customers & products
├── models/                    # Placeholder for ML models
├── pages/                     # Streamlit multipage feature pages
│   ├── 0_Product_Management.py
│   ├── 1_Customer_Management.py
│   ├── 2_Recommendations.py
│   ├── 5_Product_Comp.py
│   ├── 6_Log_Life_Event.py
│   ├── 7_Life_Goal_Planning.py
│   ├── 8_Multi_Profile_Management.py
│   ├── 9_What_If_Analysis.py
│   ├── 10_Savings_Calculator.py
│   └── 11_Interactive_Charts.py
├── utils/                     # Helper functions & logic
│   ├── file_manager.py
│   ├── life_stage.py
│   ├── logger.py
│   ├── needs_analysis.py
│   └── recommendation.py
├── requirements.txt           # Python dependencies
└── README.md                  # Documentation

⚙️ Setup Instructions

1️⃣ Clone the repository:

git clone <repository-url>
cd INSURANCE_RECOMMENDER2


2️⃣ (Optional) Create a virtual environment:

python -m venv venv


Windows:

venv\Scripts\activate


macOS/Linux:

source venv/bin/activate


3️⃣ Install dependencies:

pip install -r requirements.txt


4️⃣ Run the application:

streamlit run app.py

🔑 Default Admin Credentials

Username: admin

Password: admin@123

Change credentials after first login for security.

📜 Usage Overview

Before Login: Only login & signup pages are accessible.

User Role: Access personal recommendations, profile management, goal planning, and analysis tools.

Admin Role: Full control — manage all users, insurance products, and view all recommendations.

🛠️ Key Features Explained

Customer Management: Store detailed personal, financial, and health data.

Product Management: Manage and compare insurance products by premium, coverage, and benefits.

Recommendation Engine: Hybrid filtering logic to rank best-fit policies.

Life Stage & Needs Analysis: Adapts suggestions based on life events.

Interactive Tools: Savings calculators, what-if analysis, and visual comparisons.

Data Storage: Uses CSV for portability; future DB integration planned.

💻 Technologies Used

Python 3.8+

Streamlit – Interactive UI

Pandas – Data processing

CSV – Data storage

🚀 Future Improvements

Database integration (PostgreSQL/MySQL)

Secure password hashing & OAuth login

Machine learning model for recommendations

Multi-language UI

Real-time updates & advanced charts

Cloud deployment with CI/CD

🤝 Contribution Guidelines

Fork the repo.

Create a new branch (feature/YourFeature).

Commit changes with clear messages.

Submit a pull request.

📬 Contact

For queries, features, or support:
📧 Open an issue on GitHub or contact the maintainers.

Enjoy personalized insurance planning with the Insurance Recommender App!
