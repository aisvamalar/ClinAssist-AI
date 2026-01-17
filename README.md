
# ClinAssist AI 🏥A multi-agent Clinical Decision Support System powered by NVIDIA AI, providing patient-friendly clinical analysis, risk assessment, and treatment recommendations.[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)[![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)](https://flask.palletsprojects.com/)[![Streamlit](https://img.shields.io/badge/Streamlit-Latest-red.svg)](https://streamlit.io/)[![NVIDIA AI](https://img.shields.io/badge/NVIDIA-AI-yellow.svg)](https://www.nvidia.com/)## 📋 Table of Contents- [Features](#-features)- [Screenshots](#-screenshots)- [Architecture](#-architecture)- [Prerequisites](#-prerequisites)- [Installation](#-installation)- [Configuration](#-configuration)- [Running the Application](#-running-the-application)- [Usage](#-usage)- [API Documentation](#-api-documentation)- [Project Structure](#-project-structure)- [Technologies Used](#-technologies-used)- [Contributing](#-contributing)- [License](#-license)## ✨ Features- 🏥 **Modern UI**: Beautiful dark-themed interface with purple-blue gradient accents- 👤 **Personalized Responses**: Patient name integration for customized, empathetic communication- 🤖 **Multi-Agent System**: Three specialized AI agents working in orchestrated workflow- 💬 **Patient-Friendly Language**: Clear, empathetic doctor-to-patient communication style- 📊 **Comprehensive Analysis**: Clinical summary, risk assessment, and treatment recommendations- ⚡ **Real-time Processing**: Fast AI-powered analysis using NVIDIA Foundation Models- 🎨 **Responsive Design**: Clean, professional medical interface optimized for usability## 📸 Screenshots### Main Interface![Main Interface](images/main-interface.png)*ClinAssist AI main interface with patient data input form*### Clinical Summary![Clinical Summary](images/clinical-summary.png)*Patient-friendly clinical summary with clear explanations*### Risk Assessment![Risk Assessment](images/risk-assessment.png)*Risk level assessment with color-coded indicators*### Recommendations![Recommendations](images/recommendations.png)*Comprehensive treatment recommendations including diagnosis, tests, and treatment plans*## 🏗️ ArchitectureClinAssist AI uses a **multi-agent orchestration system** where a coordinator manages three specialized AI agents in a sequential workflow.### System Components- **Coordinator**: Orchestrates the multi-agent workflow, manages data flow, and coordinates agent execution- **Clinical Agent**: Analyzes patient data (age, symptoms, SpO₂) and generates comprehensive clinical summaries- **Risk Agent**: Assesses patient risk level (Low/Moderate/High) based on clinical summary- **Recommendation Agent**: Provides diagnosis, tests, and treatment recommendations using clinical summary and risk assessment### Workflow Diagram
┌─────────────┐
│ Patient Data│
│ (Input) │
└──────┬──────┘
│
▼
┌──────────────────┐
│ Clinical Agent │ ───► Clinical Summary
└────────┬─────────┘
│
▼
┌──────────────────┐
│ Risk Agent │ ───► Risk Assessment
└────────┬─────────┘
│
▼
┌──────────────────┐
│Recommendation │ ───► Final Recommendations
│ Agent │
└──────────────────┘
### Technology Stack- **Backend**: Flask (REST API server)- **Frontend**: Streamlit (Interactive web interface)- **AI/ML**: NVIDIA AI Foundation Models (Meta Llama 3-8B Instruct)- **Architecture Pattern**: Multi-agent orchestration with coordinator pattern- **Language**: Python 3.8+## 📦 PrerequisitesBefore you begin, ensure you have:- **Python 3.8 or higher** installed on your system- **NVIDIA API Key** - Get your free API key from [NVIDIA AI Foundation Models](https://build.nvidia.com/ai-foundation-models)- **pip** (Python package manager)- **Git** (for cloning the repository)## 🔧 Installation### 1. Clone the Repositorygit clone https://github.com/aisvamalar/ClinAssist-AI.gitcd ClinAssist-AI### 2. Install Dependenciespip install -r requirements.txtThis will install the following packages:- `flask` - Web framework for the backend API- `streamlit` - Frontend web application framework- `requests` - HTTP library for API calls- `python-dotenv` - Environment variable management### 3. Set Up Virtual Environment (Recommended)# Create virtual environmentpython -m venv venv# Activate virtual environment# On Windows:venv\Scripts\activate# On macOS/Linux:source venv/bin/activate# Install dependenciespip install -r requirements.txt## ⚙️ Configuration### Environment Variables1. Create a `.env` file in the `backend/` directory:cd backendtouch .env  # On Windows: type nul > .env2. Add your NVIDIA API key to the `.env` file:NVIDIA_API_KEY=your_nvidia_api_key_here3. Replace `your_nvidia_api_key_here` with your actual NVIDIA API key.**⚠️ Important**: Never commit the `.env` file to version control. It's already included in `.gitignore`.## 🚀 Running the Application### Start the Backend Server1. Navigate to the backend directory:ashcd backend2. Start the Flask server:python app.pyYou should see:
2. Install Dependencies
pip install -r requirements.txtunning on `http://localhost:5000`.### Start the Frontend1. Open a **new terminal window** (keep the backend server running)2. Navigate to the frontend directory:cd frontend3. Start the Streamlit app:streamlit run app.pyThe Streamlit app will automatically open in your default web browser at `http://localhost:8501`.## 💻 Usage### Using the Web Interface1. **Enter Patient Information**:   - **Patient Name** (optional): Enter the patient's name for personalized responses   - **Patient Age**: Enter age in years (1-120)   - **Oxygen Saturation (SpO₂)**: Enter SpO₂ percentage (50-100)   - **Symptoms**: Enter symptoms separated by commas (e.g., "fever, cough, headache")2. **Run Analysis**:   - Click the **"🔍 Run Clinical Analysis"** button   - Wait for the AI agents to process the data (usually 10-30 seconds)3. **Review Results**:   - **Clinical Summary**: Overview of symptoms and vital signs in patient-friendly language   - **Risk Assessment**: Risk level classification (Low/Moderate/High) with explanations   - **Recommendations**: Diagnosis suggestions, recommended tests, and treatment plans### Example Input
This will install the following packages:
flask - Web framework for the backend API
streamlit - Frontend web application framework
requests - HTTP library for API calls
python-dotenv - Environment variable management
3. Set Up Virtual Environment (Recommended)
# Create virtual environmentpytwill provide:- **Clinical Summary**: "Hello Sarah! Based on your symptoms..."- **Risk Assessment**: "🟡 Moderate Risk - Your symptoms indicate..."- **Recommendations**: "Likely Diagnosis: Upper respiratory infection..."## 📡 API Documentation### Endpoint: `/cds`**Method**: `POST`**Content-Type**: `application/json`**Request Body**:{  "name": "string (optional)",  "age": 25,  "symptoms": "fever, cough, headache",  "spo2": 95}**Response**:on{  "clinical_summary": "Patient-friendly clinical summary...",  "risk": "Risk assessment with level...",  "recommendation": "Diagnosis, tests, and treatment recommendations..."}**Example cURL Request**:hcurl -X POST http://localhost:5000/cds \  -H "Content-Type: application/json" \  -d '{    "name": "John",    "age": 35,    "symptoms": "fever, cough",    "spo2": 96  }'## 📁 Project Structure
⚙️ Configuration
Environment Variables
Create a .env file in the backend/ directory:
cd backendtouch .env  # On Windows: type nul > .env[Flask](https://flask.palletsprojects.com/) - Lightweight Python web framework- **Frontend Framework**: [Streamlit](https://streamlit.io/) - Rapid web app development- **AI Model**: [NVIDIA AI Foundation Models](https://www.nvidia.com/en-us/ai-data-science/foundation-models/) - Meta Llama 3-8B Instruct- **Language**: Python 3.8+- **HTTP Client**: [Requests](https://requests.readthedocs.io/) - HTTP library- **Environment Management**: [python-dotenv](https://github.com/theskumar/python-dotenv) - .env file support## 🤝 ContributingContributions are welcome! Please follow these steps:1. Fork the repository2. Create a feature branch (`git checkout -b feature/AmazingFeature`)3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)4. Push to the branch (`git push origin feature/AmazingFeature`)5. Open a Pull Request### Development Guidelines- Follow PEP 8 Python style guidelines- Add comments for complex logic- Update README.md if adding new features- Test your changes before submitting## ⚠️ Disclaimer**ClinAssist AI is for educational purposes only. It is not a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of qualified health providers with any questions you may have regarding a medical condition.**## 📄 LicenseThis project is open source and available under the [MIT License](LICENSE).## 👥 Authors- **Aisvamalar** - [GitHub Profile](https://github.com/aisvamalar)## 🙏 Acknowledgments- NVIDIA for providing AI Foundation Models- Meta for the Llama 3 model- Streamlit and Flask communities for excellent documentation- Open source contributors who made this project possible## 📞 SupportFor issues, questions, or contributions:- Open an issue on [GitHub Issues](https://github.com/aisvamalar/ClinAssist-AI/issues)- Check existing documentation and FAQs---⭐ If you find this project helpful, please consider giving it a star on GitHub!
Add your NVIDIA API key to the .env file:
NVIDIA_API_KEY=you
Replace your_nvidia_api_key_here with your actual NVIDIA API key.
⚠️ Important: Never commit the .env file to version control. It's already included in .gitignore.
🚀 Running the Application
Start the Backend Server
Navigate to the backend directory:
cd backend
Start the Flask server:
python app.py
You should see:
 * Running on http://127.0.0.1:5000 * Running on http://[::1]:5000
