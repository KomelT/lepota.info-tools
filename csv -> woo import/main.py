#!/usr/bin/python

import sys
import csv
import os
import re

# Modules to process different lines
from modules.Iam import iam
from modules.Other import other

VALUES_DELIMITER = ","
STRING_DELIMITER = '"'

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

os.system('rm -r files/out/*')

csv_data = ""
with open(sys.argv[2]) as csv_file:
    csv_reader = csv.reader(
        csv_file, delimiter=VALUES_DELIMITER, doublequote=STRING_DELIMITER)

    # Call function ta parse CSV data
    if sys.argv[1] == "iam":
        csv_data = iam(csv_reader)
    elif sys.argv[1] == "other":
        csv_data = other(csv_reader)

    os.system("echo > debug.txt")


fieldnames = ["naziv", "kratkiO", "opis", "proizvajalec", "orgLink", "kategorije", "kategorije2", "cena", "skrij",
              "slike", "navodila", "opozorila", "sestavine", "odgOseba", "certifikati", "video", "barva", "volumen"]

with open('output.csv', 'w') as f:
    writer = csv.writer(f, delimiter=VALUES_DELIMITER,
                        doublequote=STRING_DELIMITER)
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()

    rows = []

    for prod in csv_data:

        # Add space between value and unit, if it is missing.
        x = re.findall("([0-9]+)([A-z]+)", prod.volumen)
        if len(x) == 1:
            prod.volumen = str(prod.volumen).replace(
                x[0][0], str(x[0][0]) + " ")

        rows.append({
            fieldnames[0]: prod.naziv,
            fieldnames[1]: prod.kratkiO,
            fieldnames[2]: prod.opis,
            fieldnames[3]: prod.proizvajalec,
            fieldnames[4]: prod.orgLink,
            fieldnames[5]: prod.kategorije,
            fieldnames[6]: prod.kategorije2,
            fieldnames[7]: prod.cena,
            fieldnames[8]: prod.skrij,
            fieldnames[9]: prod.slike,
            fieldnames[10]: prod.navodila,
            fieldnames[11]: prod.opozorila,
            fieldnames[12]: prod.sestavine,
            fieldnames[13]: prod.odgOseba,
            fieldnames[14]: prod.certifikati,
            fieldnames[15]: prod.video,
            fieldnames[16]: prod.barva,
            fieldnames[17]: prod.volumen
        })

    writer.writerows(rows)
