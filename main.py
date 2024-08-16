def convert_temperature(value, from_unit, to_unit):
    units = {
        "celsius": 1.0,
        "fahrenheit": (5.0 / 9.0),
        "kelvin": 1.0,
        "rankine": (5.0 / 9.0),
        "delisle": 100.0,
        "reaumur": 1.25,
        "newton": 0.333333,
        "romer": (5.0 / 9.0),
        "leiden": 1.0,
        "rømer": (5.0 / 9.0),
        "centigrade": 1.0,
        "absolute": 1.0
    }
    if from_unit == "fahrenheit":
        value = (value - 32) * (5.0 / 9.0)
    elif from_unit == "rankine":
        value = (value - 491.67) * (5.0 / 9.0)
    elif from_unit == "delisle":
        value = 100 - value
    elif from_unit == "reaumur":
        value = value * (5.0 / 4.0)
    elif from_unit == "newton":
        value = value * (100.0 / 33.0)
    elif from_unit == "romer":
        value = (value - 7.5) * (5.0 / 24.0) + 273.15
    elif from_unit == "leiden":
        value = value
    elif from_unit == "rømer":
        value = (value - 7.5) * (5.0 / 24.0) + 273.15
    elif from_unit == "centigrade":
        value = value
    elif from_unit == "absolute":
        value = value - 273.15

    if to_unit == "fahrenheit":
        return (value * (9.0 / 5.0)) + 32
    elif to_unit == "rankine":
        return (value * (9.0 / 5.0)) + 491.67
    elif to_unit == "delisle":
        return 100 - value
    elif to_unit == "reaumur":
        return value * (4.0 / 5.0)
    elif to_unit == "newton":
        return value * (33.0 / 100.0)
    elif to_unit == "romer":
        return (value - 273.15) * (24.0 / 5.0) + 7.5
    elif to_unit == "leiden":
        return value
    elif to_unit == "rømer":
        return (value - 273.15) * (24.0 / 5.0) + 7.5
    elif to_unit == "centigrade":
        return value
    elif to_unit == "absolute":
        return value + 273.15
    else:
        return None

def convert_area(value, from_unit, to_unit):
    units = {
        "square meters": 1.0,
        "square kilometers": 1e6,
        "hectares": 1e4,
        "square miles": 2.58999e6,
        "acres": 4046.86,
        "square feet": 0.092903,
        "square yards": 0.836127,
        "square centimeters": 1e-4,
        "square millimeters": 1e-6,
        "ares": 100.0,
        "dunams": 1000.0,
        "bighas": 3350.0,
        "cane": 0.00446,
        "bighas": 3350.0,
        "gunthas": 0.01,
        "kanal": 505.857,
        "muraba": 64.0,
        "marla": 0.0253,
        "kattha": 338.0,
        "paisa": 0.0625,
        "nali": 1652.0,
        "tarms": 4.04686,
        "guntas": 101.171,
        "bighas (Nepal)": 3350.0,
        "bhigas": 1000.0,
        "seres": 404.686,
        "magas": 0.00446,
        "rasis": 10.0
    }
    if from_unit in units and to_unit in units:
        return value * (units[to_unit] / units[from_unit])
    else:
        return None

