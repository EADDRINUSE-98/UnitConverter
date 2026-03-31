from django.test import TestCase, Client
from django.urls import reverse
from .logic.converter import convert


# Create your tests here.
class ConversionAppTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_page(self):
        response = self.client.get(
            reverse("unitconverter:index")
        )  # reverse("named-url", kwargs={}, args=[])
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "unitconverter_app/index.html")

    def test_result_page(self):
        response = self.client.get(
            reverse("unitconverter:result"),
            {"input-num": 1000, "convert-from": "m", "convert-to": "km"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "unitconverter_app/result.html")

    def test_length_conversion_form_submission(self):
        response = self.client.get(
            reverse("unitconverter:result"),
            {"input-num": 1000, "convert-from": "m", "convert-to": "km"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "unitconverter_app/result.html")
        self.assertAlmostEqual(response.context["converted_value"], 1)

    def test_temperature_conversion_form_submission(self):
        response = self.client.get(
            reverse("unitconverter:result"),
            {"input-num": 0, "convert-from": "c", "convert-to": "k"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "unitconverter_app/result.html")
        self.assertEqual(response.context["converted_value"], 273.15)

    def test_weight_conversion_form_submission(self):
        response = self.client.get(
            reverse("unitconverter:result"),
            {"input-num": 1, "convert-from": "lb", "convert-to": "kg"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "unitconverter_app/result.html")
        self.assertEqual(response.context["converted_value"], 0.4536)


class LengthConversionTests(TestCase):
    def test_m_to_km(self):
        result, _ = convert("m", "km", 1000)
        self.assertEqual(result, 1)

    def test_km_to_m(self):
        result, _ = convert("km", "m", 1)
        self.assertEqual(result, 1000)

    def test_m_to_cm(self):
        result, _ = convert("m", "cm", 1)
        self.assertEqual(result, 100)

    def test_cm_to_m(self):
        result, _ = convert("cm", "m", 100)
        self.assertEqual(result, 1)

    def test_m_to_inches(self):
        result, _ = convert("m", "inch", 1)
        self.assertAlmostEqual(result, 39.37, places=2)

    def test_inches_to_m(self):
        result, _ = convert("inch", "m", 39.37)
        self.assertAlmostEqual(result, 1, places=2)

    def test_m_to_feet(self):
        result, _ = convert("m", "feet", 1)
        self.assertAlmostEqual(result, 3.28084, places=2)

    def test_feet_to_m(self):
        result, _ = convert("feet", "m", 3.28084)
        self.assertAlmostEqual(result, 1, places=2)


class TemperatureConversionTests(TestCase):
    def test_c_to_f(self):
        result, _ = convert("c", "f", 100)
        self.assertAlmostEqual(result, 212, places=2)

    def test_f_to_c(self):
        result, _ = convert("f", "c", 212)
        self.assertAlmostEqual(result, 100, places=2)

    def test_c_to_k(self):
        result, _ = convert("c", "k", 0)
        self.assertAlmostEqual(result, 273.15, places=2)

    def test_k_to_c(self):
        result, _ = convert("k", "c", 273.15)
        self.assertAlmostEqual(result, 0, places=2)

    def test_f_to_k(self):
        result, _ = convert("f", "k", 32)
        self.assertAlmostEqual(result, 273.15, places=2)

    def test_k_to_f(self):
        result, _ = convert("k", "f", 273.15)
        self.assertAlmostEqual(result, 32, places=2)


class WeightConversionTests(TestCase):
    def test_kg_to_g(self):
        result, _ = convert("kg", "g", 1)
        self.assertEqual(result, 1000)

    def test_g_to_kg(self):
        result, _ = convert("g", "kg", 1000)
        self.assertEqual(result, 1)

    def test_g_to_mg(self):
        result, _ = convert("g", "mg", 1)
        self.assertEqual(result, 1000)

    def test_mg_to_g(self):
        result, _ = convert("mg", "g", 1000)
        self.assertEqual(result, 1)

    def test_kg_to_mg(self):
        result, _ = convert("kg", "mg", 1)
        self.assertEqual(result, 1_000_000)

    def test_lb_to_g(self):
        result, _ = convert("lb", "g", 1)
        self.assertAlmostEqual(result, 453.592, places=4)

    def test_g_to_lb(self):
        result, _ = convert("g", "lb", 453.592)
        self.assertAlmostEqual(result, 1, places=4)

    def test_lb_to_kg(self):
        result, _ = convert("lb", "kg", 1)
        self.assertAlmostEqual(result, 0.453592, places=4)

    def test_kg_to_lb(self):
        result, _ = convert("kg", "lb", 1)
        self.assertAlmostEqual(result, 2.20462, places=4)

    def test_oz_to_g(self):
        result, _ = convert("oz", "g", 1)
        self.assertAlmostEqual(result, 28.3495, places=4)

    def test_g_to_oz(self):
        result, _ = convert("g", "oz", 28.3495)
        self.assertAlmostEqual(result, 1, places=4)

    def test_lb_to_oz(self):
        result, _ = convert("lb", "oz", 1)
        self.assertEqual(result, 16)

    def test_oz_to_lb(self):
        result, _ = convert("oz", "lb", 16)
        self.assertEqual(result, 1)
