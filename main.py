def convert_temperature(value, from_unit, to_unit):
    if from_unit == "celsius" and to_unit == "fahrenheit":
        return value * 9/5 + 32
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
    elif from_unit == "rankine" and to_unit == "celsius":
        return (value - 491.67) * 5/9
    elif from_unit == "fahrenheit" and to_unit == "rankine":
        return value + 459.67
    elif from_unit == "rankine" and to_unit == "fahrenheit":
        return value - 459.67
    elif from_unit == "kelvin" and to_unit == "rankine":
        return value * 9/5
    elif from_unit == "rankine" and to_unit == "kelvin":
        return value * 5/9
    elif from_unit == "celsius" and to_unit == "delisle":
        return (100 - value) * 3/2
    elif from_unit == "delisle" and to_unit == "celsius":
        return 100 - value * 2/3
    elif from_unit == "fahrenheit" and to_unit == "delisle":
        return (212 - value) * 5/6
    elif from_unit == "delisle" and to_unit == "fahrenheit":
        return 212 - value * 6/5
    elif from_unit == "kelvin" and to_unit == "delisle":
        return (373.15 - value) * 3/2
    elif from_unit == "delisle" and to_unit == "kelvin":
        return 373.15 - value * 2/3
    elif from_unit == "rankine" and to_unit == "delisle":
        return (671.67 - value) * 5/6
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
        "square miles": 2.59e6,
        "acres": 4046.86,
        "hectares": 10000.0,
        "square yards": 0.836127,
        "square feet": 0.092903,
        "square inches": 0.00064516,
        "square micrometers": 1e-12,
        "square nanometers": 1e-18,
        "square picometers": 1e-24,
        "square rods": 25.2929,
        "square furlongs": 404685.64224,
        "square leagues": 2.591e12,
        "square chains": 404.68564224,
        "ares": 100.0,
        "square perches": 25.2929,
        "circular inches": 0.0005067075,
        "homesteads": 647497.027584,
        "sections": 2.58998811e6,
        "roods": 1011.7141056,
        "virgates": 12000.0,
        "oxgangs": 12000.0,
        "square decimeters": 0.01,
        "square decameters": 100.0,
        "square hectometers": 10000.0,
        "acres ancient": 4046.8564224,
        "circular millimeters": 7.854e-10,
        "square solar systems": 2.78e29,
        "square light years": 8.464e35,
        "square parsecs": 2.612e36,
        "square astronomical units": 2.77e23,
        "square kiloparsecs": 6.7e41,
        "square megaparsecs": 4.49e49,
        "square gigaparsecs": 2.47e57,
        "square teraparsecs": 1.52e65
    }
    if from_unit in units and to_unit in units:
        return value * (units[to_unit] / units[from_unit])
    else:
        return None

