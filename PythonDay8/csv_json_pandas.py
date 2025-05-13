
import pandas as pd

# Read CSV file
df = pd.read_csv('file_data_formats/input.csv')

# DataFrame to JSON
df.to_json('output_pandas.json', orient='records', lines=True)


df.to_xml('xml_pandas.xml')