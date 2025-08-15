from .life_stage import classify_life_stage, insurance_needs_by_stage

def analyze_needs(customer):
    stage = classify_life_stage(customer['age'])
    needs = insurance_needs_by_stage(stage)
    priority = {need: 1 for need in needs}

    # Advanced triggers
    if customer.get('occupation') == "Business":
        priority["Wealth Protection"] = 2
    if customer.get('health_score', 1) < 0.4:
        priority["Critical Illness"] = 2
    if customer.get('dependents', 0) >= 2:
        priority["Family Cover"] = 2
    if customer.get('life_events') in ["Marriage", "Child Birth"]:
        priority["Family Cover"] = 2
    if customer.get('income', 0) > 130000:
        priority["Wealth Protection"] = 2
    
    # Sort needs by highest priority
    sorted_needs = dict(sorted(priority.items(), key=lambda x: -x[1]))
    return sorted_needs, stage