def convert_volume(value, from_unit, to_unit):
    units = {
        "liters": 1.0,
        "milliliters": 0.001,
        "cubic meters": 1000.0,
        "cubic centimeters": 0.001,
        "cubic millimeters": 1e-6,
        "cubic inches": 0.0163871,
        "cubic feet": 28.3168,
        "cubic yards": 764.555,
        "cubic miles": 4.168e12,
        "cubic nautical miles": 3.43e12,
        "cubic light years": 8.467e47,
        "cubic parsecs": 2.938e49,
        "teaspoons": 0.00492892,
        "tablespoons": 0.0147868,
        "fluid ounces": 0.0295735,
        "cups": 0.24,
        "pints": 0.473176,
        "quarts": 0.946353,
        "gallons": 3.78541,
        "barrels": 158.987,
        "hogsheads": 238.481,
        "firkins": 34.318,
        "puncheons": 477.703,
        "butts": 636.503,
        "tuns": 953.506,
        "cords": 3624.556,
        "drams": 3.69669,
        "gills": 0.118294,
        "shots": 0.0443603,
        "gills uk": 0.142065,
        "fluid ounces uk": 0.0284131,
        "tablespoons uk": 0.0177582,
        "teaspoons uk": 0.00591939,
        "fluid scruples": 0.0028413,
        "fluid drams": 0.0343613,
        "liters per minute": 1.0,
        "cubic meters per hour": 1000.0,
        "milliliters per second": 0.001,
        "barrels per day": 158.987,
        "gallons per minute": 3.78541,
        "cups per hour": 0.24,
        "pints per second": 0.473176,
        "teaspoons per second": 0.00492892,
        "fluid ounces per hour": 0.0295735,
        "kiloliters per year": 1e3,
        "milliliters per year": 1e-3,
        "cubic centimeters per minute": 0.001,
        "deciliters per day": 0.1,
        "centiliters per second": 0.01
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
        "knots": 0.514444,
        "feet per second": 0.3048,
        "inches per second": 0.0254,
        "mach": 340.29,
        "speed of light": 299792458.0,
        "parsecs per second": 3.086e16,
        "leagues per hour": 0.0003086,
        "furlongs per fortnight": 0.0001663,
        "cubits per second": 0.4572,
        "chains per hour": 0.0127,
        "links per hour": 0.00127,
        "hands per second": 0.1016,
        "paces per second": 0.762,
        "light years per millennium": 9.4607e12,
        "astronomical units per century": 1.5e12,
        "gigameters per year": 3.154e19,
        "terameters per decade": 3.154e16,
        "fathoms per minute": 0.18288,
        "roods per day": 0.0001454,
        "stadia per hour": 0.009144,
        "sverdrups per year": 3.154e9,
        "gallons per minute": 0.227,
        "cups per second": 0.06,
        "hectometers per second": 0.01,
        "kilometers per minute": 0.0166667,
        "megameters per year": 3.154e15,
        "parsecs per day": 2.659e13,
        "light minutes per hour": 0.0010793,
        "tangents per hour": 0.004,
        "knots per hour": 0.514444,
        "mph per day": 0.44704
    }
    if from_unit in units and to_unit in units:
        return value * (units[to_unit] / units[from_unit])
    else:
        return None

def convert_pressure(value, from_unit, to_unit):
    units = {
        "pascals": 1.0,
        "kilopascals": 1000.0,
        "megapascals": 1e6,
        "gigapascals": 1e9,
        "bar": 1e5,
        "atmospheres": 101325.0,
        "torr": 133.322,
        "inches of mercury": 3396.98,
        "pounds per square inch": 6894.76,
        "kgf per square centimeter": 98066.5,
        "newtons per square meter": 1.0,
        "dynes per square centimeter": 0.001,
        "pounds per square foot": 4788.02,
        "kgf per square meter": 9.80665,
        "newtons per square centimeter": 100000.0,
        "newtons per square millimeter": 1e6,
        "pascals per square millimeter": 1e6,
        "pascals per square inch": 6894.76,
        "barometric pressure": 101325.0,
        "centimeters of water": 98.0665,
        "inches of water": 249.088,
        "millibars": 100.0,
        "hectopascals": 100.0,
        "newtons per square foot": 4788.02,
        "inches of water": 249.088,
        "centimeters of mercury": 133.322,
        "inches of mercury": 3396.98,
        "pounds per square inch": 6894.76,
        "kgf per square centimeter": 98066.5,
        "newtons per square meter": 1.0,
        "dynes per square centimeter": 0.001,
        "pounds per square foot": 4788.02,
        "kgf per square meter": 9.80665,
        "newtons per square centimeter": 100000.0,
        "newtons per square millimeter": 1e6,
        "pascals per square millimeter": 1e6,
        "pascals per square inch": 6894.76,
        "barometric pressure": 101325.0,
        "centimeters of water": 98.0665,
        "inches of water": 249.088,
        "millibars": 100.0,
        "hectopascals": 100.0
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
        "foot-pounds per second": 1.35582,
        "calories per second": 4.184,
        "kilocalories per second": 4184.0,
        "joules per second": 1.0,
        "ergs per second": 1e-7,
        "watt-hours per day": 86400.0,
        "watt-hours per year": 8766000.0,
        "kilowatt-hours per day": 86.4,
        "kilowatt-hours per year": 8766.0,
        "megawatt-hours per day": 0.0864,
        "megawatt-hours per year": 8.766,
        "gigawatt-hours per day": 0.0000864,
        "gigawatt-hours per year": 0.031536,
        "horsepower-hours per day": 16725.0,
        "horsepower-hours per year": 6112125.0,
        "foot-pounds per minute": 81.49,
        "calories per hour": 150.0,
        "kilocalories per hour": 1500.0,
        "watts per square meter": 1.0,
        "kilowatts per square meter": 0.001,
        "megawatts per square meter": 1e-6,
        "gigawatts per square meter": 1e-9,
        "terawatts per square meter": 1e-12,
        "joules per square meter": 1.0,
        "ergs per square meter": 1e-7,
        "foot-pounds per square meter": 1.35582,
        "calories per square meter": 4.184,
        "kilocalories per square meter": 4184.0,
        "horsepower per unit area": 745.7,
        "watts per unit volume": 1.0,
        "kilowatts per unit volume": 0.001,
        "megawatts per unit volume": 1e-6,
        "gigawatts per unit volume": 1e-9,
        "terawatts per unit volume": 1e-12
    }
    if from_unit in units and to_unit in units:
        return value * (units[to_unit] / units[from_unit])
    else:
        return None

