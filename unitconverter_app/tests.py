from django.test import TestCase, Client
from django.urls import reverse
from .logic.converter import convert


# Create your tests here.
"""
tests.py — Production-grade test suite for the Unit Converter Django app.

Covers:
  - View layer (HTTP status, template routing, context values)
  - Conversion logic (unit correctness, precision, edge cases)
  - Input validation / error handling
  - Cross-category mismatch guard

Run with:
    python manage.py test unitconverter_app
"""


# import pytest


# ---------------------------------------------------------------------------
# Helpers / Shared Constants
# ---------------------------------------------------------------------------

RESULT_URL = "unitconverter:result"
INDEX_URL = "unitconverter:index"
RESULT_TEMPLATE = "unitconverter_app/result.html"
INDEX_TEMPLATE = "unitconverter_app/index.html"


# ---------------------------------------------------------------------------
# View Tests
# ---------------------------------------------------------------------------


class IndexViewTests(TestCase):
    """Smoke tests for the landing page."""

    def setUp(self):
        self.client = Client()

    def test_returns_200(self):
        """Index page must return HTTP 200."""
        response = self.client.get(reverse(INDEX_URL))
        self.assertEqual(response.status_code, 200)

    def test_uses_correct_template(self):
        """Index page must render the correct template."""
        response = self.client.get(reverse(INDEX_URL))
        self.assertTemplateUsed(response, INDEX_TEMPLATE)


