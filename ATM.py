import pandas as pd

balance_i = int(input("Dime la cantidad inicial: "))

print("  ATM ")
print("\n")
print("""
1)   Balance
2)   Retirada
3)   Depósito
4)   Salir
""")

df = pd.DataFrame(columns=['Transaccion', 'Balance'])

print(df)

def bal(bf):
    return bf

def retirada(b, r):
    bf = b - r
    return bf

def deposito(b, i):
    bf = b + i
    return bf

def salir():
    exit()

conteo = 0

while True:
    opcion = int(input("Elige una de las 4 opciones: "))

    if opcion == 1:
        conteo = conteo + 1
        balance_i = bal(balance_i)
        df = df.append({'Transaccion': conteo, 'Balance':bal(balance_i)}, ignore_index=True)
        print(df)
    elif opcion == 2:
        retiro = int(input("Ingrese la cantidad a retirar: "))
        balance_i = retirada(balance_i,retiro)
        conteo = conteo + 1
        df = df.append({'Transaccion': conteo, 'Balance':balance_i}, ignore_index=True)
        print(df)
    elif opcion == 3:
        ingreso = int(input("Ingrese la cantidad a depositar: "))
        balance_i = deposito(balance_i, ingreso)
        conteo = conteo + 1
        df = df.append({'Transaccion': conteo, 'Balance':balance_i}, ignore_index=True)
        print(df)
    elif opcion == 4:
        exit()
    else:
        break