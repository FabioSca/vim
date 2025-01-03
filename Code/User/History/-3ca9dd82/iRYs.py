
import openpyxl
import os 

print(os.listdir())

# aprire l'Excel file (ad esempio, "italy_2024.xlsm")
wb = openpyxl.load_workbook("italy__2024.xlsm")

# ottenere la riga attualmente selezionata
ws  = wb['ServiceItaly'].active_cell

#print(dir(ws))

""""
# scrivere il messaggio di output
print("La riga attualmente selezionata è: ", selta )

# scrivere i italy_2024 della riga in un file nuovo
with open('italy_2024_new.xlsx', 'w') as f:
    for row in selta.rows:
        f.write(str(row.value) + "\n")
"""