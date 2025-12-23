# Usage plan
The plan for the usage file to catch any errors and display helpful information

Phase 0: Requirements Analysis
------------------------------
The goal of this file is to create a tool that can be called in order to display useful information when an error occurs. A sort of "catch all".

The usage function inside this file will take two types of input, an error and a forecast time type.
Please note the inspiration for the design of this file is accredited to Prof. Falor.
The usage function will print out text according to the information provided. If an error is provided, it will print the error message; however, if a forecast type is provided, it will display the variables for that type.
Lastly, it will close the application after it's completed.

Phase 1: Design
--------------------------------
The pseudocode should look something like this:
```
global variables:
- string displaying usage message for daily variables
- string displaying usage message for hourly variables
- string displaying usage message for current weather variables

imports: sys

usage function:
input: error (default none), forecast_type (default none)
output: none
================
if an error message is provided, print the error to stderr

check for each of the forecast types
for each forcast type, display the globas variable message to stderr
if there is no argument, then display all of the usage messages

lastly, use the sys exit type 1
```

Phase 2: Implementation
------------------------
I implemented my pseudocode and only had some minor syntax typos. Implementation went well, likely thanks mainly to having a clean reference.

