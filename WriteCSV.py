import csv
# Field names
fields = ['Name', 'Goals', 'Assists', 'Shots']
# Rows of data in the csv file
rows = [['Emily', '12', '18', '112'],
        ['Katie', '8', '24', '96'],
        ['John', '16', '9', '101'],
        ['Mike', '3', '14', '82']]
filename = "soccer.csv"
# Writing to csv file
with open(filename, 'w+') as csvfile:
    # Creating a csv writer object
    csvwriter = csv.writer(csvfile)
    # Writing the fields
    csvwriter.writerow(fields)
    # Writing the data rows
    csvwriter.writerows(rows)