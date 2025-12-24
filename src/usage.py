import sys

hourly = """main.py hourly [VARIABLES]
        Presents weather information by the hour of the next 7 days
        VARIABLES  Specify what information to display as variables (default VARIABLES=precipitation_percentage)
        all seperated by commas only"""

hourly_vars = """        - precipitations percentage"""

daily = """main.py daily [VARIABLES]
        Presents weather information by the day for the next 7 days
        VARIABLES  Specify what information to display as variables (default VARIABLES=sunrise,sunset)
        all seperated by commans only"""

daily_vars = """        - sunrise
        - sunset"""

def usage(error=None, tool=None):

    # print any error message as requested
    if error is not None:
        print(f"Error: {error}\n", file=sys.stderr)

    if tool == "hourly":
        print(f"{hourly}", file=sys.stderr)
    elif tool == "daily":
        print(f"{daily}", file=sys.stderr)
    else:
        print(
            "\nWeather Forecast Options:\n=========================",
            hourly,
            hourly_vars,
            daily,
            daily_vars,
            sep="\n\n",
            end="\n\n",
            file=sys.stderr)

    sys.exit(1)
