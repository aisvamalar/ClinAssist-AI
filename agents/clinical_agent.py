from llm import call_llm

def clinical_agent(patient_data):
    name = patient_data.get('name')
    age = patient_data.get('age', 'Not specified')
    symptoms = patient_data.get('symptoms', 'Not specified')
    spo2 = patient_data.get('spo2', 'Not specified')
    
    # Personalized greeting
    greeting = f"Hello {name}, " if name else ""
    name_reference = name if name else "the patient"
    
    prompt = f"""You are a caring and experienced doctor explaining a patient's clinical presentation in simple, understandable terms.

Patient Information:
{f"- Name: {name}" if name else ""}
- Age: {age} years old
- Symptoms: {symptoms}
- Oxygen Saturation (SpO₂): {spo2}%

Please provide a clear, patient-friendly clinical summary that explains:
1. **What we know:** Summarize the main symptoms and vital signs in simple language
2. **What it means:** Explain what the oxygen saturation level indicates (normal is typically 95-100%)
3. **Key observations:** Highlight any concerning signs or patterns you notice

{greeting}Write this as if you're talking directly to {name_reference} or their family - use clear language, be empathetic, and avoid unnecessary medical jargon. Format it with clear sections and bullet points for easy reading. {"Use the patient's name naturally throughout your response." if name else ""}"""
    
    return call_llm(prompt)