def convert_volume(value, from_unit, to_unit):
    units = {
        "liters": 1.0,
        "milliliters": 1e-3,
        "cubic meters": 1000.0,
        "cubic centimeters": 1e-3,
        "cubic inches": 1.63871e-5,
        "cubic feet": 0.0283168,
        "gallons": 3.78541,
        "quarts": 0.946353,
        "pints": 0.473176,
        "fluid ounces": 0.0295735,
        "tablespoons": 0.0147868,
        "teaspoons": 0.00492892,
        "cubic yards": 0.764555,
        "imperial gallons": 4.54609,
        "imperial quarts": 1.13652,
        "imperial pints": 0.568261,
        "imperial fluid ounces": 0.0284131,
        "bushels": 35.2391,
        "cubic decimeters": 1.0,
        "barrels": 158.987,
        "mug": 0.236588,
        "cup": 0.236588,
        "glass": 0.237,
        "scoop": 0.06,
        "paddle": 0.1,
        "drams": 0.0037,
        "drops": 1.0e-4,
        "shot glasses": 0.04436,
        "jiggers": 0.04436,
        "jugs": 2.0,
        "pitchers": 1.0,
        "carafes": 0.5,
        "flasks": 0.1
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
        "centimeters per second": 0.01,
        "inches per second": 0.0254,
        "yards per second": 0.9144,
        "meters per minute": 0.0166667,
        "kilometers per minute": 0.0166667,
        "miles per minute": 0.0268224,
        "feet per minute": 0.018288,
        "knots per minute": 0.00857,
        "centimeters per minute": 0.00016667,
        "inches per minute": 0.00042333,
        "yards per minute": 0.00083333,
        "meters per hour": 0.000277778,
        "kilometers per hour": 0.000277778,
        "miles per hour": 0.00044704,
        "feet per hour": 0.0001,
        "knots per hour": 0.000514444,
        "centimeters per hour": 0.00001,
        "inches per hour": 0.0000254,
        "yards per hour": 0.00009144,
        "meters per day": 1.1574e-5,
        "kilometers per day": 1.1574e-5,
        "miles per day": 1.763e-5,
        "feet per day": 1.06e-5,
        "knots per day": 1.11e-5,
        "centimeters per day": 1.1574e-5,
        "inches per day": 1.32e-5,
        "yards per day": 1.31e-5,
        "kilometers per second": 0.000277778,
        "miles per second": 0.00044704,
        "feet per second": 0.3048,
        "knots per second": 0.514444,
        "centimeters per second": 0.01,
        "inches per second": 0.0254,
        "yards per second": 0.9144
    }
    if from_unit in units and to_unit in units:
        return value * (units[to_unit] / units[from_unit])
    else:
        return None

def convert_pressure(value, from_unit, to_unit):
    units = {
        "pascals": 1.0,
        "kilopascals": 1e3,
        "hectopascals": 1e2,
        "bar": 1e5,
        "atmospheres": 101325.0,
        "psi": 6894.76,
        "torr": 133.322,
        "mmHg": 133.322,
        "inHg": 3386.39,
        "dynes per square centimeter": 0.1,
        "pounds per square inch": 6894.76,
        "kgf per square meter": 9806.65,
        "kgf per square centimeter": 98066.5,
        "mpa": 1e6,
        "psi (US)": 6894.76,
        "psi (UK)": 6894.76,
        "kilogram-force per square centimeter": 98066.5,
        "newtons per square meter": 1.0,
        "megapascals": 1e6,
        "gigapascals": 1e9,
        "hydrostatic pressure": 9810.0,
        "gauge pressure": 101325.0,
        "absolute pressure": 101325.0,
        "differential pressure": 101325.0,
        "vapor pressure": 100000.0,
        "inches of water": 249.088,
        "millibars": 100.0,
        "hectopascals (hPa)": 100.0,
        "kilobars": 100000.0,
        "exabytes per square meter": 1e-18,
        "petabytes per square meter": 1e-15,
        "terabytes per square meter": 1e-12
    }
    if from_unit in units and to_unit in units:
        return value * (units[to_unit] / units[from_unit])
    else:
        return None

def convert_power(value, from_unit, to_unit):
    units = {
        "watts": 1.0,
        "kilowatts": 1000.0,
        "megawatts": 1e6,
        "gigawatts": 1e9,
        "terawatts": 1e12,
        "horsepower": 745.7,
        "foot-pounds per minute": 0.22481,
        "calories per second": 4.184,
        "kilocalories per second": 4184.0,
        "british thermal units per hour": 0.293071,
        "watt-hours": 1.0,
        "kilowatt-hours": 1000.0,
        "megawatt-hours": 1e6,
        "gigawatt-hours": 1e9,
        "terawatt-hours": 1e12,
        "Joules per second": 1.0,
        "calories per minute": 250.0,
        "kilocalories per hour": 15000000.0,
        "tonnes of refrigeration": 3516.85,
        "watt-seconds": 1.0,
        "joules per second": 1.0,
        "thermal units": 1055.06,
        "horsepower hours": 745.7,
        "ergs per second": 1e-7,
        "BTU per minute": 0.04923,
        "calories per hour": 15000.0,
        "kilojoules per second": 1000.0,
        "megajoules per minute": 60000.0,
        "gigajoules per hour": 3600000.0,
        "terajoules per day": 3.6e12
    }
    if from_unit in units and to_unit in units:
        return value * (units[to_unit] / units[from_unit])
    else:
        return None

