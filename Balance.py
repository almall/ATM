import pandas as pd
from datetime import datetime

filename = 'ATM.csv'
df = pd.read_csv(filename, header = 0)
gastos = pd.DataFrame(columns=['Transacción', 'Gasto', 'Date'])
ganancias = pd.DataFrame(columns=['Transacción', 'Ganancia', 'Date'])

conteo = 0
gasto = 0
ganancia = 0

for i in range(len(df)): 
    if (df.iloc[i] ['Tipo'] == "Retirada" or df.iloc[i] ['Tipo'] == "Pago mediante BIZUM -"
    or df.iloc[i] ['Tipo'] == "Pago mediante transferencia externa -" 
    or df.iloc[i] ['Tipo'] == "Pago mediante transferencia entre cuentas -" 
    or df.iloc[i] ['Tipo'] == "Recibo bancario" or "Pago con tarjeta"):
        conteo = conteo + 1
        gastos = gastos.append({'Transacción': conteo, 'Gasto': df.iloc[i] ['Balance'], 
        'Date' : datetime.now()}, ignore_index=True)
        gasto = gasto + gastos ['Gasto']. sum ()
print(gastos)

for i in range(len(df)): 
    if (df.iloc[i] ['Tipo'] == "Depósito" or df.iloc[i] ['Tipo'] == "Pago mediante BIZUM +"
    or df.iloc[i] ['Tipo'] == "Pago mediante transferencia externa +" 
    or df.iloc[i] ['Tipo'] == "Pago mediante transferencia entre cuentas +"):
        conteo = conteo + 1
        ganancias = ganancias.append({'Transacción': conteo, 'Ganancia': df.iloc[i] ['Balance'], 
        'Date' : datetime.now()}, ignore_index=True)
        ganancia = ganancia + ganancia ['Ganancia']. sum ()
print(ganancias)

balance = ganancias - gastos
print(balance)
    