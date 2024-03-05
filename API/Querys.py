import pandas as pd
from sodapy import Socrata
import json

client = Socrata("www.datos.gov.co",None)

dataset_id ="ch4u-f3i5"
results = client.get(dataset_id,departamento="RISARALDA")

# Convert to pandas DataFrame
results_df=pd.DataFrame.from_records(results)

with open('QueryResults.json','w') as file:
    json.dump(results,file)
