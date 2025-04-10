#!/sbin/python
## MT-python-geosupport-test-stuff.py
## Last modified: 2025-04-10 14:54

print("This script tests whether geosupport is working. Environmental variables must be set before running, so be sure to use the wrapper script to-set-geosupport-env-vars.sh instead of running this script directly.")
print(" ")

## NOTE: Be sure to set environment variables first. If you are running the script on the command line, use the wrapper script, as noted in print() above.
## NOTE: Otherwise, if you are running this script interactively (or want to run it manually stand-alone on the command line), you have set the GEOFILES and LD_LIBRARY_PATH environment variables set BEFORE you start python, using ye olde export command:
    # export LD_LIBRARY_PATH=/usr/share/R/library/geocoding_tests/version-24d_24.4/lib/
    # export GEOFILES=/usr/share/R/library/geocoding_tests/version-24d_24.4/fls/

################################################################################
# An alternative for setting env vars: It is possible to set environment variables in python, but because geosupport uses the linked C libraries, you have to set the env vars and then call a separate script. So as an option (suggested by ChatGPT) you could create a small python wrapper script that set the environment variables:
#import os
#os.environ["GEOFILES"] = "/usr/share/R/library/geocoding_tests/version-24d_24.4/fls"
#os.environ["LD_LIBRARY_PATH"] = "/usr/share/R/library/geocoding_tests/version-24d_24.4/lib"
## And then calls another python script that does the actual geosupport stuff with those enviornment variables set:
#script = "MT-python-geosupport-test-stuff.py"
#args = [script] + sys.argv[1:]
#os.execve(sys.executable, [sys.executable] + args, os.environ)
## Obviously, this would not work for using python interactively.
################################################################################

########################################
# test that geosupport has it's environment variables set (and linked) and geosupport is working correctly.
import os
import sys

# Import the library and create a `Geosupport` object.
from geosupport import Geosupport, GeosupportError
# (This will fail if python-geosupport is not install correctly)

def check_geosupport_env():
    required_vars = ["LD_LIBRARY_PATH", "GEOFILES"]
    missing = [var for var in required_vars if not os.environ.get(var)]

    if missing:
        print("Content-Type: text/plain\n")
        print(f"Error: Missing required environment variable(s): {', '.join(missing)}")
        sys.exit(1)

    try:
        gtest = Geosupport()
        # Try a minimal address lookup to confirm it's working
        result = gtest.address(house_number="1", street_name="Centre St", borough="Manhattan")
        if not result or "Message" in result and "error" in result["Message"].lower():
            raise GeosupportError("Geosupport responded with error.")
        print("Geosupport environment variables checked, moving on...")
        print(" ")
    except Exception as e:
        print("Content-Type: text/plain\n")
        print(f"Error initializing Geosupport: {e}")
        sys.exit(1)

# Call the check function:
check_geosupport_env()
########################################

## Basic usage:
## This stuff from python-geosupport documentation: 
## https://python-geosupport.readthedocs.io/en/latest/
g = Geosupport()

# Call the address processing function by name
result = g.address(house_number=125, street_name='Worth St', borough_code='Mn')

## 'result' is a dictionary with the output from Geosupport.

## Calling Geosupport Functions
# python-geosupport is flexible with how you call functions. You can use
# either Geosupport function codes or human readable alternate names, and access
# them either through python object attribute notation or dictionary item
# notation:

# Different ways of calling function 3S which processes street stretches
# g.street_stretch(...)
# g['street_stretch'](...)
# g['3S'](...)
# g.call({'function': '3S', ...})
# g.call(function='3S', ...)
# You can pass arguments as a dictionary, keyword arguments.

# Use a dictionary with short names
g.street_stretch({'borough_code': 'MN', 'on': '1 Av', 'from': '1 st', 'to': '2 st'})
# Use keyword arguments with short names
g.street_stretch(borough_code='MN', street_name_1='1 Av', street_name_2='1 st', street_name_3='9 st')
# Use dictionary with full names
q.street_stretch({
    'Borough Code-1': 'MN',
    'Street Name-1': '1 Av',
    'Street Name-2': '1 st',
    'Street Name-3': '9 st'
})

## Mode
# A number of Geosupport functions support several modes: Exetended, Long, and
# TPAD Long. You can set the flags individually as you would with using
# Geosupport directly, but python-geosupport makes it easier with the mode
# argument. mode can be one of regular (default), extended, long and long+tpad.

# Call BL (Block and Lot) function in long mode
# g.BL(mode='long', ...)
# g.BL(mode='long+tpad', ...) # With TPAD

# Call 3 (Street Segment) function in extended mode
# g.street_segment(mode='extended', ...)
 
## Error handling
# See: https://python-geosupport.readthedocs.io/en/latest/errors.html

## Interactive help
# View an overview of all the functions available:
g.help()

# View help for an individual function including a description, inputs, outputs and valid modes.
g.address.help()
g.help('address')

# View a list of all possible inputs to Geosupport
g.help('input')

## Running tests
# See: https://python-geosupport.readthedocs.io/en/latest/development.html



