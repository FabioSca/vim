
import openpyxl

# aprire l'Excel file (ad esempio, "italy_2024.xlsx")
wb = openpyxl.load_workbook("italy_2024.xlsx")

# ottenere la riga attualmente selezionata
selta = wb['Sheet1'].active

# scrivere il messaggio di output
print("La riga attualmente selezionata è: ", selta.value)

# scrivere i italy_2024 della riga in un file nuovo
with open('italy_2024_new.xlsx', 'w') as f:
    for row in selta.rows:
        f.write(str(row.value) + "\n")
