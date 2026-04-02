"""
from_unit -> base_unit
base_unit -> to_unit

length base unit: meters
temperature base unit: kelvin
weight base unit: gram
speed base unit: mps
time base unit: second
"""

"""
'from_unit' to 'base_unit' conversion function definition section.
"""


# For Length
def __meter_to_base(input_num):
    return input_num, [f"= {input_num}m"]


def __kilometer_to_base(input_num):
    return input_num * 1000, [f"= {input_num}km", f"= ({input_num} * 1000)m"]


def __centimeter_to_base(input_num):
    return input_num / 100, [f"= {input_num}cm", f"= ({input_num} / 100)m"]


def __inch_to_base(input_num):
    return input_num / 39.37, [f"= {input_num}inches", f"= ({input_num} / 39.37)m"]


def __feet_to_base(input_num):
    return input_num / 3.281, [f"= {input_num}feets", f"= ({input_num} / 3.281)m"]


"""
'base_unit' to 'to_unit' conversion function definition section.
"""


def __base_to_meter(value_in_base):
    return value_in_base, [f"= ({value_in_base} * 1)m"]


def __base_to_kilometer(value_in_base):
    return value_in_base / 1000, [
        f"= ({value_in_base} * 1)m",
        f"= ({value_in_base} / 1000)km",
    ]


def __base_to_centimeter(value_in_base):
    return value_in_base * 100, [
        f"= ({value_in_base} * 1)m",
        f"= ({value_in_base} * 100)cm",
    ]


def __base_to_inche(value_in_base):
    return value_in_base * 39.37, [
        f"= ({value_in_base} * 1)m",
        f"= ({value_in_base} * 39.37)inches",
    ]


def __base_to_feet(value_in_base):
    return value_in_base * 3.281, [
        f"= ({value_in_base} * 1)m",
        f"= ({value_in_base} * 3.281)feets",
    ]


# For Temperature


def __kelvin_to_base(input_num):
    return input_num, [f"= {input_num}°k"]


def __celsius_to_base(input_num):
    return input_num + 273.15, [f"= {input_num}°c", f"= ({input_num} + 273.15)°k"]


def __fahrenheit_to_base(input_num):
    return (input_num - 32) * (5 / 9) + 273.15, [
        f"= {input_num}°f",
        f"= (({input_num} - 32) * (5/9) + 273.15)°k",
    ]


def __base_to_kelvin(value_in_base):
    return value_in_base, [f"= ({value_in_base} * 1)°k"]


def __base_to_celsius(value_in_base):
    return value_in_base - 273.15, [
        f"= ({value_in_base} * 1)°k",
        f"= ({value_in_base} - 273.15)°c",
    ]


def __base_to_fahrenheit(value_in_base):
    return (value_in_base - 273.15) * (9 / 5) + 32, [
        f"= ({value_in_base} * 1)°k",
        f"= (({value_in_base} - 273.15) * (9/5) + 32)°f",
    ]


# For Weight


def __gram_to_base(input_num):
    return input_num, [f"= {input_num}g"]


def __kilogram_to_base(input_num):
    return input_num * 1000, [f"= {input_num}kg", f"= ({input_num} * 1000)g"]


def __miligram_to_base(input_num):
    return input_num / 1000, [f"= {input_num}mg", f"= ({input_num} / 1000)g"]


def __pound_to_base(input_num):
    return input_num * 453.592, [f"= {input_num}lb", f"= ({input_num} * 453.592)g"]


def __ounce_to_base(input_num):
    return input_num * 28.3495, [f"= {input_num}oz", f"= ({input_num} * 28.3495)g"]


def __base_to_gram(value_in_base):
    return value_in_base, [f"= ({value_in_base} * 1)g"]


def __base_to_kilogram(value_in_base):
    return value_in_base / 1000, [
        f"= ({value_in_base} * 1)g",
        f"= ({value_in_base} / 1000)kg",
    ]


def __base_to_miligram(value_in_base):
    return value_in_base * 1000, [
        f"= ({value_in_base} * 1)g",
        f"= ({value_in_base} * 1000)mg",
    ]


def __base_to_pound(value_in_base):
    return value_in_base / 453.592, [
        f"= ({value_in_base} * 1)g",
        f"= ({value_in_base} / 453.592)lb",
    ]


def __base_to_ounce(value_in_base):
    return value_in_base / 28.3495, [
        f"= ({value_in_base} * 1)g",
        f"= ({value_in_base} / 28.3495)oz",
    ]


# For Time
def __second_to_base(input_num):
    return input_num, [f"= {input_num}s"]


def __minute_to_base(input_num):
    return input_num * 60, [f"= {input_num}min", f"= ({input_num} * 60)s"]


def __hour_to_base(input_num):
    return input_num * 3600, [f"= {input_num}hr", f"= ({input_num} * 3600)s"]


def __day_to_base(input_num):
    return input_num * 86400, [f"= {input_num}day", f"= ({input_num} * 86400)s"]


def __base_to_second(value_in_base):
    return value_in_base, [f"= ({value_in_base} * 1)s"]


def __base_to_minute(value_in_base):
    return value_in_base / 60, [
        f"= ({value_in_base} * 1)s",
        f"= ({value_in_base} / 60)min",
    ]


