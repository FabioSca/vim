
import openpyxl

# aprire l'Excel file (ad esempio, "dati.xlsx")
wb = openpyxl.load_workbook("dati.xlsx")

# ottenere la riga attualmente selezionata
selta = wb['Sheet1'].active

# scrivere il messaggio di output
print("La riga attualmente selezionata è: ", selta.value)

# scrivere i dati della riga in un file nuovo
with open('dati_new.xlsx', 'w') as f:
    for row in selta.rows:
        f.write(str(row.value) + "\n")
