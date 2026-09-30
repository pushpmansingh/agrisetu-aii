from unittest.mock import patch
from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

class PageRenderingTests(TestCase):
    def test_home_page_renders(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'AgriSetu AI')
        self.assertContains(response, 'preconnect')

    def test_advisory_page_clean_get(self):
        response = self.client.get(reverse('advisory'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'advisory-form')
        self.assertNotContains(response, 'AGRISETU AI RECOMMENDATION')

    def test_diagnosis_page_clean_get(self):
        response = self.client.get(reverse('diagnosis'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'diagnosis-form')
        self.assertNotContains(response, 'POSSIBLE PROBLEM')

    def test_brics_hub_page_renders(self):
        response = self.client.get(reverse('brics_hub'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'BRICS AGRIN COOPERATION NETWORK')

class FormAndAPIHandlingTests(TestCase):

    @patch('core.views.get_weather')
    @patch('core.views.generate_advisory')
    def test_advisory_post_success(self, mock_ai, mock_weather):
        mock_weather.return_value = {
            "location": "Lucknow",
            "country": "India",
            "current": {"temperature_2m": 30},
            "daily": {}
        }
        mock_ai.return_value = {
            "climate_summary": {"summary": "Warm climate", "key_conditions": ["Sun"]},
            "soil_health_assessment": {"assessment": "Good soil", "recommendations": ["Mulch"]},
            "crop_farming_recommendation": {"recommendation": "Irrigate regularly", "actions": []},
            "regenerative_practices": ["Composting"],
            "water_management": {"recommendation": "Drip irrigation", "actions": []},
            "risk_alerts": [],
            "next_7_day_action_plan": [{"day": "Day 1", "action": "Water crops"}]
        }

        response = self.client.post(reverse('advisory'), {
            'country': 'India',
            'location': 'Lucknow',
            'crop': 'Wheat',
            'crop_stage': 'Seedling',
            'soil_type': 'Loamy',
            'soil_ph': '',
            'organic_matter': '',
            'farm_size': '',
            'farm_unit': '',
        })

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'AGRISETU AI RECOMMENDATION')
        self.assertContains(response, 'Warm climate')

    @patch('core.views.get_weather')
    def test_advisory_weather_error(self, mock_weather):
        mock_weather.return_value = {"error": "Location not found. Please enter a more specific city or district."}

        response = self.client.post(reverse('advisory'), {
            'country': 'India',
            'location': 'InvalidCityName123',
            'crop': 'Wheat',
            'crop_stage': 'Seedling',
            'soil_type': 'Loamy',
        })

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Location not found')

    @patch('core.views.generate_diagnosis')
    def test_diagnosis_symptoms_only_success(self, mock_ai):
        mock_ai.return_value = {
            "possible_problem": "Leaf Spot",
            "confidence_level": "Medium",
            "severity": "Moderate",
            "likely_causes": ["Fungal infection"],
            "immediate_actions": ["Prune infected leaves"],
            "sustainable_treatment": ["Neem oil spray"],
            "prevention_advice": ["Improve ventilation"],
            "expert_note": "Consult local agri clinic if spreading."
        }

        response = self.client.post(reverse('diagnosis'), {
            'crop': 'Tomato',
            'crop_stage': 'Vegetative',
            'symptoms': 'Small brown spots on leaves',
        })

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Leaf Spot')

    @patch('core.views.generate_diagnosis')
    def test_diagnosis_with_image_upload(self, mock_ai):
        mock_ai.return_value = {
            "possible_problem": "Early Blight",
            "confidence_level": "High",
            "severity": "High",
            "likely_causes": ["Alternaria solani"],
            "immediate_actions": ["Remove lower leaves"],
            "sustainable_treatment": ["Copper fungicide"],
            "prevention_advice": ["Crop rotation"],
            "expert_note": "Monitor field closely."
        }

        test_image = SimpleUploadedFile(
            "leaf.jpg",
            b"\xFF\xD8\xFF\xE0\x00\x10JFIF\x00\x01\x01\x01\x00\x60\x00\x60\x00\x00\xFF\xD9",
            content_type="image/jpeg"
        )

        response = self.client.post(reverse('diagnosis'), {
            'crop': 'Tomato',
            'crop_stage': 'Fruiting',
            'symptoms': 'Target-shaped lesions on foliage',
            'crop_image': test_image,
        })

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Early Blight')
