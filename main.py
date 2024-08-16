def convert_length(value, from_unit, to_unit):
    units = {
        "meters": 1.0,
        "kilometers": 1000.0,
        "centimeters": 0.01,
        "millimeters": 0.001,
        "miles": 1609.34,
        "yards": 0.9144,
        "feet": 0.3048,
        "inches": 0.0254,
        "nautical miles": 1852.0,
        "micrometers": 1e-6,
        "nanometers": 1e-9,
        "picometers": 1e-12
    }
    if from_unit in units and to_unit in units:
        return value * (units[to_unit] / units[from_unit])
    else:
        return None

def convert_weight(value, from_unit, to_unit):
    units = {
        "grams": 1.0,
        "kilograms": 1000.0,
        "milligrams": 0.001,
        "pounds": 453.592,
        "ounces": 28.3495,
        "tons": 1e6,
        "micrograms": 1e-6,
        "nanograms": 1e-9,
        "picograms": 1e-12
    }
    if from_unit in units and to_unit in units:
        return value * (units[to_unit] / units[from_unit])
    else:
        return None

def convert_temperature(value, from_unit, to_unit):
    if from_unit == "celsius" and to_unit == "fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "fahrenheit" and to_unit == "celsius":
        return (value - 32) * 5/9
    elif from_unit == "celsius" and to_unit == "kelvin":
        return value + 273.15
    elif from_unit == "kelvin" and to_unit == "celsius":
        return value - 273.15
    elif from_unit == "fahrenheit" and to_unit == "kelvin":
        return (value - 32) * 5/9 + 273.15
    elif from_unit == "kelvin" and to_unit == "fahrenheit":
        return (value - 273.15) * 9/5 + 32
    elif from_unit == "celsius" and to_unit == "rankine":
        return (value + 273.15) * 9/5
    elif from_unit == "fahrenheit" and to_unit == "rankine":
        return value + 459.67
    elif from_unit == "kelvin" and to_unit == "rankine":
        return value * 9/5
    elif from_unit == "rankine" and to_unit == "celsius":
        return (value - 491.67) * 5/9
    elif from_unit == "rankine" and to_unit == "fahrenheit":
        return value - 459.67
    elif from_unit == "rankine" and to_unit == "kelvin":
        return value * 5/9
    else:
        return None

def convert_area(value, from_unit, to_unit):
    units = {
        "square meters": 1.0,
        "square kilometers": 1e6,
        "square centimeters": 0.0001,
        "square millimeters": 1e-6,
        "hectares": 1e4,
        "square miles": 2.59e6,
        "acres": 4046.86,
        "square yards": 0.836127,
        "square feet": 0.092903,
        "square inches": 0.00064516
    }
    if from_unit in units and to_unit in units:
        return value * (units[to_unit] / units[from_unit])
    else:
        return None

def convert_volume(value, from_unit, to_unit):
    units = {
        "cubic meters": 1.0,
        "liters": 0.001,
        "milliliters": 1e-6,
        "cubic centimeters": 1e-6,
        "cubic millimeters": 1e-9,
        "cubic kilometers": 1e9,
        "cubic feet": 0.0283168,
        "cubic inches": 0.0000163871,
        "gallons": 0.00378541,
        "quarts": 0.000946353,
        "pints": 0.000473176,
        "cups": 0.000236588,
        "tablespoons": 0.0000147868,
        "teaspoons": 0.00000492892
    }
    if from_unit in units and to_unit in units:
        return value * (units[to_unit] / units[from_unit])
    else:
        return None

def main():
    print("Length Conversion: 5 meters to kilometers:", convert_length(5, "meters", "kilometers"))
    print("Weight Conversion: 5000 grams to kilograms:", convert_weight(5000, "grams", "kilograms"))
    print("Temperature Conversion: 100 celsius to fahrenheit:", convert_temperature(100, "celsius", "fahrenheit"))
    print("Area Conversion: 1000 square meters to hectares:", convert_area(1000, "square meters", "hectares"))
    print("Volume Conversion: 2 liters to cubic meters:", convert_volume(2, "liters", "cubic meters"))

if __name__ == "__main__":
    main()
