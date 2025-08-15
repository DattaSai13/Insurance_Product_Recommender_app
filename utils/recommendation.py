import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import joblib
import os

def content_based(customer, products_df):
    scores = []
    top_triggers = []
    for _, p in products_df.iterrows():
        triggers = []
        score = 0
        # Age match
        if p['min_age'] <= customer['age'] <= p['max_age']:
            score += 1
            triggers.append(f"Age({customer['age']}) matches product age range")
        # Risk profile
        rp = customer['risk_score']
        risk_match = (
            (rp <= 0.3 and p['risk_category'] == "Low") or
            (0.3 < rp <= 0.6 and p['risk_category'] == "Medium") or
            (rp > 0.6 and p['risk_category'] == "High")
        )
        if risk_match:
            score += 1
            triggers.append(f"Risk score({customer['risk_score']:.2f}) matches product risk ({p['risk_category']})")
        scores.append(score)
        top_triggers.append(", ".join(triggers) if triggers else "General match")
    return np.array(scores), top_triggers

def collaborative_filtering(customers_df, products_df, customer_id):
    df_reset = customers_df.reset_index(drop=True)
    features = df_reset[['income', 'risk_score']].values
    sim_matrix = cosine_similarity(features)
    idx = df_reset[df_reset['customer_id'] == customer_id].index[0]
    similar_indices = sim_matrix[idx].argsort()[::-1][1:4]
    recommended_products = set()
    for sim_idx in similar_indices:
        recommended_products.update(products_df.sample(2)['product_id'].tolist())
    return list(recommended_products)


def hybrid_recommendation(customer, customers_df, products_df):
    cb_scores, cb_triggers = content_based(customer, products_df)
    cf_products = collaborative_filtering(customers_df, products_df, customer['customer_id'])

    final_scores = []
    confidence = []
    explanations = []
    all_triggers = []
    for idx, row in products_df.iterrows():
        cf_score = 1 if row['product_id'] in cf_products else 0
        score = 0.6 * cb_scores[idx] + 0.4 * cf_score
        confidence_val = f"{int((score/2)*100)}%"
        triggers = cb_triggers[idx]
        explain_items = []
        if cb_scores[idx] > 0:
            explain_items.append(triggers)
        if cf_score:
            explain_items.append("Picked by users similar to you")
        if cb_scores[idx] == 0 and cf_score == 0:
            explain_items.append("General recommendation based on availability")
        explanations.append("; ".join(explain_items))
        confidence.append(confidence_val)
        all_triggers.append(triggers)
        final_scores.append(score)

    products_df = products_df.copy()
    products_df['score'] = final_scores
    products_df['explanation'] = explanations
    products_df['confidence'] = confidence
    products_df['top_triggers'] = all_triggers
    products_df = products_df.sort_values(by='score', ascending=False)
    return products_df
