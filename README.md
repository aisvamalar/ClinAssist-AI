<img width="3788" height="1797" alt="Screenshot 2026-01-17 231151" src="https://github.com/user-attachments/assets/379bd62f-8b09-4297-9041-737062fc5718" /><img width="3829" height="2069" alt="Screenshot 2026-01-17 231121" src="https://github.com/user-attachments/assets/dda1818d-600c-4c2f-8094-d6a35351a100" /># 🏥 ClinAssist AI - NVIDIA Powered Clinical Decision Support

A multi-agent AI system providing intelligent clinical analysis, risk assessment, and treatment recommendations using NVIDIA Foundation Models.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/) [![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)](https://flask.palletsprojects.com/) [![Streamlit](https://img.shields.io/badge/Streamlit-Latest-red.svg)](https://streamlit.io/) [![NVIDIA AI](https://img.shields.io/badge/NVIDIA-AI-76B900.svg)](https://www.nvidia.com/)

---

## 📸 Demo

<img width="3829" height="2069" alt="Screenshot 2026-01-17 231121" src="https://github.com/user-attachments/assets/35f48bd5-c7e7-4cc9-a36a-c2038864519a" />
<img width="3803" height="1952" alt="Screenshot 2026-01-17 231136" src="https://github.com/user-attachments/assets/71bf9674-fcdd-49fc-872a-152b691c9d10" />
![Uploading Screenshot 2026-01-17 231151.png…]()


*ClinAssist AI analyzing patient symptoms with AI-powered clinical insights*

---

## ✨ Features | 🏗️ Architecture

**🤖 Multi-Agent System** - Orchestrated AI workflow  
**💬 Patient-Friendly** - Empathetic communication  
**📊 Comprehensive** - Summary, risk, recommendations  
**⚡ Real-time** - Fast NVIDIA AI processing  

```
Patient Data → Clinical Agent → Risk Agent → Recommendation Agent → Results
```

**Clinical Agent**: Analyzes symptoms & vitals  
**Risk Agent**: Assesses severity (Low/Moderate/High)  
**Recommendation Agent**: Diagnosis & treatment plan

---

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8+ | [NVIDIA API Key](https://build.nvidia.com/) (Free)

### Quick Start

```bash
# 1. Clone repository
git clone https://github.com/aisvamalar/ClinAssist-AI.git
cd ClinAssist-AI

# 2. Install dependencies
pip install -r requirements.txt

# 3. Configure API key
cd backend
echo NVIDIA_API_KEY=your_api_key_here > .env

# 4. Run backend (Terminal 1)
python app.py

# 5. Run frontend (Terminal 2 - new terminal)
cd ../frontend
streamlit run app.py
```

App opens at `http://localhost:8501`

---

## 💻 Usage

### Input
- **Name**: Sarah (optional)
- **Age**: 28 years
- **SpO₂**: 94%
- **Symptoms**: fever, cough, fatigue

### Output
✅ **Clinical Summary**: "Hello Sarah! Your symptoms suggest..."  
⚠️ **Risk Assessment**: "🟡 Moderate Risk - Respiratory symptoms with low SpO₂"  
💊 **Recommendations**: "Diagnosis: Upper respiratory infection. Tests: Chest X-ray, CBC..."

---

## 📡 API Reference

**Endpoint**: `POST /cds`

```json
// Request
{
  "name": "Sarah",
  "age": 28,
  "symptoms": "fever, cough",
  "spo2": 94
}

// Response
{
  "clinical_summary": "Clinical analysis...",
  "risk": "Risk assessment...",
  "recommendation": "Treatment plan..."
}
```

**cURL Example**:
```bash
curl -X POST http://localhost:5000/cds \
  -H "Content-Type: application/json" \
  -d '{"name":"Sarah","age":28,"symptoms":"fever, cough","spo2":94}'
```

---

## 📁 Project Structure

```
ClinAssist-AI/
├── backend/
│   ├── agents/
│   │   ├── coordinator.py          # Orchestrates workflow
│   │   ├── clinical_agent.py       # Clinical analysis
│   │   ├── risk_agent.py           # Risk assessment
│   │   └── recommendation_agent.py # Treatment plan
│   ├── app.py                      # Flask API
│   ├── llm.py                      # NVIDIA AI integration
│   └── .env                        # API key (create this)
├── frontend/
│   └── app.py                      # Streamlit UI
└── requirements.txt                # Dependencies
```

---

## 🛠️ Tech Stack

**Backend**: Flask | **Frontend**: Streamlit | **AI**: NVIDIA Llama 3-8B | **Language**: Python 3.8+

---

## 🤝 Contributing

1. Fork → 2. Branch (`git checkout -b feature/Amazing`) → 3. Commit → 4. Push → 5. Pull Request

Follow PEP 8, add comments, test before submitting.

---

## ⚠️ Disclaimer

**Educational purposes only.** Not a substitute for professional medical advice. Always consult qualified healthcare providers.

---

## 📄 License | 👥 Author | 📞 Support

**MIT License** | **[Aisvamalar](https://github.com/aisvamalar)** | **[Issues](https://github.com/aisvamalar/ClinAssist-AI/issues)**

---

### 🙏 Acknowledgments
NVIDIA AI Foundation Models • Meta Llama 3 • Streamlit & Flask Communities

---

⭐ **Star this repo if you find it helpful!**
