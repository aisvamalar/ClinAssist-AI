from llm import call_llm

def risk_agent(clinical_summary, patient_name=None):
    name_reference = patient_name if patient_name else "the patient"
    greeting = f"Hello {patient_name}, " if patient_name else ""
    
    prompt = f"""You are a compassionate doctor assessing a patient's risk level. Explain this in a clear, reassuring way that helps the patient understand their situation.

Clinical Summary:
{clinical_summary}

Please provide a patient-friendly risk assessment that includes:

1. **Risk Level:** Clearly state if this is LOW, MODERATE, or HIGH risk (use capital letters and emoji if helpful: 🟢 Low, 🟡 Moderate, 🔴 High)

2. **What this means:** Explain what this risk level means in simple terms that a patient can understand

3. **Why this level:** Briefly explain what factors contributed to this risk assessment

4. **Reassurance:** Provide appropriate reassurance while being honest about any concerns

{greeting}Write in a warm, professional tone - like a doctor calmly explaining the situation to {name_reference}. Use clear formatting with headers or bold text for emphasis. Be specific and helpful. {"Use the patient's name naturally in your response." if patient_name else ""}"""
    
    return call_llm(prompt)
