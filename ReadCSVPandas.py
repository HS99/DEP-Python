import pandas as pd
filename = "Iris.csv"
# Read in the data
data = pd.read_csv(filename)
# Print the first 5 rows
print(data.head(5))
# Write the data to file
data.to_csv("new_data.csv", sep=",", index=False)