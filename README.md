# AgriSetu AI

An interoperable AI-powered agricultural intelligence network for climate-resilient and regenerative farming across BRICS nations.

Built for Hack2Skill — Build with AI: Code for Communities (C4C)
Track 4 — AgriN & Regenerative Agricultural Intelligence

--------------------------------------------------

THE PROBLEM

Small and marginal farmers across emerging economies often lack access to timely, localised and data-driven agricultural guidance. Limited access to weather intelligence, environmental data and AI-powered decision support can increase crop risks and reduce climate resilience.

At the same time, agricultural data and knowledge systems remain fragmented across countries, limiting opportunities for cooperation on sustainable and climate-resilient food production.

--------------------------------------------------

OUR SOLUTION

AgriSetu AI is a focused agricultural intelligence MVP that combines:

- Real-time weather and environmental context
- Google Gemini AI
- Regenerative agriculture recommendations
- AI-assisted crop disease diagnosis
- BRICS-inspired interoperable agricultural cooperation

The platform is built around a key principle:

Local agricultural data remains sovereign while standardised, anonymised insights and interoperable models can be shared to strengthen climate-resilient farming across BRICS nations.

--------------------------------------------------

CORE FEATURES

1. AI AGRO-ADVISORY

Farmers provide simple farm information:

- BRICS country
- Location
- Current crop
- Crop growth stage
- Soil type
- Optional soil pH
- Optional organic matter information
- Farm size

AgriSetu AI combines this information with real weather and environmental data to generate a practical, localised agricultural advisory.

Farmer and Farm Data
        |
        v
Location Intelligence
        |
        v
Real Weather and Environmental Data
        |
        v
Google Gemini AI
        |
        v
Localised Agro-Advisory

ADVISORY OUTPUT

- Climate Summary
- Soil Health Assessment
- Crop and Farming Recommendation
- Regenerative Practices
- Water Management
- Risk Alerts
- Next 7-Day Action Plan

The system is designed to remain useful even when farmers do not know advanced soil information such as exact pH or organic matter values.

--------------------------------------------------

2. AI CROP DISEASE DIAGNOSIS

Farmers can describe crop symptoms naturally in:

- English
- Hindi
- Hinglish
- Roman Hindi
- Simple informal language

Example:

Tamatar mein chote chote holes aur brown spots hain.

Farmers can also optionally upload a crop or leaf image.

DIAGNOSIS OUTPUT

The AI provides a careful possible diagnosis, including:

- Possible Problem
- Confidence Level
- Severity
- Likely Causes
- Immediate Actions
- Sustainable Treatment Suggestions
- Prevention Advice
- Expert Verification Note

The system supports:

Symptoms Only
      |
      v
AI-Assisted Diagnosis

and:

Symptoms + Crop Image
          |
          v
AI Multimodal Analysis
          |
          v
AI-Assisted Diagnosis

Note: The diagnosis is AI-assisted guidance and should not be considered a laboratory-confirmed diagnosis.

--------------------------------------------------

3. BRICS AGRIN COOPERATION HUB

AgriSetu AI is designed as more than a single-country farmer application.

The BRICS AgriN Cooperation Hub demonstrates how interoperable agricultural intelligence can support cooperation between:

- Brazil
- Russia
- India
- China
- South Africa

INTEROPERABILITY MODEL

Local Agricultural Data
          |
          v
Standardise
          |
          v
Anonymise
          |
          v
Share Insights and Models
          |
          v
Stronger Climate-Resilient Agriculture

The concept focuses on sharing standardised and anonymised:

- Climate insights
- Soil intelligence models
- Crop disease patterns
- Regenerative agriculture knowledge

while respecting local agricultural data sovereignty.

This demonstrates a scalable digital public infrastructure approach without claiming that a real international agricultural database has been created.

--------------------------------------------------

TECHNOLOGY STACK

BACKEND

- Python
- Django

ARTIFICIAL INTELLIGENCE

- Google Gemini API

