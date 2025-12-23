# Main Plan

The plan for implementing user control to the main file, focusing on implementing the new usage tool

Phase 0: Requirements Analysis
------------------------------
The most basic functionality of the main file, that is getting access to the API through helper
functions is already in place. This plan is meant to outline the next step, enabling user control
through the `sys` module and utilizing the usage tools recently created.

For now I will only allow the user the option of accessing the daily tool with the sunrise and
sunset variables. After I get this working, I will focus on creating the hourly tool as a
secondary segment of this document.

The user must be able to include one, both, or neither of the variables in the daily tool to
display information. If the user gives no variable for the daily tool, it will automatically call
all of the information--that currently being sunrise and sunset--to display for the user. The
program must be able to raise an error if the variable given does not exist along with a helpful
tip.

**What I know how to do:**
-   raise errors for non-existent variables.
-   check for and use different system arguments
-   have an automatic response in the case of no variables (it should already be implemented as defaults in the other files)

**What I don't know how to do:**

Phase 1: Design
---------------
The main file at this stage should look a little something like this:
```
imports:
json, sys, usage, get_data, clean (clean_data, fix_times)

function: main
input: None
output: JSON data structure
===========================
check if the only arguments given are the call of the main file
    if so, call usage with no args to display helpful tip

if there is more arguments than the main file
    if the forecarst specifier isn't daily, display a usage message
    if there is another argument after the forecast specifier
        check that any more arguments are viable variables (for now either sunset or sunrise)
        place the arguments into the correct functions
    display the default parametered message

convert and return the data in a json structure
===========================

call main and get the object
print the object for testing sake
```
