import streamlit as st
import pandas as pd

CUSTOMERS_CSV = "data/customers.csv"

def load_customers():
    try:
        df = pd.read_csv(CUSTOMERS_CSV)
    except FileNotFoundError:
        df = pd.DataFrame(columns=[
            'customer_id', 'age', 'gender', 'marital_status', 'dependents',
            'occupation', 'income', 'health_score', 'risk_score', 'life_events', 'financial_goals'
        ])
        df.to_csv(CUSTOMERS_CSV, index=False)
    return df

def add_customer(data):
    df = load_customers()
    # Assign new unique customer_id
    if df.empty:
        max_id = 0
    else:
        max_id = df['customer_id'].astype(int).max()
    new_id = max_id + 1
    data['customer_id'] = new_id
    df = pd.concat([df, pd.DataFrame([data])], ignore_index=True)
    df.to_csv(CUSTOMERS_CSV, index=False)
    return new_id

def update_customer(customer_id, updated_data):
    df = load_customers()
    customer_id = str(customer_id)
    df['customer_id'] = df['customer_id'].astype(str)
    idx_match = df.index[df['customer_id'] == customer_id]
    if len(idx_match) == 0:
        return False
    idx = idx_match[0]
    for key, value in updated_data.items():
        if key in df.columns:
            df.at[idx, key] = value
    df.to_csv(CUSTOMERS_CSV, index=False)
    return True

def delete_customer(customer_id):
    df = load_customers()
    customer_id = str(customer_id)
    df['customer_id'] = df['customer_id'].astype(str)
    df = df[df['customer_id'] != customer_id]
    df.to_csv(CUSTOMERS_CSV, index=False)

st.set_page_config(page_title="Manage Customers", layout="wide")
st.title("👥 Customer Profile Management")

customers_df = load_customers()

st.sidebar.header("Select Action")
action = st.sidebar.radio("Choose:", ["View Customers", "Add Customer", "Modify Customer", "Delete Customer"])

st.sidebar.write("---")
st.sidebar.write(f"Total customers: {len(customers_df)}")

if action == "View Customers":
    st.subheader("View Customers")
    search = st.text_input("Search by Occupation, Gender, or Marital Status")
    filtered_df = customers_df
    if search:
        filtered_df = customers_df[customers_df.apply(lambda x: search.lower() in str(x).lower(), axis=1)]
    st.dataframe(filtered_df)

elif action == "Add Customer":
    st.subheader("➕ Add New Customer Profile")

    def risk_tolerance_quiz():
        st.markdown("### 📝 Risk Tolerance Questionnaire")
        age_group = st.selectbox("Your age group:", ["Under 25", "25-40", "41-60", "Over 60"])
        income_stability = st.selectbox(
            "How stable is your income?", ["Very stable", "Somewhat stable", "Unstable", "No income"]
        )
        dependents_q = st.radio("How many financial dependents do you have?", ["0", "1", "2 or more"])
        health_rating = st.selectbox("How would you rate your current health?", ["Excellent", "Good", "Fair", "Poor"])
        risk_feeling = st.slider("How comfortable are you with financial risk?", 1, 5)
        points = 0
        if age_group == "Under 25":
            points += 2
        elif age_group == "25-40":
            points += 1
        elif age_group == "Over 60":
            points -= 1
        if income_stability == "Unstable":
            points -= 1
        if income_stability == "No income":
            points -= 2
        if income_stability == "Very stable":
            points += 2
        if dependents_q == "2 or more":
            points -= 2
        if dependents_q == "1":
            points -= 1
        if health_rating == "Excellent":
            points += 2
        elif health_rating == "Poor":
            points -= 2
        elif health_rating == "Fair":
            points -= 1
        points += (risk_feeling - 3)
        risk_score = (points + 6) / 12
        risk_score = min(max(risk_score, 0), 1)
        st.info(f"Your calculated risk score: **{risk_score:.2f}** (0 = Very Low, 1 = Very High)")
        dependents_val = 2 if dependents_q == "2 or more" else int(dependents_q)
        return risk_score, dependents_val

    with st.form(key="add_customer_form"):
        age = st.number_input("Age", min_value=0, max_value=100, value=18)
        gender = st.radio("Gender", ["Male", "Female"])
        marital_status = st.radio("Marital Status", ["Single", "Married"])
        occupation_options = ["Engineer", "Teacher", "Business", "Doctor", "Student", "Retired", "Other"]
        occupation = st.selectbox("Occupation", occupation_options)
        if occupation == "Other":
            other_occupation = st.text_input("Please specify your occupation")
        else:
            other_occupation = None
        income = 0 if occupation == "Student" else st.number_input("Income ($)", min_value=0, max_value=500000, value=30000)
        health_score = st.slider("Health Score (0 - Poor, 1 - Excellent)", 0.0, 1.0, 0.7)
        calculated_risk_score, dependents = risk_tolerance_quiz()
        life_events = st.selectbox("Recent Life Event", ["None", "Marriage", "Child Birth", "Job Change"])
        financial_goals = st.text_area("Financial Goals (optional)", "")
        submit_btn = st.form_submit_button("Add Customer")
        if submit_btn:
            occupation_final = other_occupation.strip() if other_occupation else occupation
            data = dict(
                age=age,
                gender=gender,
                marital_status=marital_status,
                dependents=dependents,
                occupation=occupation_final,
                income=income,
                health_score=health_score,
                risk_score=calculated_risk_score,
                life_events=life_events,
                financial_goals=financial_goals
            )
            new_id = add_customer(data)
            st.success(f"Customer profile added! Unique ID: {new_id}")
            st.rerun()

