import json
import pandas as pd
# Read the data from file, # We now have a Python dictionary
with open('first.json') as f:
    data_listofdict = json.load(f)
# We can do the same thing with pandas
data_df = pd.read_json('first.json', orient='records')
# We can write a dictionary to JSON like so, # Use 'indent' and 'sort_keys' to make the JSON, # file look nice
with open('new_data1.json', 'w+') as json_file:
    json.dump(data_listofdict, json_file, indent=4, sort_keys=True)
# And again the same thing with pandas
export = data_df.to_json('new_data2.json', orient='records')