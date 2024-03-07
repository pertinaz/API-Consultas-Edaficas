import tkinter as tk
from tkinter import *
from tkinter import ttk
import customtkinter
import json


# System settings and app frame 
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")
customtkinter.deactivate_automatic_dpi_awareness()

#load the json file into the interface and add it to the table
with open('QueryResults.json','r') as file:
    QueryResults = json.load(file)




# New window with the Query data 
class Query(customtkinter.CTkToplevel):
    def __init__(self, *args, coincidencias=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x300")
        self.title("Consulta por departamento")
        self.iconbitmap('icon.ico')

        #Display treeView with the API data
        data = ttk.Treeview(self,columns=("KEY","VALUE"), show='headings')

        data.heading("KEY",text="Caracteristica")
        data.heading("VALUE",text="Valores")
        
        #Filter only the info we need to show
        keys = ["departamento","municipio","cultivo","topografia","ph_agua_suelo_2_5_1_0","f_sforo_p_bray_ii_mg_kg","potasio_k_intercambiable_cmol_kg"]

        if coincidencias:
            for lista in QueryResults:
                for key, value in lista.items():
                    if key in keys:
                        keyStr = str(key)
                        valueStr = str(value)
                        data.insert("","end",values = (keyStr,valueStr))
                data.insert("","end",text="")

       
        
        data.pack(expand=True, fill="both")

        
        

# Create the Graphic User interface for the main menu
class Interface(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x400")
        self.title("Edaficas Risaralda")
        self.iconbitmap('icon.ico')



        # Main menu 
        departament = customtkinter.CTkEntry(self,placeholder_text="DEPARTAMENTO")
        departament.pack(padx=10,pady=10)

        

        municipality = customtkinter.CTkEntry(self,placeholder_text="MUNICIPIO")
        municipality.pack(padx=10,pady=10)

        crop = customtkinter.CTkEntry(self,placeholder_text="CULTIVO")
        crop.pack(padx=10,pady=10)

        limit = customtkinter.CTkEntry(self,placeholder_text="LIMITE CONSULTA")
        limit.pack(padx=10,pady=10)

        #Query button
        self.button = customtkinter.CTkButton(self, text="CONSULTAR", command=self.openQuery)
        self.button.pack(side="top", padx=20, pady=20)

        self.dataQueryWindow = None
         
    #Open new query window triggered by button above
    def openQuery(self): 

        #Get the entry inputs 
        departamento = self.departament.get()
        municipio = self.municipality.get()
        cultivo = self.crop.get()
        limite = self.limit.get()

        #Storage the entrys
        coincidencias = []

        for entry in QueryResults: 
            if departamento == entry.get("departamento") and municipio == entry.get("municipio") and cultivo == entry.get("cultivo"):
                coincidencias.append(entry)
            #Limit coincidences
            if limite and len(coincidencias) >= int(limite):
                break

        if self.dataQueryWindow is None or not self.dataQueryWindow.winfo_exists():
            self.dataQueryWindow = Query(self)  # create window if its None or destroyed
        else:
            self.dataQueryWindow.focus()  # if window exists focus it

# Run the app
self = Interface()
self.mainloop()