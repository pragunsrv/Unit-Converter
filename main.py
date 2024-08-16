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
        "angstroms": 1e-10,
        "rods": 5.0292,
        "chains": 20.1168,
        "cubits": 0.4572,
        "spans": 0.2286,
        "hands": 0.1016,
        "palms": 0.0762,
        "links": 0.201168,
        "twips": 1.7638888889e-5,
        "picas": 0.0042175176,
        "points": 0.0003527778,
        "astronomical leagues": 4.828e12,
        "cubits ancient": 0.524,
        "inches roman": 0.0246,
        "li chinese": 500.0,
        "feet greek": 0.308,
        "paces": 1.524,
        "ell": 1.143,
        "spanish feet": 0.278635,
        "rope": 20.1168,
        "cubit biblical": 0.4572,
        "stadion": 192.27,
        "gerah": 0.0001
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
        "grains": 0.06479891,
        "scruples": 1.2959782,
        "drams": 1.7718451953125,
        "apothecaries ounces": 31.1034768,
        "pennyweights": 1.55517384,
        "troy ounces": 31.1034768,
        "metric tons": 1e6,
        "slugs": 14593.903,
        "quintals": 100000.0,
        "hundredweights": 50802.34544,
        "quarters": 12700.58636,
        "grains troy": 0.06479891,
        "poundals": 14.593903,
        "scruples apothecary": 1.2959782,
        "bales": 40000.0,
        "talents": 26000.0,
        "shekels": 11.34,
        "pyramids": 53592.0,
        "chinese pounds": 453.6,
        "candareens": 0.37793,
        "mommes": 3.75,
        "taels": 37.5,
        "stone uk": 6350.29318,
        "ounces uk": 28.3495231,
        "tons uk": 1016046.9088
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
    elif from_unit == "celsius" and to_unit == "reaumur":
        return value * 4/5
    elif from_unit == "fahrenheit" and to_unit == "reaumur":
        return (value - 32) * 4/9
    elif from_unit == "kelvin" and to_unit == "reaumur":
        return (value - 273.15) * 4/5
    elif from_unit == "rankine" and to_unit == "reaumur":
        return (value - 491.67) * 4/9
    elif from_unit == "delisle" and to_unit == "reaumur":
        return (100 - value * 5/4) * 3/2
    elif from_unit == "reaumur" and to_unit == "celsius":
        return value * 5/4
    elif from_unit == "reaumur" and to_unit == "fahrenheit":
        return (value * 9/4) + 32
    elif from_unit == "reaumur" and to_unit == "kelvin":
        return (value * 5/4) + 273.15
    elif from_unit == "reaumur" and to_unit == "rankine":
        return (value * 9/4) + 491.67
    elif from_unit == "reaumur" and to_unit == "delisle":
        return (100 - value * 5/4) * 3/2
    elif from_unit == "kelvin" and to_unit == "newton":
        return (value - 273.15) * 0.33
    elif from_unit == "newton" and to_unit == "kelvin":
        return value * 100/33 + 273.15
    elif from_unit == "fahrenheit" and to_unit == "newton":
        return (value - 32) * 0.18333
    elif from_unit == "newton" and to_unit == "fahrenheit":
        return value * 100/33 * 1.8 + 32
    elif from_unit == "celsius" and to_unit == "newton":
        return value * 0.33
    elif from_unit == "newton" and to_unit == "celsius":
        return value * 100/33
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
        "acres ancient": 4046.8564224
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
        "fluid drams": 0.0343613
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
        "light years per millennium": 9.461e12,
        "fathoms per minute": 0.03048
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
        "fortnights": 1209600.0,
        "months": 2.63e6,
        "years": 3.154e7,
        "decades": 3.154e8,
        "centuries": 3.154e9,
        "millennia": 3.154e10,
        "plank time": 5.39e-44,
        "shakes": 1e-8,
        "jiffies": 0.01,
        "microfortnights": 1.2096,
        "femtoseconds": 1e-15,
        "picoseconds": 1e-12,
        "nanoseconds": 1e-9,
        "microseconds": 1e-6,
        "milliseconds": 1e-3,
        "centiseconds": 1e-2,
        "decaseconds": 10.0,
        "hectoseconds": 100.0,
        "kiloseconds": 1000.0
    }
    if from_unit in units and to_unit in units:
        return value * (units[to_unit] / units[from_unit])
    else:
        return None

def convert_energy(value, from_unit, to_unit):
    units = {
        "joules": 1.0,
        "kilojoules": 1000.0,
        "calories": 4.184,
        "kilocalories": 4184.0,
        "watt-hours": 3600.0,
        "kilowatt-hours": 3.6e6,
        "ergs": 1e-7,
        "british thermal units": 1055.06,
        "foot-pounds": 1.35582,
        "electronvolts": 1.60218e-19,
        "tons of tnt": 4.184e9,
        "therms": 1.05506e8,
        "horsepower-hours": 2.68452e6,
        "joules per kilogram": 1.0,
        "kilojoules per kilogram": 1000.0,
        "calories per gram": 4.184,
        "calories per kilogram": 4184.0,
        "british thermal units per pound": 2326.0,
        "tonnes of tnt": 4.184e12,
        "kilotons of tnt": 4.184e15,
        "megatons of tnt": 4.184e18,
        "gigatons of tnt": 4.184e21,
        "teratons of tnt": 4.184e24,
        "petatons of tnt": 4.184e27,
        "exatons of tnt": 4.184e30,
        "zettatons of tnt": 4.184e33,
        "yottatons of tnt": 4.184e36,
        "joules per mole": 1.0,
        "kilojoules per mole": 1000.0,
        "calories per mole": 4.184,
        "kilocalories per mole": 4184.0
    }
    if from_unit in units and to_unit in units:
        return value * (units[to_unit] / units[from_unit])
    else:
        return None

def convert_pressure(value, from_unit, to_unit):
    units = {
        "pascals": 1.0,
        "kilopascals": 1000.0,
        "bar": 100000.0,
        "atmospheres": 101325.0,
        "millimeters of mercury": 133.322,
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
        "kilocalories per hour": 1500.0
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
        "solar panel voltage": 36.0
    }
    if from_unit in units and to_unit in units:
        return value * (units[to_unit] / units[from_unit])
    else:
        return None

def convert_current(value, from_unit, to_unit):
    units = {
        "amperes": 1.0,
        "milliamperes": 0.001,
        "microamperes": 1e-6,
        "nanoamperes": 1e-9,
        "picoamperes": 1e-12,
        "kiloamperes": 1000.0,
        "megaamperes": 1e6,
        "gigaamperes": 1e9,
        "centiamperes": 0.01,
        "deciamperes": 0.1,
        "decaamperes": 10.0,
        "hectoamperes": 100.0,
        "ampere-hours": 3600.0,
        "milliampere-hours": 3.6,
        "microampere-hours": 3.6e-3,
        "ampere-seconds": 1.0,
        "milliampere-seconds": 0.001,
        "microampere-seconds": 1e-6,
        "coulombs": 1.0,
        "electric current": 1.0,
        "current density": 1.0,
        "magnetomotive force": 1.0,
        "electric charge": 1.0
    }
    if from_unit in units and to_unit in units:
        return value * (units[to_unit] / units[from_unit])
    else:
        return None
