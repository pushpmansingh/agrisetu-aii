from django.shortcuts import render
from .services.weather import get_weather
from .services.ai import generate_advisory , generate_diagnosis


# Create your views here.

def home(request):
    return render(request, "core/home.html")


def advisory(request):

    if request.method == "POST":

        country = request.POST.get("country")
        location = request.POST.get("location")
        crop = request.POST.get("crop")
        crop_stage = request.POST.get("crop_stage")
        soil_type = request.POST.get("soil_type")
        soil_ph = request.POST.get("soil_ph")
        organic_matter = request.POST.get("organic_matter")
        farm_size = request.POST.get("farm_size")
        farm_unit = request.POST.get("farm_unit")

        farm_data = {
            "country": country,
            "location": location,
            "crop": crop,
            "crop_stage": crop_stage,
            "soil_type": soil_type,
            "soil_ph": soil_ph,
            "organic_matter": organic_matter,
            "farm_size": farm_size,
            "farm_unit": farm_unit,
        }

        weather_data = get_weather(location, country)
        advisory_data = None
        ai_error = None

        if weather_data.get("error"):
             ai_error = weather_data["error"]
        else:             
            try:
                advisory_data = generate_advisory(
                    farm_data,
                    weather_data
                )

            except Exception as error:
                print("Gemini Error:", error)
                ai_error = (
                    "We could not generate the AI advisory right now. "
                    "Please try again."
                )

        return render(
            request,
            "core/advisory.html",
            {
                "farm_data": farm_data,
                "weather_data": weather_data,
                "advisory_data": advisory_data,
                "ai_error": ai_error,
            }
        )

    return render(
    request,
    "core/advisory.html",
    {
        "advisory_data": None,
        "ai_error": None,
    }
)

def diagnosis(request):

    if request.method == "POST":

        crop = request.POST.get("crop")
        crop_stage = request.POST.get("crop_stage")
        symptoms = request.POST.get("symptoms")
        crop_image = request.FILES.get("crop_image")
        crop_data = {
            "crop": crop,
            "crop_stage": crop_stage or "Not provided",
            "symptoms": symptoms,
        }

        diagnosis_data = None
        diagnosis_error = None

        try:

            diagnosis_data = generate_diagnosis(crop_data,crop_image)

        except Exception as error:

            print("Gemini Diagnosis Error:", error)

            diagnosis_error = (
                "AgriSetu AI could not analyze the crop right now. "
                "Please try again."
            )

        return render(
            request,
            "core/diagnosis.html",
            {
                "diagnosis_data": diagnosis_data,
                "diagnosis_error": diagnosis_error,
            }
        )

    return render(
        request,
        "core/diagnosis.html",
        {
            "diagnosis_data": None,
            "diagnosis_error": None,
        }
    )

def brics_hub(request):
    return render(request, "core/brics_hub.html")