The Flask API server will be running on http://localhost:5000.
Start the Frontend
Open a new terminal window (keep the backend server running)
Navigate to the frontend directory:
cd frontend
Start the Streamlit app:
streamlit run app.py
The Streamlit app will automatically open in your default web browser at http://localhost:8501.
💻 Usage
Using the Web Interface
Enter Patient Information:
Patient Name (optional): Enter the patient's name for personalized responses
Patient Age: Enter age in years (1-120)
Oxygen Saturation (SpO₂): Enter SpO₂ percentage (50-100)
Symptoms: Enter symptoms separated by commas (e.g., "fever, cough, headache")
Run Analysis:
Click the "🔍 Run Clinical Analysis" button
Wait for the AI agents to process the data (usually 10-30 seconds)
Review Results:
Clinical Summary: Overview of symptoms and vital signs in patient-friendly language
Risk Assessment: Risk level classification (Low/Moderate/High) with explanations
Recommendations: Diagnosis suggestions, recommended tests, and treatment plans
Example Input
Patient Name: SarahAge
Example Output
The system will provide:
Clinical Summary: "Hello Sarah! Based on your symptoms..."
Risk Assessment: "🟡 Moderate Risk - Your symptoms indicate..."
Recommendations: "Likely Diagnosis: Upper respiratory infection..."
📡 API Documentation
Endpoint: /cds
Method: POST
Content-Type: application/json
Request Body:
{  "name": "string (optional)",  "age": 25,  "symptoms": "fever, cough, headache",  "spo2": 95}
Response:
{  "clinical_summary": "Patient-friendly clinical summary...",  "risk": "Risk assessment with level...",  "recommendation": "Diagnosis, tests, and treatment recommendations..."}
Example cURL Request:
curl -X POST http://localhost:5000/cds \  -H "Content-Type: application/json" \  -d '{    "name": "John",    "age": 35,    "symptoms": "fever, cough",    "spo2": 96  }'
📁 Project Structure
ClinAssist-AI/│├── backend/                    # Backend API server│   ├── agents/                # Multi-agent system│   │   ├── __init__.py│   │   ├── coordinator.py     # Orchestrates multi-agent workflow│   │   ├── clinical_agent.py  # Clinical analysis agent│   │   ├── risk_agent.py      # Risk assessment agent│   │   └── recommendation_agent.py  # Treatment recommendation agent│   ├── app.py                 # Flask server and API endpoints│   ├── llm.py                 # NVIDIA AI integration and LLM calls│   └── .env                   # Environment variables (not in git)│├── frontend/                   # Frontend web application│   ├── __init__.py│   └── app.py                 # Streamlit interface│├── images/                     # Screenshots for README (optional)│   ├── main-interface.png│   ├── clinical-summary.png│   ├── risk-assessment.png│   └── recommendations.png│├── .gitignore                  # Git ignore rules├── requirements.txt            # Python dependencies└── README.md                   # This file
🛠️ Technologies Used
Backend Framework: Flask - Lightweight Python web framework
Frontend Framework: Streamlit - Rapid web app development
AI Model: NVIDIA AI Foundation Models - Meta Llama 3-8B Instruct
Language: Python 3.8+
HTTP Client: Requests - HTTP library
Environment Management: python-dotenv - .env file support
🤝 Contributing
Contributions are welcome! Please follow these steps:
Fork the repository
Create a feature branch (git checkout -b feature/AmazingFeature)
Commit your changes (git commit -m 'Add some AmazingFeature')
Push to the branch (git push origin feature/AmazingFeature)
Open a Pull Request
Development Guidelines
Follow PEP 8 Python style guidelines
Add comments for complex logic
Update README.md if adding new features
Test your changes before submitting
⚠️ Disclaimer
ClinAssist AI is for educational purposes only. It is not a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of qualified health providers with any questions you may have regarding a medical condition.
📄 License
This project is open source and available under the MIT License.
👥 Authors
Aisvamalar 