def convert_voltage(value, from_unit, to_unit):
    units = {
        "volts": 1.0,
        "millivolts": 1e-3,
        "kilovolts": 1e3,
        "megavolts": 1e6,
        "gigavolts": 1e9,
        "microvolts": 1e-6,
        "nanovolts": 1e-9,
        "picovolts": 1e-12,
        "statvolts": 299.792,
        "abvolts": 1e-8,
        "electrostatic volts": 299.792,
        "volt-amperes": 1.0,
        "volt-amps reactive": 1.0,
        "volt-hours": 1.0,
        "volt-seconds": 1.0,
        "voltage drop": 1.0,
        "electric potential": 1.0,
        "microvolts per meter": 1e-6,
        "millivolts per meter": 1e-3,
        "kilovolts per meter": 1e3,
        "megavolts per meter": 1e6,
        "gigavolts per meter": 1e9,
        "millivolts per centimeter": 1e-2,
        "microvolts per centimeter": 1e-5,
        "kilovolts per centimeter": 1e1,
        "megavolts per centimeter": 1e4,
        "gigavolts per centimeter": 1e7,
        "statvolts per meter": 299.792,
        "abvolts per meter": 1e-8,
        "volts per second": 1.0
    }
    if from_unit in units and to_unit in units:
        return value * (units[to_unit] / units[from_unit])
    else:
        return None

def convert_energy(value, from_unit, to_unit):
    units = {
        "joules": 1.0,
        "kilojoules": 1000.0,
        "megajoules": 1e6,
        "gigajoules": 1e9,
        "terajoules": 1e12,
        "calories": 4.184,
        "kilocalories": 4184.0,
        "british thermal units": 1055.06,
        "foot-pounds": 1.35582,
        "electronvolts": 1.602e-19,
        "watt-hours": 3600.0,
        "kilowatt-hours": 3.6e6,
        "megawatt-hours": 3.6e9,
        "gigawatt-hours": 3.6e12,
        "terawatt-hours": 3.6e15,
        "watt-seconds": 1.0,
        "kilowatt-seconds": 1000.0,
        "megawatt-seconds": 1e6,
        "gigawatt-seconds": 1e9,
        "terawatt-seconds": 1e12,
        "therms": 105505585.0,
        "calories per second": 4.184,
        "calories per minute": 250.0,
        "calories per hour": 15000.0,
        "kilocalories per second": 4184.0,
        "kilocalories per minute": 250000.0,
        "kilocalories per hour": 15000000.0,
        "megajoules per second": 1e6,
        "megajoules per minute": 6e7,
        "megajoules per hour": 3.6e9,
        "gigajoules per second": 1e9,
        "gigajoules per minute": 6e10,
        "gigajoules per hour": 3.6e12,
        "BTUs": 1055.06,
        "kcal": 4184.0,
        "kWh": 3600.0,
        "MWh": 3.6e6,
        "GWh": 3.6e9
    }
    if from_unit in units and to_unit in units:
        return value * (units[to_unit] / units[from_unit])
    else:
        return None

