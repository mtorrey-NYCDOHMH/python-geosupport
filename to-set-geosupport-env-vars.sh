#!/bin/bash
# Last modified: 2025-04-10 14:30
# this file: to-set-geosupport-env-vars.sh

########################################
# This file is a wrapper script that sets env vars and calls a python
# script that uses those vars
#
# Explanation:
# Geosupport uses these variables to link a library to python, and it
# can't do that if python is already started without the libraries linked.
# So you _have_ to set the environment variables in bash _before_ you
# start python. Therefore you need some kind of wrapper script that sets
# the vars and _then_ calls your python script.
########################################

printf ("Setting GEOFILES and LD_LIBRARY_PATH environment variables...\n")
export export LD_LIBRARY_PATH=/usr/share/R/library/geocoding_tests/version-24d_24.4/lib/
export export GEOFILES=/usr/share/R/library/geocoding_tests/version-24d_24.4/fls/
printf("Running python geocoding script...\n")
exec python3 MT-python-geosupport-test-stuff.py "$@"


