version = 0.1
TITLE = "Badanie stałych paliw rakietowych v" + str(version)
FUELS_FOLDER = 'database'
SURVEY_TYPES = {"ciśnienia i ciągu": "pressthru",
                "ciśnienia": 'press',
                "ciągu": "thrust"}
INTEGRATION_METHODS = ("rect", "trapeze", "Simpson")
CALCULATION_METHODS = ("average", "time")
SURVEY_VALUES_SEPARATOR = "    "
PRESS = "press"
THRUST = "thrust"
PRESSTHRU = "pressthru"
FORBIDDEN_NAME_SIGNS = "*.\"/[]:;|,"