def convert_frequency(value, from_unit, to_unit):
    units = {
        "hertz": 1.0,
        "kilohertz": 1e3,
        "megahertz": 1e6,
        "gigahertz": 1e9,
        "terahertz": 1e12,
        "revolutions per second": 1.0,
        "revolutions per minute": 0.0166667,
        "cycles per second": 1.0,
        "cycles per minute": 0.0166667,
        "rpm": 0.0166667,
        "beats per minute": 0.0166667,
        "oscillations per second": 1.0,
        "pulses per second": 1.0,
        "wavelength per second": 1.0,
        "frequency per second": 1.0,
        "hertz per second": 1.0,
        "kilohertz per second": 1e3,
        "megahertz per second": 1e6,
        "gigahertz per second": 1e9,
        "terahertz per second": 1e12,
        "hertz per minute": 0.0166667,
        "kilohertz per minute": 1e-2,
        "megahertz per minute": 1e-5,
        "gigahertz per minute": 1e-8,
        "terahertz per minute": 1e-11,
        "hertz per hour": 2.77778e-4,
        "kilohertz per hour": 2.77778e-7,
        "megahertz per hour": 2.77778e-10,
        "gigahertz per hour": 2.77778e-13,
        "terahertz per hour": 2.77778e-16
    }
    if from_unit in units and to_unit in units:
        return value * (units[to_unit] / units[from_unit])
    else:
        return None

def main():
    while True:
        print("\nUnit Converter")
        print("1. Temperature")
        print("2. Area")
        print("3. Volume")
        print("4. Speed")
        print("5. Pressure")
        print("6. Power")
        print("7. Voltage")
        print("8. Energy")
        print("9. Frequency")
        print("10. Exit")
        print("11. Length")
        print("12. Mass")
        print("13. Time")
        print("14. Density")
        print("15. Force")
        print("16. Data")
        choice = input("Enter your choice: ")
        if choice == "10":
            break
        
        if choice == "11":
            print("Length conversion selected.")
            value = float(input("Enter the value: "))
            from_unit = input("Enter from unit: ")
            to_unit = input("Enter to unit: ")
            result = convert_length(value, from_unit, to_unit)
        elif choice == "12":
            print("Mass conversion selected.")
            value = float(input("Enter the value: "))
            from_unit = input("Enter from unit: ")
            to_unit = input("Enter to unit: ")
            result = convert_mass(value, from_unit, to_unit)
        elif choice == "13":
            print("Time conversion selected.")
            value = float(input("Enter the value: "))
            from_unit = input("Enter from unit: ")
            to_unit = input("Enter to unit: ")
            result = convert_time(value, from_unit, to_unit)
        elif choice == "14":
            print("Density conversion selected.")
            value = float(input("Enter the value: "))
            from_unit = input("Enter from unit: ")
            to_unit = input("Enter to unit: ")
            result = convert_density(value, from_unit, to_unit)
        elif choice == "15":
            print("Force conversion selected.")
            value = float(input("Enter the value: "))
            from_unit = input("Enter from unit: ")
            to_unit = input("Enter to unit: ")
            result = convert_force(value, from_unit, to_unit)
        elif choice == "16":
            print("Data conversion selected.")
            value = float(input("Enter the value: "))
            from_unit = input("Enter from unit: ")
            to_unit = input("Enter to unit: ")
            result = convert_data(value, from_unit, to_unit)
        else:
            value = float(input("Enter the value: "))
            from_unit = input("Enter from unit: ")
            to_unit = input("Enter to unit: ")

            if choice == "1":
                result = convert_temperature(value, from_unit, to_unit)
            elif choice == "2":
                result = convert_area(value, from_unit, to_unit)
            elif choice == "3":
                result = convert_volume(value, from_unit, to_unit)
            elif choice == "4":
                result = convert_speed(value, from_unit, to_unit)
            elif choice == "5":
                result = convert_pressure(value, from_unit, to_unit)
            elif choice == "6":
                result = convert_power(value, from_unit, to_unit)
            elif choice == "7":
                result = convert_voltage(value, from_unit, to_unit)
            elif choice == "8":
                result = convert_energy(value, from_unit, to_unit)
            elif choice == "9":
                result = convert_frequency(value, from_unit, to_unit)
            else:
                print("Invalid choice")
                continue
        
        if result is not None:
            print(f"Converted value: {result}")
        else:
            print("Invalid units")

