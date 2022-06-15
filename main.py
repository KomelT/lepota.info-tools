#!/usr/bin/python

import sys

if len(sys.argv) <= 1:
    print("ERROR: File path is missing!")
    exit(1)

try:
    f = open(sys.argv[1])
except Exception as e:
    print(e)
    exit(1)

if f.name.split(".")[-1] != "csv":
    print("ERROR: File ending is not .csv!")
    exit(1)
