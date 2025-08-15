def classify_life_stage(age):
    if age <= 18:
        return "Child"
    elif age <= 30:
        return "Young Adult"
    elif age <= 50:
        return "Adult"
    else:
        return "Senior"

def insurance_needs_by_stage(stage):
    return {
        "Child": ["Health Insurance"],
        "Young Adult": ["Health Insurance", "Term Life", "Travel Insurance"],
        "Adult": ["Life", "Health", "Home", "Critical Illness", "Family Cover"],
        "Senior": ["Health", "Retirement Plan", "Critical Illness"]
    }.get(stage, [])