def convert_length(value, from_unit, to_unit):
    units = {
        "meters": 1.0,
        "kilometers": 1e3,
        "centimeters": 1e-2,
        "millimeters": 1e-3,
        "micrometers": 1e-6,
        "nanometers": 1e-9,
        "miles": 1609.34,
        "yards": 0.9144,
        "feet": 0.3048,
        "inches": 0.0254,
        "nautical miles": 1852.0,
        "parsecs": 3.08567758149137e16,
        "light years": 9.4607e15,
        "astronomical units": 1.496e11,
        "furlongs": 201.168,
        "chains": 20.1168,
        "rods": 5.0292,
        "perches": 5.0292,
        "links": 0.201168
    }
    if from_unit in units and to_unit in units:
        return value * (units[to_unit] / units[from_unit])
    else:
        return None

def convert_mass(value, from_unit, to_unit):
    units = {
        "grams": 1.0,
        "kilograms": 1e3,
        "milligrams": 1e-3,
        "micrograms": 1e-6,
        "tonnes": 1e6,
        "pounds": 453.592,
        "ounces": 28.3495,
        "stones": 6350.29,
        "slugs": 145.038,
        "grains": 64.79891,
        "carats": 2e-1,
        "daltons": 1.66053906660e-27,
        "atomic mass units": 1.66053906660e-27,
        "planck mass": 2.17644e-8,
        "slug": 145.038,
        "kiloponds": 9.80665e2,
        "tonnes (metric)": 1e6,
        "tonnes (short)": 9.072e5
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
        "months": 2.628e6,
        "years": 3.154e7,
        "milliseconds": 1e-3,
        "microseconds": 1e-6,
        "nanoseconds": 1e-9,
        "picoseconds": 1e-12,
        "femtoseconds": 1e-15,
        "attoseconds": 1e-18,
        "centuries": 3.15576e9,
        "decades": 3.154e8,
        "fortnights": 1209600.0,
        "quarters": 7.884e6
    }
    if from_unit in units and to_unit in units:
        return value * (units[to_unit] / units[from_unit])
    else:
        return None

def convert_density(value, from_unit, to_unit):
    units = {
        "kg/m^3": 1.0,
        "g/cm^3": 1000.0,
        "g/mL": 1000.0,
        "lb/ft^3": 16.0185,
        "lb/in^3": 27679.9,
        "slug/ft^3": 515.378,
        "oz/yd^3": 0.5977,
        "g/L": 1.0,
        "kg/L": 1000.0,
        "g/m^3": 1e-3,
        "mg/m^3": 1e-6
    }
    if from_unit in units and to_unit in units:
        return value * (units[to_unit] / units[from_unit])
    else:
        return None

def convert_force(value, from_unit, to_unit):
    units = {
        "newtons": 1.0,
        "dynes": 1e-5,
        "pounds-force": 4.44822,
        "kilograms-force": 9.80665,
        "ounces-force": 0.2780139,
        "kips": 4448.22,
        "ton-force (short)": 8896.44,
        "ton-force (long)": 9806.65,
        "poundals": 0.138255,
        "kiloponds": 9.80665,
        "grams-force": 0.00980665
    }
    if from_unit in units and to_unit in units:
        return value * (units[to_unit] / units[from_unit])
    else:
        return None

def convert_data(value, from_unit, to_unit):
    units = {
        "bytes": 1.0,
        "kilobytes": 1e3,
        "megabytes": 1e6,
        "gigabytes": 1e9,
        "terabytes": 1e12,
        "petabytes": 1e15,
        "exabytes": 1e18,
        "zettabytes": 1e21,
        "yottabytes": 1e24,
        "bits": 1e-3,
        "kilobits": 1.0,
        "megabits": 1e3,
        "gigabits": 1e6,
        "terabits": 1e9,
        "petabits": 1e12,
        "exabits": 1e15,
        "zettabits": 1e18,
        "yottabits": 1e21,
        "nibbles": 0.5,
        "words": 2.0
    }
    if from_unit in units and to_unit in units:
        return value * (units[to_unit] / units[from_unit])
    else:
        return None
