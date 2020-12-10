version = 1.0
TITLE = "Badanie stałych paliw rakietowych v" + str(version)
FUELS_FOLDER = 'database'
SURVEY_TYPES = {"ciśnienia i ciągu": "pressthru",
                "ciśnienia": 'press',
                "ciągu": "thrust"}
INTEGRATION_METHODS = {"prostokątów": 0, "trapezów": 1, "Simpsona": 2}
CALCULATION_METHODS = {"średnich": 0, "chwilowych": 1}
SURVEY_VALUES_SEPARATOR = "    "
PRESS = "press"
THRUST = "thrust"
PRESSTHRU = "pressthru"
FORBIDDEN_NAME_SIGNS = "*.\"/[]:;|,"
