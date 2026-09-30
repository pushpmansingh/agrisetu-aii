import json

import os

from google import genai


def _clean_json_response(text):
    text = (text or "").strip()
    if text.startswith("```"):
        lines = text.splitlines()
        if lines and lines[0].startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].startswith("```"):
            lines = lines[:-1]
        text = "\n".join(lines).strip()
    return json.loads(text)


def generate_advisory(farm_data, weather_data):

    client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

    prompt = f"""
You are AgriSetu AI, an agricultural intelligence assistant designed for small
and marginal farmers across BRICS nations.

Generate a practical, localized and climate-resilient agricultural advisory.

IMPORTANT RULES:
- Use the farmer data and real weather data provided below.
- Do not invent exact soil test results or claim certainty where data is missing.
- If soil information is unknown, clearly mention that recommendations are based
  on limited soil information.
- Give practical advice understandable by a farmer.
- Prioritize regenerative and sustainable practices where appropriate.
- Do not recommend excessive or dangerous chemical use.
- Mention uncertainty when disease, weather or soil conditions require local
  expert verification.
- The 7-day action plan should be specific and practical.

FARM DATA:
{json.dumps(farm_data, indent=2)}

WEATHER DATA:
{json.dumps(weather_data, indent=2)}

Return ONLY valid JSON.
Do not use markdown.
Do not add ```json.

Use exactly this structure:

{{
    "climate_summary": {{
        "summary": "",
        "key_conditions": []
    }},
    "soil_health_assessment": {{
        "assessment": "",
        "recommendations": []
    }},
    "crop_farming_recommendation": {{
        "recommendation": "",
        "actions": []
    }},
    "regenerative_practices": [],
    "water_management": {{
        "recommendation": "",
        "actions": []
    }},
    "risk_alerts": [
        {{
            "risk": "",
            "severity": "",
            "action": ""
        }}
    ],
    "next_7_day_action_plan": [
        {{
            "day": "Day 1",
            "action": ""
        }}
    ]
}}
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )

    return _clean_json_response(response.text)


def generate_diagnosis(crop_data, crop_image=None):

    client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

    prompt = f"""
You are AgriSetu AI, an agricultural crop health assistant for small and
marginal farmers across BRICS nations.

Analyze the crop symptoms provided by the farmer and, if an image is provided,
also analyze the visible crop or leaf conditions.

Give a careful, practical POSSIBLE diagnosis.

IMPORTANT RULES:

- Do not claim absolute certainty.
- Use both the farmer's description and the image when an image is available.
- If the image is unclear, low quality, or does not clearly show the affected
  crop area, say that visual confidence is limited.
- Base the diagnosis only on the symptoms, crop information, and visible image
  evidence provided.
- Clearly state when visual inspection or a local agricultural expert is needed.
- Do not invent facts.
- Prioritize low-risk, sustainable and regenerative approaches.
- Avoid recommending excessive chemical pesticide or fungicide use.
- If chemical treatment may be necessary, recommend following local agricultural
  guidance and product labels rather than giving unsafe application instructions.
- Keep the advice understandable and practical for a farmer.
- The farmer may describe the crop and symptoms in English, Hindi, Hinglish,
  Roman Hindi, or simple informal language.
- Understand common crop names such as "tamatar" as tomato where the meaning
  is reasonably clear.
- Interpret informal symptom descriptions carefully, but do not pretend to be
  certain when the description is ambiguous.
- If the symptoms could indicate multiple problems, identify the most likely
  possibility and mention uncertainty where appropriate.

CROP DATA:

{json.dumps(crop_data, indent=2)}

Return ONLY valid JSON.

Do not use markdown.
Do not add ```json.

Use exactly this structure:

{{
    "possible_problem": "",
    "confidence_level": "",
    "severity": "",
    "likely_causes": [],
    "immediate_actions": [],
    "sustainable_treatment": [],
    "prevention_advice": [],
    "expert_note": ""
}}
"""

    # If no image was uploaded, use symptom-based diagnosis
    if not crop_image:

        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=prompt
        )

    # If an image was uploaded, send both text + image
    else:

        image_bytes = crop_image.read()

        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=[
                prompt,
                {
                    "inline_data": {
                        "mime_type": crop_image.content_type,
                        "data": image_bytes
                    }
                }
            ]
        )

    return _clean_json_response(response.text)