def convert_mass_(value, from_unit, to_unit):
    units = {
        "grams": 1.0,
        "kilograms": 1e3,
        "milligrams": 1e-3,
        "micrograms": 1e-6,
        "pounds": 453.592,
        "ounces": 28.3495,
        "tons": 907184.74,
        "stones": 6350.29,
        "carats": 2.0,
        "atomic mass units": 1.66054e-27,
        "kilograms per cubic meter": 1e3,
        "grams per cubic centimeter": 1.0,
        "slugs": 145.038,
        "newtons": 9.80665,
        "pennyweights": 1.55517,
        "troy ounces": 31.1035,
        "pennyweight": 1.55517,
        "kips": 4448.22,
        "kilograms per liter": 1e3,
        "milligrams per milliliter": 1e-3,
        "pounds per gallon": 119.826,
        "stones per cubic meter": 6350.29,
        "ounces per cubic foot": 0.0283495
    }
    if from_unit in units and to_unit in units:
        return value * (units[to_unit] / units[from_unit])
    else:
        return None

def convert_time_(value, from_unit, to_unit):
    units = {
        "seconds": 1.0,
        "minutes": 60.0,
        "hours": 3600.0,
        "days": 86400.0,
        "weeks": 604800.0,
        "months": 2628000.0,
        "years": 31536000.0,
        "milliseconds": 1e-3,
        "microseconds": 1e-6,
        "nanoseconds": 1e-9,
        "fortnights": 1209600.0,
        "centuries": 3.1536e9,
        "decades": 3.1536e8,
        "quarters": 7884000.0,
        "hours (decimal)": 3600.0,
        "minutes (decimal)": 60.0,
        "seconds (decimal)": 1.0,
        "milliseconds (decimal)": 0.001,
        "microseconds (decimal)": 1e-6,
        "nanoseconds (decimal)": 1e-9,
        "leap years": 31622400.0,
        "Julian years": 31557600.0
    }
    if from_unit in units and to_unit in units:
        return value * (units[to_unit] / units[from_unit])
    else:
        return None


def main():
    while True:
        print("\nUnit Converter")
        print("1. Temperature")
        print("2. Area")
        print("3. Volume")
        print("4. Speed")
        print("5. Pressure")
        print("6. Power")
        print("7. Voltage")
        print("8. Energy")
        print("9. Frequency")
        print("10. Exit")
        print("11. Length")
        print("12. Mass")
        print("13. Time")
        print("14. Density")
        print("15. Force")
        print("16. Data")
        print("17. Advanced Length")
        print("18. Advanced Mass")
        print("19. Advanced Time")
        print("20. Advanced Density")
        print("21. Advanced Force")
        print("22. Advanced Data")
        choice = input("Enter your choice: ")
        if choice == "10":
            break
        
        if choice == "17":
            print("Advanced Length conversion selected.")
            value = float(input("Enter the value: "))
            from_unit = input("Enter from unit: ")
            to_unit = input("Enter to unit: ")
            result = convert_length(value, from_unit, to_unit)
            print(f"Result: {result}")

        elif choice == "18":
            print("Advanced Mass conversion selected.")
            value = float(input("Enter the value: "))
            from_unit = input("Enter from unit: ")
            to_unit = input("Enter to unit: ")
            result = convert_mass(value, from_unit, to_unit)
            print(f"Result: {result}")

        elif choice == "19":
            print("Advanced Time conversion selected.")
            value = float(input("Enter the value: "))
            from_unit = input("Enter from unit: ")
            to_unit = input("Enter to unit: ")
            result = convert_time(value, from_unit, to_unit)
            print(f"Result: {result}")

        elif choice == "20":
            print("Advanced Density conversion selected.")
            value = float(input("Enter the value: "))
            from_unit = input("Enter from unit: ")
            to_unit = input("Enter to unit: ")
            result = convert_density(value, from_unit, to_unit)
            print(f"Result: {result}")

        elif choice == "21":
            print("Advanced Force conversion selected.")
            value = float(input("Enter the value: "))
            from_unit = input("Enter from unit: ")
            to_unit = input("Enter to unit: ")
            result = convert_force(value, from_unit, to_unit)
            print(f"Result: {result}")

        elif choice == "22":
            print("Advanced Data conversion selected.")
            value = float(input("Enter the value: "))
            from_unit = input("Enter from unit: ")
            to_unit = input("Enter to unit: ")
            result = convert_data(value, from_unit, to_unit)
            print(f"Result: {result}")

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