class ResultViewTests(TestCase):
    """Tests for the result view — routing, context injection, and error handling."""

    def setUp(self):
        self.client = Client()

    # ------------------------------------------------------------------
    # Happy-path routing
    # ------------------------------------------------------------------

    def test_returns_200(self):
        """Result view must return HTTP 200 for a valid conversion request."""
        response = self.client.get(
            reverse(RESULT_URL),
            {
                "input-num": 1000,
                "convert-from": "m",
                "convert-to": "km",
                "conversion-type": "length",
            },
        )
        self.assertEqual(response.status_code, 200)

    def test_uses_correct_template(self):
        """Result view must render the correct template."""
        response = self.client.get(
            reverse(RESULT_URL),
            {
                "input-num": 1000,
                "convert-from": "m",
                "convert-to": "km",
                "conversion-type": "length",
            },
        )
        self.assertTemplateUsed(response, RESULT_TEMPLATE)

    # ------------------------------------------------------------------
    # Context values — one representative case per category
    # ------------------------------------------------------------------

    def test_context_length(self):
        """Result context must contain the correct converted value for length."""
        response = self.client.get(
            reverse(RESULT_URL),
            {
                "input-num": 1000,
                "convert-from": "m",
                "convert-to": "km",
                "conversion-type": "length",
            },
        )
        self.assertAlmostEqual(response.context["converted_value"], 1.0)

    def test_context_temperature(self):
        """Result context must contain the correct converted value for temperature."""
        response = self.client.get(
            reverse(RESULT_URL),
            {
                "input-num": 0,
                "convert-from": "c",
                "convert-to": "k",
                "conversion-type": "temperature",
            },
        )
        self.assertAlmostEqual(response.context["converted_value"], 273.15)

    def test_context_weight(self):
        """Result context must contain the correct converted value for weight."""
        response = self.client.get(
            reverse(RESULT_URL),
            {
                "input-num": 1,
                "convert-from": "lb",
                "convert-to": "kg",
                "conversion-type": "weight",
            },
        )
        self.assertAlmostEqual(response.context["converted_value"], 0.4536, places=4)

    def test_context_time(self):
        """Result context must contain the correct converted value for time."""
        response = self.client.get(
            reverse(RESULT_URL),
            {
                "input-num": 3600,
                "convert-from": "s",
                "convert-to": "hr",
                "conversion-type": "time",
            },
        )
        self.assertAlmostEqual(response.context["converted_value"], 1.0)

    def test_context_speed(self):
        """Result context must contain the correct converted value for speed."""
        response = self.client.get(
            reverse(RESULT_URL),
            {
                "input-num": 1,
                "convert-from": "mps",
                "convert-to": "mph",
                "conversion-type": "speed",
            },
        )
        self.assertAlmostEqual(response.context["converted_value"], 2.237, places=2)

    # ------------------------------------------------------------------
    # Edge-case / validation guard
    # ------------------------------------------------------------------

    def test_identity_conversion(self):
        """Converting a unit to itself must return the original value unchanged."""
        response = self.client.get(
            reverse(RESULT_URL),
            {
                "input-num": 42,
                "convert-from": "m",
                "convert-to": "m",
                "conversion-type": "length",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertAlmostEqual(response.context["converted_value"], 42.0)

    def test_zero_input(self):
        """Zero input must produce zero output for linear (non-temperature) conversions."""
        response = self.client.get(
            reverse(RESULT_URL),
            {
                "input-num": 0,
                "convert-from": "km",
                "convert-to": "m",
                "conversion-type": "length",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertAlmostEqual(response.context["converted_value"], 0.0)

    def test_negative_input_length(self):
        """Negative numeric input must be handled without error for length conversions."""
        response = self.client.get(
            reverse(RESULT_URL),
            {
                "input-num": -5,
                "convert-from": "km",
                "convert-to": "m",
                "conversion-type": "length",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertAlmostEqual(response.context["converted_value"], -5000.0)

    def test_missing_input_num_returns_400(self):
        """Omitting the required input-num parameter must return HTTP 400."""
        response = self.client.get(
            reverse(RESULT_URL),
            {"convert-from": "m", "convert-to": "km", "conversion-type": "length"},
        )
        self.assertEqual(response.status_code, 400)

    def test_non_numeric_input_returns_400(self):
        """Non-numeric input-num must return HTTP 400."""
        response = self.client.get(
            reverse(RESULT_URL),
            {
                "input-num": "abc",
                "convert-from": "m",
                "convert-to": "km",
                "conversion-type": "length",
            },
        )
        self.assertEqual(response.status_code, 400)


# ---------------------------------------------------------------------------
# Converter Logic — Length
# ---------------------------------------------------------------------------


class LengthConversionTests(TestCase):
    """Unit tests for length conversions via the convert() function."""

    # Metric
    def test_m_to_km(self):
        result, _ = convert("m", "km", 1000, "length")
        self.assertEqual(result, 1.0)

    def test_km_to_m(self):
        result, _ = convert("km", "m", 1, "length")
        self.assertEqual(result, 1000.0)

    def test_m_to_cm(self):
        result, _ = convert("m", "cm", 1, "length")
        self.assertEqual(result, 100.0)

    def test_cm_to_m(self):
        result, _ = convert("cm", "m", 100, "length")
        self.assertEqual(result, 1.0)

    def test_km_to_cm(self):
        result, _ = convert("km", "cm", 1, "length")
        self.assertEqual(result, 100_000.0)

    def test_cm_to_km(self):
        result, _ = convert("cm", "km", 100_000, "length")
        self.assertEqual(result, 1.0)

    # Imperial
    def test_m_to_inch(self):
        result, _ = convert("m", "inch", 1, "length")
        self.assertAlmostEqual(result, 39.37, places=2)

    def test_inch_to_m(self):
        result, _ = convert("inch", "m", 39.37, "length")
        self.assertAlmostEqual(result, 1.0, places=2)

    def test_m_to_feet(self):
        result, _ = convert("m", "feet", 1, "length")
        self.assertAlmostEqual(result, 3.281, places=2)

    def test_feet_to_m(self):
        result, _ = convert("feet", "m", 3.281, "length")
        self.assertAlmostEqual(result, 1.0, places=2)

    def test_inch_to_feet(self):
        result, _ = convert("inch", "feet", 12, "length")
        self.assertAlmostEqual(result, 1.0, places=2)

    def test_feet_to_inch(self):
        result, _ = convert("feet", "inch", 1, "length")
        self.assertAlmostEqual(result, 12.0, places=1)

    # Edge cases
    def test_zero_length(self):
        """Zero metres must stay zero across any linear conversion."""
        result, _ = convert("m", "km", 0, "length")
        self.assertEqual(result, 0.0)

    def test_large_value(self):
        """Large values must convert without overflow or precision loss."""
        result, _ = convert("km", "m", 1_000_000, "length")
        self.assertEqual(result, 1_000_000_000.0)


# ---------------------------------------------------------------------------
# Converter Logic — Temperature
# ---------------------------------------------------------------------------


class TemperatureConversionTests(TestCase):
    """Unit tests for temperature conversions.

    Temperature uses non-linear (affine) transforms, so all results
    are validated with assertAlmostEqual.
    """

    def test_c_to_f_boiling(self):
        result, _ = convert("c", "f", 100, "temperature")
        self.assertAlmostEqual(result, 212.0, places=2)

    def test_f_to_c_boiling(self):
        result, _ = convert("f", "c", 212, "temperature")
        self.assertAlmostEqual(result, 100.0, places=2)

    def test_c_to_k_freezing(self):
        result, _ = convert("c", "k", 0, "temperature")
        self.assertAlmostEqual(result, 273.15, places=2)

    def test_k_to_c_freezing(self):
        result, _ = convert("k", "c", 273.15, "temperature")
        self.assertAlmostEqual(result, 0.0, places=2)

    def test_f_to_k_freezing(self):
        result, _ = convert("f", "k", 32, "temperature")
        self.assertAlmostEqual(result, 273.15, places=2)

    def test_k_to_f_freezing(self):
        result, _ = convert("k", "f", 273.15, "temperature")
        self.assertAlmostEqual(result, 32.0, places=2)

    def test_c_to_f_absolute_zero(self):
        """Absolute zero in Celsius must map to −459.67 °F."""
        result, _ = convert("c", "f", -273.15, "temperature")
        self.assertAlmostEqual(result, -459.67, places=1)

    def test_c_to_f_body_temperature(self):
        """37 °C (body temp) must convert to 98.6 °F."""
        result, _ = convert("c", "f", 37, "temperature")
        self.assertAlmostEqual(result, 98.6, places=1)

    def test_round_trip_c_to_f_to_c(self):
        """Converting C→F→C must return the original value (round-trip)."""
        original = 25.0
        f, _ = convert("c", "f", original, "temperature")
        result, _ = convert("f", "c", f, "temperature")
        self.assertAlmostEqual(result, original, places=4)


# ---------------------------------------------------------------------------
# Converter Logic — Weight
# ---------------------------------------------------------------------------


class WeightConversionTests(TestCase):
    """Unit tests for weight/mass conversions."""

    # Metric
    def test_kg_to_g(self):
        result, _ = convert("kg", "g", 1, "weight")
        self.assertEqual(result, 1000)

    def test_g_to_kg(self):
        result, _ = convert("g", "kg", 1000, "weight")
        self.assertEqual(result, 1)

    def test_g_to_mg(self):
        result, _ = convert("g", "mg", 1, "weight")
        self.assertEqual(result, 1000)

    def test_mg_to_g(self):
        result, _ = convert("mg", "g", 1000, "weight")
        self.assertEqual(result, 1)

    def test_kg_to_mg(self):
        result, _ = convert("kg", "mg", 1, "weight")
        self.assertEqual(result, 1_000_000)

    # Imperial / mixed
    def test_lb_to_g(self):
        result, _ = convert("lb", "g", 1, "weight")
        self.assertAlmostEqual(result, 453.592, places=2)

    def test_g_to_lb(self):
        result, _ = convert("g", "lb", 453.592, "weight")
        self.assertAlmostEqual(result, 1.0, places=3)

    def test_lb_to_kg(self):
        result, _ = convert("lb", "kg", 1, "weight")
        self.assertAlmostEqual(result, 0.453592, places=4)

    def test_kg_to_lb(self):
        result, _ = convert("kg", "lb", 1, "weight")
        self.assertAlmostEqual(result, 2.20462, places=4)

    def test_oz_to_g(self):
        result, _ = convert("oz", "g", 1, "weight")
        self.assertAlmostEqual(result, 28.3495, places=3)

    def test_g_to_oz(self):
        result, _ = convert("g", "oz", 28.3495, "weight")
        self.assertAlmostEqual(result, 1.0, places=3)

    def test_lb_to_oz(self):
        result, _ = convert("lb", "oz", 1, "weight")
        self.assertEqual(result, 16)

    def test_oz_to_lb(self):
        result, _ = convert("oz", "lb", 16, "weight")
        self.assertEqual(result, 1)

    # Edge cases
    def test_zero_weight(self):
        result, _ = convert("kg", "g", 0, "weight")
        self.assertEqual(result, 0)

    def test_fractional_weight(self):
        """Sub-milligram values must not be lost to rounding."""
        result, _ = convert("mg", "g", 0.5, "weight")
        self.assertAlmostEqual(result, 0.0005, places=6)


# ---------------------------------------------------------------------------
# Converter Logic — Time
# ---------------------------------------------------------------------------


class TimeConversionTests(TestCase):
    """Unit tests for time conversions."""

    def test_s_to_min(self):
        result, _ = convert("s", "min", 60, "time")
        self.assertEqual(result, 1)

    def test_min_to_s(self):
        result, _ = convert("min", "s", 1, "time")
        self.assertEqual(result, 60)

    def test_min_to_hr(self):
        result, _ = convert("min", "hr", 60, "time")
        self.assertEqual(result, 1)

    def test_hr_to_min(self):
        result, _ = convert("hr", "min", 1, "time")
        self.assertEqual(result, 60)

    def test_hr_to_s(self):
        result, _ = convert("hr", "s", 1, "time")
        self.assertEqual(result, 3600)

    def test_s_to_hr(self):
        result, _ = convert("s", "hr", 3600, "time")
        self.assertEqual(result, 1)

    def test_day_to_hr(self):
        result, _ = convert("day", "hr", 1, "time")
        self.assertEqual(result, 24)

    def test_hr_to_day(self):
        result, _ = convert("hr", "day", 24, "time")
        self.assertEqual(result, 1)

    def test_day_to_s(self):
        result, _ = convert("day", "s", 1, "time")
        self.assertEqual(result, 86400)

    def test_s_to_day(self):
        result, _ = convert("s", "day", 86400, "time")
        self.assertEqual(result, 1)

    # Edge cases
    def test_zero_seconds(self):
        result, _ = convert("s", "hr", 0, "time")
        self.assertEqual(result, 0)

    def test_large_time_span(self):
        """One year in seconds should equal 365 * 86400."""
        one_year_s = 365 * 86400
        result, _ = convert("s", "day", one_year_s, "time")
        self.assertAlmostEqual(result, 365.0, places=2)


# ---------------------------------------------------------------------------
# Converter Logic — Speed
# ---------------------------------------------------------------------------


class SpeedConversionTests(TestCase):
    """Unit tests for speed conversions."""

    def test_mps_to_kmph(self):
        result, _ = convert("mps", "kmph", 1, "speed")
        self.assertAlmostEqual(result, 3.6, places=3)

    def test_kmph_to_mps(self):
        result, _ = convert("kmph", "mps", 3.6, "speed")
        self.assertAlmostEqual(result, 1.0, places=3)

    def test_mps_to_mph(self):
        result, _ = convert("mps", "mph", 1, "speed")
        self.assertAlmostEqual(result, 2.23694, places=3)

    def test_mph_to_mps(self):
        result, _ = convert("mph", "mps", 2.23694, "speed")
        self.assertAlmostEqual(result, 1.0, places=3)

    def test_kmph_to_mph(self):
        result, _ = convert("kmph", "mph", 1, "speed")
        self.assertAlmostEqual(result, 0.621371, places=4)

    def test_mph_to_kmph(self):
        result, _ = convert("mph", "kmph", 1, "speed")
        self.assertAlmostEqual(result, 1.60934, places=4)

    def test_mps_to_knots(self):
        result, _ = convert("mps", "knots", 1, "speed")
        self.assertAlmostEqual(result, 1.94384, places=3)

    def test_knots_to_mps(self):
        result, _ = convert("knots", "mps", 1.94384, "speed")
        self.assertAlmostEqual(result, 1.0, places=3)

    def test_mps_to_mach(self):
        """343 m/s (speed of sound at sea level) must equal exactly 1 Mach."""
        result, _ = convert("mps", "mach", 343, "speed")
        self.assertAlmostEqual(result, 1.0, places=4)

    def test_mach_to_mps(self):
        result, _ = convert("mach", "mps", 1, "speed")
        self.assertAlmostEqual(result, 343.0, places=2)

    # Edge cases
    def test_zero_speed(self):
        result, _ = convert("mps", "kmph", 0, "speed")
        self.assertEqual(result, 0)

    def test_round_trip_mps_kmph(self):
        """mps → kmph → mps round-trip must preserve the original value."""
        original = 27.78
        kmph, _ = convert("mps", "kmph", original, "speed")
        result, _ = convert("kmph", "mps", kmph, "speed")
        self.assertAlmostEqual(result, original, places=2)


# ---------------------------------------------------------------------------
# Cross-Category Mismatch Guard
# ---------------------------------------------------------------------------


class CrossCategoryConversionTests(TestCase):
    """Ensure the converter raises an error for incompatible unit pairs."""

    def test_length_to_weight_raises(self):
        """Converting length to weight must raise TypeError."""
        with self.assertRaises(TypeError):
            convert("m", "kg", 1, "length")

    def test_weight_to_length_raises(self):
        """Converting weight to length must raise TypeError."""
        with self.assertRaises(TypeError):
            convert("kg", "m", 1, "weight")

    def test_length_to_temperature_raises(self):
        """Converting length to temperature must raise TypeError."""
        with self.assertRaises(TypeError):
            convert("m", "c", 1, "length")

    def test_temperature_to_length_raises(self):
        """Converting temperature to length must raise TypeError."""
        with self.assertRaises(TypeError):
            convert("c", "m", 1, "temperature")

    def test_length_to_time_raises(self):
        """Converting length to time must raise TypeError."""
        with self.assertRaises(TypeError):
            convert("m", "s", 1, "length")

    def test_time_to_length_raises(self):
        """Converting time to length must raise TypeError."""
        with self.assertRaises(TypeError):
            convert("s", "km", 60, "time")

    def test_length_to_speed_raises(self):
        """Converting length to speed must raise TypeError."""
        with self.assertRaises(TypeError):
            convert("km", "kmph", 60, "length")

    def test_speed_to_length_raises(self):
        """Converting speed to length must raise TypeError."""
        with self.assertRaises(TypeError):
            convert("kmph", "km", 60, "speed")

    def test_temperature_to_weight_raises(self):
        """Converting temperature to weight must raise TypeError."""
        with self.assertRaises(TypeError):
            convert("c", "kg", 1, "temperature")

    def test_weigth_to_temperature_raises(self):
        """Converting weight to temperature must raise TypeError."""
        with self.assertRaises(TypeError):
            convert("kg", "c", 1, "weight")

    def test_temperature_to_time_raises(self):
        """Converting temperature to time must raise TypeError."""
        with self.assertRaises(TypeError):
            convert("k", "day", 273.15, "temperature")

    def test_time_to_temperature_raises(self):
        """Converting time to temperature must raise TypeError."""
        with self.assertRaises(TypeError):
            convert("day", "k", 365, "time")

    def test_temperature_to_speed_raises(self):
        """Converting temperature to speed must raise TypeError."""
        with self.assertRaises(TypeError):
            convert("c", "mps", 100, "temperature")

    def test_speed_to_temperature_raises(self):
        """Converting speed to temperature must raise TypeError."""
        with self.assertRaises(TypeError):
            convert("mach", "f", 1, "speed")

    def test_weight_to_time_raises(self):
        """Converting weight to time must raise TypeError."""
        with self.assertRaises(TypeError):
            convert("kg", "min", 1000, "weight")

    def test_time_to_weight_raises(self):
        """Converting time to weight must raise TypeError."""
        with self.assertRaises(TypeError):
            convert("min", "kg", 1, "time")

    def test_weight_to_speed_raises(self):
        """Converting weight to speed must raise TypeError."""
        with self.assertRaises(TypeError):
            convert("kg", "knots", 1000, "weight")

    def test_speed_to_weight_raises(self):
        """Converting speed to weight must raise TypeError."""
        with self.assertRaises(TypeError):
            convert("knots", "kg", 1, "speed")

    def test_time_to_speed_raises(self):
        """Converting time to speed must raise TypeError."""
        with self.assertRaises(TypeError):
            convert("hr", "kmph", 1, "time")

    def test_speed_to_time_raises(self):
        """Converting speed to time must raise TypeError."""
        with self.assertRaises(TypeError):
            convert("kmph", "hr", 1, "speed")

    def test_unknown_unit_raises(self):
        """An unrecognised unit symbol must raise TypeError."""
        with self.assertRaises(TypeError):
            convert("parsec", "km", 1, "time")