elif action == "Modify Customer":
    st.subheader("✏️ Edit Customer Profile")
    customers_df = load_customers()
    if customers_df.empty:
        st.info("No customers found. Please add customers first.")
        st.stop()
    customer_id = st.selectbox("Select Customer ID", customers_df['customer_id'].astype(str))
    current_customer = customers_df[customers_df['customer_id'].astype(str) == customer_id].iloc[0].to_dict()
    event_options = ["None", "Marriage", "Child Birth", "Job Change"]
    current_event = current_customer.get('life_events')
    if current_event not in event_options:
        current_event = "None"
    with st.form(key="edit_customer_form"):
        age = st.number_input("Age", min_value=0, max_value=100, value=int(current_customer['age']))
        gender = st.radio("Gender", ["Male", "Female"], index=0 if current_customer['gender'] == "Male" else 1)
        marital_status = st.radio("Marital Status", ["Single", "Married"], index=0 if current_customer['marital_status'] == "Single" else 1)
        dependents = st.number_input("Number of Dependents", min_value=0, max_value=10, value=int(current_customer['dependents']))
        occupation = st.text_input("Occupation", current_customer['occupation'])
        income = st.number_input("Income ($)", min_value=0, max_value=1000000, value=int(round(float(current_customer['income']))))
        health_score = st.slider("Health Score (0 - Poor, 1 - Excellent)", 0.0, 1.0, float(current_customer['health_score']))
        risk_score = st.slider("Risk Score (0 - Low, 1 - High)", 0.0, 1.0, float(current_customer['risk_score']))
        life_events = st.selectbox("Recent Life Event", event_options, index=event_options.index(current_event))
        financial_goals = st.text_area("Financial Goals (optional)", current_customer.get("financial_goals", ""))
        submit = st.form_submit_button("Save Changes")
        if submit:
            updated_data = {
                "age": age,
                "gender": gender,
                "marital_status": marital_status,
                "dependents": dependents,
                "occupation": occupation,
                "income": income,
                "health_score": health_score,
                "risk_score": risk_score,
                "life_events": life_events,
                "financial_goals": financial_goals
            }
            success = update_customer(customer_id, updated_data)
            if success:
                st.success("Customer updated successfully!")
                st.rerun()
            else:
                st.error("Error updating customer.")

elif action == "Delete Customer":
    st.subheader("🗑️ Delete Customer")
    customers_df = load_customers()
    if customers_df.empty:
        st.info("No customers found.")
        st.stop()
    customer_id = st.selectbox("Select Customer ID to Delete", customers_df['customer_id'].astype(str))
    customer = customers_df[customers_df['customer_id'].astype(str) == customer_id].iloc[0]
    st.write(f"Selected Customer - ID: **{customer_id}**, Occupation: {customer['occupation']}, Gender: {customer['gender']}")
    if st.button("Delete Customer"):
        delete_customer(customer_id)
