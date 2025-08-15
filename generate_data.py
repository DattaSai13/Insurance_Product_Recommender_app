import pandas as pd
import random
from faker import Faker

fake = Faker()
random.seed(42)

# Customers Data
customers = []
for i in range(10):
    age = random.randint(18, 70)
    customers.append({
        "customer_id": i+1,
        "age": age,
        "gender": random.choice(["Male", "Female"]),
        "marital_status": random.choice(["Single", "Married"]),
        "dependents": random.randint(0, 3),
        "occupation": random.choice(["Engineer", "Teacher", "Business", "Doctor", "Student", "Retired"]),
        "income": random.randint(20000, 200000),
        "health_score": round(random.uniform(0, 1), 2),
        "risk_score": round(random.uniform(0, 1), 2),
        "life_events": random.choice(["None", "Marriage", "Child Birth", "Job Change"])
    })

pd.DataFrame(customers).to_csv("data/customers.csv", index=False)

# Products Data
products = []
for pid in range(10):
    products.append({
        "product_id": pid+1,
        "product_name": f"Plan {pid+1}",
        "product_type": random.choice(["Health", "Life", "Auto", "Home"]),
        "min_age": random.randint(18, 30),
        "max_age": random.randint(50, 70),
        "risk_category": random.choice(["Low", "Medium", "High"]),
        "premium_range": f"${random.randint(100,500)}/mo",
        "coverage_type": random.choice(["Comprehensive", "Basic", "Premium"]),
        "description": fake.text(max_nb_chars=50)
    })

pd.DataFrame(products).to_csv("data/products.csv", index=False)

# Mapping Data
mapping = []
life_stages = ["Child", "Young Adult", "Adult", "Senior"]
risk_cats = ["Low", "Medium", "High"]
for stage in life_stages:
    for risk in risk_cats:
        mapping.append({
            "life_stage": stage,
            "risk_category": risk,
            "suitable_products": ",".join(map(str, random.sample(range(1, 11), 3)))
        })

pd.DataFrame(mapping).to_csv("data/product_mapping.csv", index=False)

print("Synthetic data generated successfully!")
