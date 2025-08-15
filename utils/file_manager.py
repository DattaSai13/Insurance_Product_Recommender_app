import pandas as pd

def load_customers(filepath="data/customers.csv"):
    try:
        return pd.read_csv(filepath)
    except FileNotFoundError:
        return pd.DataFrame(columns=[
            'customer_id', 'age', 'gender', 'marital_status', 'dependents',
            'occupation', 'income', 'health_score', 'risk_score', 'life_events'
        ])

def save_customers(df, filepath="data/customers.csv"):
    df.to_csv(filepath, index=False)

def add_customer(new_data, filepath="data/customers.csv"):
    df = load_customers(filepath)
    if df.empty:
        next_id = 1
    else:
        next_id = df['customer_id'].max() + 1
    new_data['customer_id'] = next_id
    df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
    save_customers(df, filepath)
    return next_id

def update_customer(customer_id, updated_data, filepath="data/customers.csv"):
    df = load_customers(filepath)
    idx = df.index[df['customer_id'] == customer_id]
    if not idx.empty:
        for key, value in updated_data.items():
            df.at[idx[0], key] = value
        save_customers(df, filepath)
        return True
    return False

def delete_customer(customer_id, filepath="data/customers.csv"):
    df = load_customers(filepath)
    df = df[df['customer_id'] != customer_id]
    save_customers(df, filepath)
    return True

def load_products(filepath="data/products.csv"):
    try:
        return pd.read_csv(filepath)
    except FileNotFoundError:
        return pd.DataFrame(columns=[
            'product_id', 'product_name', 'product_type', 'min_age', 'max_age',
            'risk_category', 'premium_range', 'coverage_type', 'description'
        ])
