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
def convert_frequency_(value, from_unit, to_unit):
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
        "cpm": 0.0166667,
        "hz": 1.0,
        "kHz": 1e3,
        "MHz": 1e6,
        "GHz": 1e9,
        "THz": 1e12,
        "rotations per minute": 0.0166667,
        "vibrations per second": 1.0,
        "oscillations per minute": 0.0166667,
        "pulses per minute": 0.0166667,
        "sound waves per second": 1.0,
        "sound waves per minute": 0.0166667,
        "cycles per hour": 0.000277778,
        "oscillations per hour": 0.000277778,
        "hertz per hour": 0.000277778,
        "kilohertz per hour": 0.277778,
        "megahertz per hour": 277.778,
        "gigahertz per hour": 277778.0
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
        choice = input("Enter your choice: ")
        if choice == "10":
            break
        
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

if __name__ == "__main__":
    main()
