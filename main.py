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
        "picometers": 1e-12,
        "furlongs": 201.168,
        "light years": 9.461e15,
        "astronomical units": 1.496e11
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
        "picograms": 1e-12,
        "stones": 6350.29,
        "short tons": 907184.74,
        "long tons": 1016046.91
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
        "square inches": 0.00064516,
        "square nautical miles": 3.429e6,
        "square micrometers": 1e-12,
        "square nanometers": 1e-18,
        "square picometers": 1e-24
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
        "teaspoons": 0.00000492892,
        "cubic miles": 4.168e9,
        "cubic yards": 0.764555,
        "cubic nanometers": 1e-27,
        "cubic micrometers": 1e-18,
        "cubic furlongs": 8.64554858e7
    }
    if from_unit in units and to_unit in units:
        return value * (units[to_unit] / units[from_unit])
    else:
        return None

def convert_speed(value, from_unit, to_unit):
    units = {
        "meters per second": 1.0,
        "kilometers per hour": 0.277778,
        "miles per hour": 0.44704,
        "feet per second": 0.3048,
        "knots": 0.514444,
        "mach": 343.0,
        "speed of light": 299792458.0,
        "inches per second": 0.0254,
        "yards per second": 0.9144,
        "millimeters per second": 0.001,
        "centimeters per second": 0.01,
        "micrometers per second": 1e-6,
        "nanometers per second": 1e-9
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
    print("Speed Conversion: 60 miles per hour to meters per second:", convert_speed(60, "miles per hour", "meters per second"))

if __name__ == "__main__":
    main()
