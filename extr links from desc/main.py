#!/usr/bin/python

import sys
import csv
import os
import re


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

csv_data = ""
print(sys.argv[1])
with open(sys.argv[1]) as csv_file:
    csv_reader = csv.reader(
        csv_file, delimiter=VALUES_DELIMITER, doublequote=STRING_DELIMITER)

    os.system("echo > debug.txt")

    link_dict = {}

    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print("")
        else:
            x = re.findall(
                "(http|ftp|https):\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-])", row[3])
            for y in x:
                tmp = "".join(y).strip()

                tmp = tmp.replace("httpswww", "https://www")
                tmp = tmp.replace("httpwww", "http://www")

                if tmp in link_dict:
                    link_dict[tmp] += 1
                else:
                    link_dict[tmp] = 1

        line_count += 1

    os.system("echo link,stevilo > output.csv")
    for x in link_dict:
        os.system('echo "'+x+'",'+str(link_dict[x])+' >> output.csv')
