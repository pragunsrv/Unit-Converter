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
        "astronomical units": 1.496e11,
        "parsecs": 3.086e16,
        "angstroms": 1e-10
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
        "long tons": 1016046.91,
        "carats": 0.2,
        "grains": 0.06479891
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
    elif from_unit == "celsius" and to_unit == "delisle":
        return (100 - value) * 3/2
    elif from_unit == "fahrenheit" and to_unit == "delisle":
        return (212 - value) * 5/6
    elif from_unit == "kelvin" and to_unit == "delisle":
        return (373.15 - value) * 3/2
    elif from_unit == "rankine" and to_unit == "delisle":
        return (671.67 - value) * 5/6
    elif from_unit == "delisle" and to_unit == "celsius":
        return 100 - value * 2/3
    elif from_unit == "delisle" and to_unit == "fahrenheit":
        return 212 - value * 6/5
    elif from_unit == "delisle" and to_unit == "kelvin":
        return 373.15 - value * 2/3
    elif from_unit == "delisle" and to_unit == "rankine":
        return 671.67 - value * 6/5
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
        "square picometers": 1e-24,
        "barns": 1e-28
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
        "cubic furlongs": 8.64554858e7,
        "cubic angstroms": 1e-30,
        "cubic barns": 1e-84
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
        "nanometers per second": 1e-9,
        "leagues per hour": 0.277778,
        "furlongs per fortnight": 0.00016630952
    }
    if from_unit in units and to_unit in units:
        return value * (units[to_unit] / units[from_unit])
    else:
        return None

def convert_time(value, from_unit, to_unit):
    units = {
        "seconds": 1.0,
        "minutes": 60.0,
        "hours": 3600.0,
        "days": 86400.0,
        "weeks": 604800.0,
        "months": 2.63e6,
        "years": 3.154e7,
        "milliseconds": 1e-3,
        "microseconds": 1e-6,
        "nanoseconds": 1e-9,
        "picoseconds": 1e-12,
        "femtoseconds": 1e-15,
        "attoseconds": 1e-18,
        "fortnights": 1.2096e6,
        "centuries": 3.154e9,
        "millennia": 3.154e10,
        "plank time": 5.39e-44
    }
    if from_unit in units and to_unit in units:
        return value * (units[to_unit] / units[from_unit])
    else:
        return None

def main():
    print("Length Conversion: 10 light years to parsecs:", convert_length(10, "light years", "parsecs"))
    print("Weight Conversion: 5000 grams to carats:", convert_weight(5000, "grams", "carats"))
    print("Temperature Conversion: 100 celsius to delisle:", convert_temperature(100, "celsius", "delisle"))
    print("Area Conversion: 500 square kilometers to square miles:", convert_area(500, "square kilometers", "square miles"))
    print("Volume Conversion: 10 liters to cubic barns:", convert_volume(10, "liters", "cubic barns"))
    print("Speed Conversion: 100 knots to leagues per hour:", convert_speed(100, "knots", "leagues per hour"))
    print("Time Conversion: 1 year to fortnights:", convert_time(1, "years", "fortnights"))

if __name__ == "__main__":
    main()
