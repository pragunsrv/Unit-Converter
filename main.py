def convert_length(value, from_unit, to_unit):
    units = {
        "meters": 1.0,
        "kilometers": 1000.0,
        "centimeters": 0.01,
        "millimeters": 0.001,
        "miles": 1609.34,
        "yards": 0.9144,
        "feet": 0.3048,
        "inches": 0.0254
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
        "ounces": 28.3495
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
    else:
        return None

def main():
    print("Length Conversion: 5 meters to kilometers:", convert_length(5, "meters", "kilometers"))
    print("Weight Conversion: 5000 grams to kilograms:", convert_weight(5000, "grams", "kilograms"))
    print("Temperature Conversion: 100 celsius to fahrenheit:", convert_temperature(100, "celsius", "fahrenheit"))

if __name__ == "__main__":
    main()
