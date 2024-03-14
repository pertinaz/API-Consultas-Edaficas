import ui
import api

def main():

    print("CONSULTAS EDAFICAS COLOMBIA")
    department,municipality,crop,limit = ui.requestedInformation()
    results_df = api.getResults(department,municipality,crop,limit)
    
    #Show the info
    ui.ShowFilteredInformation(results_df)

    #Show median
    ui.phMedian(results_df)
    ui.matchMedian(results_df)
    ui.potassiumMedian(results_df)



main()
