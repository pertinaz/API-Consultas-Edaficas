import pandas as pd
from sodapy import Socrata
import json
import tkinter as tk
from tkinter import ttk
from tkinter import *

client = Socrata("www.datos.gov.co",None)

dataset_id ="ch4u-f3i5"
results = client.get(dataset_id, limit="10000") #Limite estático para no generar un fallo por sobrecarga de datos

# Convert to pandas DataFrame
results_df=pd.DataFrame.from_records(results)

with open('QueryResults.json','w') as file:
    json.dump(results,file)

with open('QueryResults.json','r') as file:
    QueryResults = json.load(file)
