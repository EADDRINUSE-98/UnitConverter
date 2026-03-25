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
    return input_num


def __kilometer_to_base(input_num):
    return input_num * 1000


def __centimeter_to_base(input_num):
    return input_num / 100


def __inch_to_base(input_num):
    return input_num / 39.37


def __feet_to_base(input_num):
    return input_num / 3.281


"""
'base_unit' to 'to_unit' conversion function definition section.
"""


# For Length
def __base_to_meter(value_in_base):
    return value_in_base


def __base_to_kilometer(value_in_base):
    return value_in_base / 1000


def __base_to_centimeter(value_in_base):
    return value_in_base * 100


def __base_to_inche(value_in_base):
    return value_in_base * 39.37


def __base_to_feet(value_in_base):
    return value_in_base * 3.281


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
        # Weight conversion mapping
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
        # Weight conversion mapping
        # Speed conversion mapping
        # Time conversion mappping
    },
}

"""
Public function
"""


def convert(from_unit, to_unit, input_num):
    value_in_base = conversion_mapping_config.get("to_base").get(from_unit)(
        float(input_num)
    )
    converted_value = conversion_mapping_config.get("from_base").get(to_unit)(
        float(value_in_base)
    )
    return float(converted_value)


if __name__ == "__main__":
    print(convert("m", "km", 1000))
