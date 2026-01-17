from llm import call_llm

def recommendation_agent(clinical_summary, risk, patient_name=None):
    name_reference = patient_name if patient_name else "the patient"
    greeting = f"Hello {patient_name}, " if patient_name else ""
    
    prompt = f"""You are an experienced, empathetic doctor providing recommendations to a patient. Explain everything clearly and in simple terms.

Clinical Summary:
{clinical_summary}

Risk Assessment:
{risk}

Please provide a comprehensive, patient-friendly recommendation that includes:

## **Likely Diagnosis**
- Explain the most probable conditions in simple terms
- What each condition means in everyday language

## **Recommended Tests**
- List specific tests or examinations that would help confirm the diagnosis
- Briefly explain what each test involves and why it's important

## **Treatment Suggestions**
- Initial treatment recommendations (medications, lifestyle changes, etc.)
- Explain how each treatment helps
- Any immediate actions {name_reference} should take

## **Next Steps**
- What should happen next (follow-up appointment, monitoring, etc.)
- When to seek immediate medical attention
- Any warning signs to watch for

{greeting}Format this conversationally, as if you're sitting with {name_reference} explaining their care plan. Use clear headings, bullet points, and structure the information so it's easy to follow. Be encouraging and practical. {"Use the patient's name naturally throughout your response." if patient_name else ""}"""
    
    return call_llm(prompt)
