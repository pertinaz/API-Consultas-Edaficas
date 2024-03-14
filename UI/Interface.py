import pandas as pd


def requestedInformation():
    department = input("Ingrese departamento: ")
    department = department.upper()

    municipality = input("Ingrese municipio: ")
    municipality = municipality.upper()

    crop = input("Ingrese cultivo: ")
    crop = crop.capitalize()

    limit = int(input("Ingrese limite: "))
    if limit < 0 or limit >=1000: print("Limite excedido")
    return department,municipality,crop,limit

def ShowFilteredInformation(results_df):
    print("Resultados de su busqueda")
    print(results_df[['departamento','municipio','cultivo','topografia']])
    

def calculateTheMedian(results_df, column):
    if results_df.empty:
        print("No hay datos filtrados parra calcular la mediana.")
        return
    results_df[column] = pd.to_numeric(results_df[column], errors='coerce')

    median = results_df[column].median()
    print(f"La mediana de '{column}' para todos los datos filtrados es: '{median}'")

def phMedian(results_df):
    ph = 'ph_agua_suelo_2_5_1_0'
    calculateTheMedian(results_df,ph)

def matchMedian(results_df):
    match = 'f_sforo_p_bray_ii_mg_kg'
    calculateTheMedian(results_df,match)

def potassiumMedian(results_df):
    potassium = 'potasio_k_intercambiable_cmol_kg'
    calculateTheMedian(results_df,potassium)