def convert_voltage(value, from_unit, to_unit):
    units = {
        "volts": 1.0,
        "millivolts": 0.001,
        "kilovolts": 1000.0,
        "megavolts": 1e6,
        "microvolts": 1e-6,
        "nanovolts": 1e-9,
        "picovolts": 1e-12,
        "statvolts": 299.792458,
        "abvolts": 1e-8,
        "centivolts": 0.01,
        "decivolts": 0.1,
        "decalvolts": 10.0,
        "hectovolts": 100.0,
        "kilovolt-meters": 1000.0,
        "volt-amperes": 1.0,
        "volt-coulombs": 1.0,
        "volt-seconds": 1.0,
        "electromotive force": 1.0,
        "electrostatic potential": 1.0,
        "battery voltage": 1.5,
        "car battery voltage": 12.0,
        "solar panel voltage": 36.0,
        "volts per meter": 1.0,
        "kilovolts per meter": 1000.0,
        "megavolts per meter": 1e6,
        "microvolts per meter": 1e-6,
        "nanovolts per meter": 1e-9,
        "picovolts per meter": 1e-12,
        "volt per unit length": 1.0,
        "kilovolt per unit length": 1000.0,
        "megavolt per unit length": 1e6,
        "microvolt per unit length": 1e-6,
        "nanovolt per unit length": 1e-9,
        "picovolt per unit length": 1e-12,
        "volts per square meter": 1.0,
        "kilovolts per square meter": 1000.0,
        "megavolts per square meter": 1e6,
        "microvolts per square meter": 1e-6,
        "nanovolts per square meter": 1e-9,
        "picovolts per square meter": 1e-12,
        "volts per unit volume": 1.0,
        "kilovolts per unit volume": 1000.0,
        "megavolts per unit volume": 1e6,
        "microvolts per unit volume": 1e-6,
        "nanovolts per unit volume": 1e-9,
        "picovolts per unit volume": 1e-12
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
        "gigajoules per hour": 3.6e12
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
        print("Select conversion type:")
        print("1. Temperature")
        print("2. Area")
        print("3. Volume")
        print("4. Speed")
        print("5. Pressure")
        print("6. Power")
        print("7. Voltage")
        print("8. Energy")
        print("9. Frequency")
        print("0. Exit")
        
        choice = input("Enter choice (0-9): ")
        
        if choice == "0":
            break
        
        value = float(input("Enter value to convert: "))
        from_unit = input("Enter from unit: ").lower()
        to_unit = input("Enter to unit: ").lower()
        
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
