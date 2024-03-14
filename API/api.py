import pandas as pd
from sodapy import Socrata

client = Socrata("www.datos.gov.co",None)
dataset_id ="ch4u-f3i5"
results = client.get(dataset_id)

def getResults(department,municipality,crop,limit):

    results = client.get(dataset_id, where=f"departamento='{department}' AND municipio='{municipality}' AND cultivo='{crop}'", limit=limit)
    
    # Convert to pandas DataFrame
    results_df=pd.DataFrame.from_records(results)

    return results_df
