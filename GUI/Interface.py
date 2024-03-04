import tkinter as tk
from tkinter import *
from tkinter import ttk
import customtkinter

# System settings and app frame 
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")
customtkinter.deactivate_automatic_dpi_awareness()


"""
("Departamento","Municipio","Cultivo","Topologia","pH del agua","Fósforo (P)","Potasio(K)")
"""

# New window with the Query data 
class Query(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x300")
        self.title("Consulta por departamento")
        self.label = customtkinter.CTkLabel(self, text="Consulta por departamento")
        self.label.pack(padx=20, pady=20)

        #Display treeView with the API data
        data = ttk.Treeview(self,columns=("Departamento","Municipio","Cultivo","Topografia","pH","Fósforo","Potasio"), show='headings')
        data.heading("Departamento",text="Departamento")
        data.heading("Municipio",text="Municipio")
        data.heading("Cultivo",text="Cultivo")
        data.heading("Topofrafia",text="Topografia")
        data.heading("pH",text="pH del agua")
        data.heading("Fósforo",text="Fósforo (p) ")
        data.heading("Potasio",text="Potasio (K) ")

        #Automation of data Query
        data.insert("",END,text="",values=("Aqui va el departamento","Aqui va el municipio","Aqui va el cultivo","Aqui va la topografia","Aqui va el PH del agua","Aqui va el Fosforo","Aqui va el potasio"))

        data.place(y=300)
        data.pack(padx=10,pady=10)

        
        

# Create de Graphic User interface for the main menu
class Interface(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x600")
        self.title("Edaficas Risaralda")

        # Main menu 
        departamento = customtkinter.CTkEntry(self, placeholder_text="Departamento")
        departamento.pack(padx=10,pady=10)

        municipio = customtkinter.CTkEntry(self,placeholder_text="Municipio")
        municipio.pack(padx=10,pady=10)

        cultivo = customtkinter.CTkEntry(self,placeholder_text="Cultivo")
        cultivo.pack(padx=10,pady=10)

        limit = customtkinter.CTkEntry(self,placeholder_text="Limite consulta")
        limit.pack(padx=10,pady=10)

        #Query button
        self.button = customtkinter.CTkButton(self, text="Hacer consulta", command=self.openQuery)
        self.button.pack(side="top", padx=20, pady=20)

        self.dataQueryWindow = None
         
    #Open new query window triggered by button above
    def openQuery(self): 
        if self.dataQueryWindow is None or not self.dataQueryWindow.winfo_exists():
            self.dataQueryWindow = Query(self)  # create window if its None or destroyed
        else:
            self.dataQueryWindow.focus()  # if window exists focus it

# Run the app
self = Interface()
self.mainloop()