WEATHER AND ENVIRONMENTAL INTELLIGENCE

- Open-Meteo Geocoding API
- Open-Meteo Weather Forecast API

FRONTEND

- Django Templates
- Bootstrap
- Custom CSS
- JavaScript

DATABASE

- SQLite for the MVP and development environment

--------------------------------------------------

PROJECT ARCHITECTURE

AgriSetu AI
|
|-- Django Frontend
|   |-- Home
|   |-- AI Advisory
|   |-- Crop Diagnosis
|   |-- BRICS AgriN Hub
|
|-- Django Backend
|   |-- Views
|   |-- Weather Service
|   |-- AI Service
|
|-- External Intelligence
|   |-- Open-Meteo APIs
|   |-- Google Gemini API
|
|-- SQLite

--------------------------------------------------

LOCAL INSTALLATION

1. Clone the Repository

git clone YOUR_REPOSITORY_URL

cd agrisetu_ai


2. Create a Virtual Environment

python -m venv venv


Windows:

venv\Scripts\activate


macOS / Linux:

source venv/bin/activate


3. Install Dependencies

pip install -r requirements.txt


4. Configure Environment Variables

Create a .env file in the project root:

DJANGO_SECRET_KEY=your_django_secret_key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost

GEMINI_API_KEY=your_gemini_api_key

You can use .env.example as a reference.

Never commit your .env file or real API keys to a public repository.

5. Run Migrations

python manage.py migrate


6. Start the Development Server

python manage.py runserver


Open:

http://127.0.0.1:8000/

--------------------------------------------------

TESTING

Run Django system checks:

python manage.py check


Run the automated test suite:

python manage.py test


The project includes tests for key application flows, including:

- Core page routing
- AI Advisory form flow
- Optional farm data handling
- Weather error handling
- Crop Diagnosis flow
- Symptom-only diagnosis
- Multipart image upload handling
- Mocked AI response flows

Live Gemini requests are intentionally not repeatedly used during automated testing to conserve API quota.

--------------------------------------------------

IMPORTANT NOTES

EXTERNAL API AVAILABILITY

AgriSetu AI relies on external services, including Open-Meteo and Google Gemini.

Response availability can occasionally be affected by:

- Network issues
- API timeouts
- Free-tier quota limits
- Temporary model overload

The application is designed to handle such failures gracefully and provide user-friendly feedback instead of exposing server errors.

--------------------------------------------------

AGRICULTURAL GUIDANCE DISCLAIMER

AgriSetu AI provides AI-assisted agricultural guidance for informational and decision-support purposes.

Its recommendations should not replace:

- Laboratory soil testing
- Physical crop inspection
- Local agricultural extension services
- Professional agronomist advice
- Official pesticide or fungicide instructions
- Local agricultural regulations

Farmers should seek local expert verification when symptoms, soil conditions or environmental risks are uncertain.

--------------------------------------------------

PROJECT PHILOSOPHY

This project was built under hackathon constraints with a focus on solving the most important parts of the problem statement through a working MVP.

Working > Fancy
Focused > Huge
Tested > Many Incomplete Features

Instead of building a large generic agriculture platform, AgriSetu AI focuses on a practical farmer journey:

Farm Information
      +
Real Weather Context
      +
AI Intelligence
      |
      v
Practical Localised Advisory

combined with:

Crop Symptoms
      +
Optional Image
      |
      v
Possible AI-Assisted Diagnosis

and a broader cooperation model:

Local Sovereignty
      +
Interoperable Standards
      +
Anonymised Shared Insights
      |
      v
BRICS Agricultural Cooperation

--------------------------------------------------

HACKATHON

Hack2Skill — Build with AI: Code for Communities (C4C)

Track 4

AgriN & Regenerative Agricultural Intelligence

Theme

BRICS Cooperation

--------------------------------------------------

TEAM

[ADD YOUR TEAM NAME]

--------------------------------------------------

AgriSetu AI

Connecting local agricultural intelligence with AI, climate resilience and BRICS cooperation.