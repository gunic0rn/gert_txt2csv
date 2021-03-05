import csv

with open("codes.txt", 'r') as infile, open("codes.csv", 'w') as outfile:
        stripped = (line.strip() for line in infile)
        lines = (line.split(" ") for line in stripped if line)
        writer = csv.writer(outfile)
        writer.writerows(lines)
