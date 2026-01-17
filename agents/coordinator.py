from agents.clinical_agent import clinical_agent
from agents.risk_agent import risk_agent
from agents.recommendation_agent import recommendation_agent

def coordinator(patient_data):
    # Extract name for personalization
    patient_name = patient_data.get('name')
    
    clinical_summary = clinical_agent(patient_data)
    risk = risk_agent(clinical_summary, patient_name)
    recommendation = recommendation_agent(clinical_summary, risk, patient_name)

    return {
        "clinical_summary": clinical_summary,
        "risk": risk,
        "recommendation": recommendation
    }