def __base_to_hour(value_in_base):
    return value_in_base / 3600, [
        f"= ({value_in_base} * 1)s",
        f"= ({value_in_base} / 3600)hr",
    ]


def __base_to_day(value_in_base):
    return value_in_base / 86400, [
        f"= ({value_in_base} * 1)s",
        f"= ({value_in_base} / 86400)day",
    ]


# For Speed


def __mps_to_base(input_num):
    return input_num, [f"= {input_num}m/s"]


def __kmph_to_base(input_num):
    return input_num / 3.6, [f"= {input_num}kmph", f"= ({input_num} / 3.6)m/s"]


def __mph_to_base(input_num):
    return input_num / 2.237, [f"= {input_num}mph", f"= ({input_num} / 2.237)m/s"]


def __knots_to_base(input_num):
    return input_num / 1.944, [f"= {input_num}knot", f"= ({input_num} / 1.944)m/s"]


def __mach_to_base(input_num):
    return input_num * 343, [f"= Mach {input_num}", f"= ({input_num} * 343)m/s"]


def __base_to_mps(value_in_base):
    return value_in_base, [f"= ({value_in_base} * 1)m/s"]


def __base_to_kmph(value_in_base):
    return value_in_base * 3.6, [
        f"= ({value_in_base} * 1)m/s",
        f"= ({value_in_base} * 3.6)kmph",
    ]


def __base_to_mph(value_in_base):
    return value_in_base * 2.237, [
        f"= ({value_in_base} * 1)m/s",
        f"= ({value_in_base} * 2.237)mph",
    ]


def __base_to_knot(value_in_base):
    return value_in_base * 1.944, [
        f"= ({value_in_base} * 1)m/s",
        f"= ({value_in_base} * 1.944)knot",
    ]


def __base_to_mach(value_in_base):
    return value_in_base / 343, [
        f"= ({value_in_base} * 1)m/s",
        f"= Mach ({value_in_base} / 343)",
    ]


"""
Mapping section
"""

conversion_mapping_config = {
    "to_base": {
        # Length conversion mapping
        "length": {
            "m": __meter_to_base,
            "km": __kilometer_to_base,
            "cm": __centimeter_to_base,
            "inch": __inch_to_base,
            "feet": __feet_to_base,
        },
        # Temperature conversion mapping
        "temperature": {
            "k": __kelvin_to_base,
            "c": __celsius_to_base,
            "f": __fahrenheit_to_base,
        },
        # Weight conversion mapping
        "weight": {
            "g": __gram_to_base,
            "kg": __kilogram_to_base,
            "mg": __miligram_to_base,
            "lb": __pound_to_base,
            "oz": __ounce_to_base,
        },
        # Time conversion mappping
        "time": {
            "s": __second_to_base,
            "min": __minute_to_base,
            "hr": __hour_to_base,
            "day": __day_to_base,
        },
        # Speed conversion mapping
        "speed": {
            "mps": __mps_to_base,
            "kmph": __kmph_to_base,
            "mph": __mph_to_base,
            "knots": __knots_to_base,
            "mach": __mach_to_base,
        },
    },
    "from_base": {
        # Length conversion mapping
        "length": {
            "m": __base_to_meter,
            "km": __base_to_kilometer,
            "cm": __base_to_centimeter,
            "inch": __base_to_inche,
            "feet": __base_to_feet,
        },
        # Temperature conversion mapping
        "temperature": {
            "k": __base_to_kelvin,
            "c": __base_to_celsius,
            "f": __base_to_fahrenheit,
        },
        # Weight conversion mapping
        "weight": {
            "g": __base_to_gram,
            "kg": __base_to_kilogram,
            "mg": __base_to_miligram,
            "lb": __base_to_pound,
            "oz": __base_to_ounce,
        },
        # Time conversion mappping
        "time": {
            "s": __base_to_second,
            "min": __base_to_minute,
            "hr": __base_to_hour,
            "day": __base_to_day,
        },
        # Speed conversion mapping
        "speed": {
            "mps": __base_to_mps,
            "kmph": __base_to_kmph,
            "mph": __base_to_mph,
            "knots": __base_to_knot,
            "mach": __base_to_mach,
        },
    },
}

"""
Public function
"""


def convert(from_unit, to_unit, input_num, conversion_type):
    # def convert(from_unit, to_unit, input_num):
    if (
        not isinstance(from_unit, str)
        and not isinstance(to_unit, str)
        and (not isinstance(input_num, int) or not isinstance(input_num, float))
    ):
        raise ValueError

    value_in_base, steps_of_conversion_1 = (
        conversion_mapping_config.get("to_base")
        .get(conversion_type)
        .get(from_unit)(float(input_num))
    )

    converted_value, steps_of_conversion_2 = (
        conversion_mapping_config.get("from_base")
        .get(conversion_type)
        .get(to_unit)(float(value_in_base))
    )

    steps_of_conversion = steps_of_conversion_1 + steps_of_conversion_2

    return float(f"{converted_value:.4f}"), steps_of_conversion


# if __name__ == "__main__":
#     print(convert("m", "km", 1000))
