def length_conversion(value, from_unit, to_unit):
    length_units = {
        'meters': 1,
        'kilometers': 0.001,
        'miles': 0.000621371,
        'feet': 3.28084,
        'inches': 39.3701
    }
    
    if from_unit not in length_units or to_unit not in length_units:
        raise ValueError("Invalid length unit provided.")
    
    # Convert to meters first
    value_in_meters = value / length_units[from_unit]
    # Convert from meters to the target unit
    return value_in_meters * length_units[to_unit]

def temperature_conversion(value, from_unit, to_unit):
    if from_unit == 'Celsius':
        if to_unit == 'Fahrenheit':
            return (value * 9/5) + 32
        elif to_unit == 'Kelvin':
            return value + 273.15
    elif from_unit == 'Fahrenheit':
        if to_unit == 'Celsius':
            return (value - 32) * 5/9
        elif to_unit == 'Kelvin':
            return (value - 32) * 5/9 + 273.15
    elif from_unit == 'Kelvin':
        if to_unit == 'Celsius':
            return value - 273.15
        elif to_unit == 'Fahrenheit':
            return (value - 273.15) * 9/5 + 32
    
    raise ValueError("Invalid temperature unit provided.")

def weight_conversion(value, from_unit, to_unit):
    weight_units = {
        'grams': 1,
        'kilograms': 0.001,
        'pounds': 0.00220462,
        'ounces': 0.035274
    }
    
    if from_unit not in weight_units or to_unit not in weight_units:
        raise ValueError("Invalid weight unit provided.")
    
    # Convert to grams first
    value_in_grams = value / weight_units[from_unit]
    # Convert from grams to the target unit
    return value_in_grams * weight_units[to_unit]

def volume_conversion(value, from_unit, to_unit):
    volume_units = {
        'liters': 1,
        'milliliters': 1000,
        'gallons': 0.264172,
        'cubic meters': 0.001
    }
    
    if from_unit not in volume_units or to_unit not in volume_units:
        raise ValueError("Invalid volume unit provided.")
    
    # Convert to liters first
    value_in_liters = value / volume_units[from_unit]
    # Convert from liters to the target unit
    return value_in_liters * volume_units[to_unit]

def validate_input(value):
    if not isinstance(value, (int, float)):
        raise ValueError("Input value must be a number.")
    if value < 0:
        raise ValueError("Input value must be non-negative.")

def convert_units(value, from_unit, to_unit):
    validate_input(value)
    
    if from_unit in ['meters', 'kilometers', 'miles', 'feet', 'inches']:
        return length_conversion(value, from_unit, to_unit)
    elif from_unit in ['Celsius', 'Fahrenheit', 'Kelvin']:
        return temperature_conversion(value, from_unit, to_unit)
    elif from_unit in ['grams', 'kilograms', 'pounds', 'ounces']:
        return weight_conversion(value, from_unit, to_unit)
    elif from_unit in ['liters', 'milliliters', 'gallons', 'cubic meters']:
        return volume_conversion(value, from_unit, to_unit)
    else:
        raise ValueError("Unsupported unit type.")