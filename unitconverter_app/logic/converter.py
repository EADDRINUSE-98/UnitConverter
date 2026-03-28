"""
from_unit -> base_unit
base_unit -> to_unit

length base unit: meters
temperature base unit: kelvin
weight base unit: gram
speed base unit: kmph
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
    return input_num * 255.928, [
        f"= {input_num}°f",
        f"= (({input_num} - 32) * (5/9) + 273.15)°k",
    ]

def __base_to_kelvin(value_in_base):
    return value_in_base, [f"= ({value_in_base} * 1)°k"]

def __base_to_celsius(value_in_base):
    return value_in_base - 273.15, [f"= ({value_in_base} * 1)°k", f"= ({value_in_base} - 273.15)°c"]

def __base_to_fahrenheit(value_in_base):
    return value_in_base / 255.928, [f"= ({value_in_base} * 1)°k", f"= (({value_in_base} + 32) * (9/5) - 273.15)°f"]


# For Weight

def __gram_to_base(input_num):
    return input_num, [f"= {input_num}g"]


def __kilogram_to_base(input_num):
    return input_num * 1000, [f"= {input_num}kg", [f"= ({input_num} * 1000)g"]]


def __miligram_to_base(input_num):
    return input_num / 1000, [f"= {input_num}mg", f"= ({input_num} / 1000)g"]


def __pound_to_base(input_num):
    return input_num * 453.592, [f"= {input_num}lb", f"= ({input_num} * 453.592)g"]


def __ounce_to_base(input_num):
    return input_num * 28.3495, [f"= {input_num}oz", f"= ({input_num} * 28.3495)g"]


def __base_to_gram(value_in_base):
    return value_in_base, [f"= ({value_in_base} * 1)g"]


def __base_to_kilogram(value_in_base):
    return value_in_base / 1000, [f"= ({value_in_base} * 1)g", [f"= ({value_in_base} / 1000)kg"]]


def __base_to_miligram(value_in_base):
    return value_in_base * 1000, [f"= ({value_in_base} * 1)g", f"= ({value_in_base} * 1000)mg"]


def __base_to_pound(value_in_base):
    return value_in_base / 453.592, [f"= ({value_in_base} * 1)g", f"= ({value_in_base} / 453.592)lb"]


def __base_to_ounce(value_in_base):
    return value_in_base / 28.3495, [f"= ({value_in_base} * 1)g", f"= ({value_in_base} / 28.3495)oz"]


"""
Mapping section
"""

conversion_mapping_config = {
    "to_base": {
        # Length conversion mapping
        "m": __meter_to_base,
        "km": __kilometer_to_base,
        "cm": __centimeter_to_base,
        "inch": __inch_to_base,
        "feet": __feet_to_base,
        # Temperature conversion mapping
        "kelvin": __kelvin_to_base,
        "celcius": __celsius_to_base,
        "fahrenheit": __fahrenheit_to_base,
        # Weight conversion mapping
        "g": __gram_to_base,
        "kg": __kilogram_to_base,
        "mg": __miligram_to_base,
        "lb": __pound_to_base,#pound
        "oz": __ounce_to_base,#ounce
        # Speed conversion mapping
        # Time conversion mappping
    },
    "from_base": {
        # Length conversion mapping
        "m": __base_to_meter,
        "km": __base_to_kilometer,
        "cm": __base_to_centimeter,
        "inch": __base_to_inche,
        "feet": __base_to_feet,
        # Temperature conversion mapping
        "kelvin": __base_to_kelvin,
        "celcius": __base_to_celsius,
        "fahrenheit": __base_to_fahrenheit,
        # Weight conversion mapping
        "g": __base_to_gram,
        "kg": __base_to_kilogram,
        "mg": __base_to_miligram,
        "lb": __base_to_pound,#pound
        "oz": __base_to_ounce,#ounce
        # Speed conversion mapping
        # Time conversion mappping
    },
}

"""
Public function
"""


def convert(from_unit, to_unit, input_num):
    value_in_base, steps_of_conversion_1 = conversion_mapping_config.get("to_base").get(
        from_unit
    )(float(input_num))

    converted_value, steps_of_conversion_2 = conversion_mapping_config.get(
        "from_base"
    ).get(to_unit)(float(value_in_base))
    steps_of_conversion = steps_of_conversion_1 + steps_of_conversion_2
    return float(f"{converted_value:.4f}"), steps_of_conversion


if __name__ == "__main__":
    print(convert("m", "km", 1000))
