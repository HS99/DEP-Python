import csv
filename = 'Iris.csv'
fields = []
rows = []
# Reading csv file
with open(filename, 'r') as csvfile:
    # Creating a csv reader object
    csvreader = csv.reader(csvfile, delimiter=',', quotechar='"', skipinitialspace=True)
    # Extracting field names in the first row
    fields = next(csvreader)
    # Extracting each data row one by one
    for row in csvreader:
        rows.append(row)
# Printing out the first 5 rows
for row in rows[:5]:
    print(row)