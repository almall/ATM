import pandas as pd

balance_i = float(input("Dime la cantidad inicial: "))

print(" ATM ")
print("\n")
print("""
1)   Balance
2)   Retirada
3)   Depósito
4)   Ingreso mediante BIZUM +
5)   Pago mediante BIZUM -
6)   Ingreso mediante transferencia externa +
7)   Pago mediante transferencia externa -
8)   Ingreso mediante transferencia entre cuentas +
9)   Pago mediante transferencia entre cuentas -
10)  Recibo bancario
11)  Pago con tarjeta
12)  Exportar a CSV y salir
13)  Salir
""")

df = pd.DataFrame(columns=['Transacción', 'Tipo', 'Balance'])

print(df)

def bal(bf):
    return bf

def retirada(b, r):
    bf = b - r
    return bf

def deposito(b, i):
    bf = b + i
    return bf

def bizum_charge(b, bi):
    bf = b + bi
    return bf

def bizum_pay(b, bi):
    bf = b - bi

def transfer_ex_charge(b, tr):
    bf = b + tr
    return bf

def transfer_ex_pay(b, tr):
    bf = b - tr
    return bf

def transfer_cu_charge(b, tr):
    bf = b + tr
    return bf

def transfer_cu_pay(b, tr):
    bf = b - tr
    return bf

def recib(b, re):
    bf = b - re
    return bf

def tarjeta(b, tarj):
    bf = b - tarj
    return bf

def salir():
    exit()

conteo: int = 0

while True:

        print(" ATM ")
        print("\n")
        print("""
        1)   Balance
        2)   Retirada
        3)   Depósito
        4)   Ingreso mediante BIZUM +
        5)   Pago mediante BIZUM -
        6)   Ingreso mediante transferencia externa +
        7)   Pago mediante transferencia externa -
        8)   Ingreso mediante transferencia entre cuentas +
        9)   Pago mediante transferencia entre cuentas -
        10)  Recibo bancario
        11)  Pago con tarjeta
        12)  Exportar a CSV y salir
        13)  Salir
        """)
        opcion = float(input("Elige una de las 13 opciones: "))

        if opcion == 1:
            conteo = conteo + 1
            balance_i = bal(balance_i)
            df = df.append({'Transacción': conteo, 'Tipo': ("Balance"), 'Balance':bal(balance_i)}, ignore_index=True)
            print(df)
        elif opcion == 2:
            retiro = float(input("Cantidad a retirar: "))
            balance_i = retirada(balance_i, retiro)
            conteo = conteo + 1
            df = df.append({'Transacción': conteo, 'Tipo': ("Retiro"), 'Balance':balance_i}, ignore_index=True)
            print(df)
        elif opcion == 3:
            ingreso = float(input("Cantidad a depositar: "))
            balance_i = deposito(balance_i, ingreso)
            conteo = conteo + 1
            df = df.append({'Transacción': conteo, 'Tipo': ("Depósito"), 'Balance':balance_i}, ignore_index=True)
            print(df)
        elif opcion == 4:
            biz = float(input("Cobro BIZUM: "))
            balance_i = bizum_charge(balance_i, biz)
            conteo = conteo + 1
            df = df.append({'Transacción': conteo, 'Tipo': ("BIZUM +"), 'Balance':balance_i}, ignore_index=True)
            print(df)
        elif opcion == 5:
            biz = float(input("Pago BIZUM: "))
            balance_i = bizum_pay(balance_i, biz)
            conteo = conteo + 1
            df = df.append({'Transacción': conteo, 'Tipo': ("BIZUM -"), 'Balance':balance_i}, ignore_index=True)
            print(df)
        elif opcion == 6:
            transfer = float(input("Transferencia externa: "))
            balance_i = transfer_ex_charge(balance_i, transfer)
            conteo = conteo + 1
            df = df.append({'Transacción': conteo, 'Tipo': ("Transferencia externa +"), 'Balance':balance_i}, ignore_index=True)
            print(df)
        elif opcion == 7:
            transfer = float(input("Transferencia externa: "))
            balance_i = transfer_ex_pay(balance_i, transfer)
            conteo = conteo + 1
            df = df.append({'Transacción': conteo, 'Tipo': ("Transferencia externa -"), 'Balance':balance_i}, ignore_index=True)
            print(df)
        elif opcion == 8:
            transfer = float(input("Transferencia entre cuentas: "))
            balance_i = transfer_cu_charge(balance_i, transfer)
            conteo = conteo + 1
            df = df.append({'Transacción': conteo, 'Tipo': ("Transferencia entre cuentas +"), 'Balance':balance_i}, ignore_index=True)
            print(df)
        elif opcion == 9:
            transfer = float(input("Transferencia entre cuentas: "))
            balance_i = transfer_cu_pay(balance_i, transfer)
            conteo = conteo + 1
            df = df.append({'Transacción': conteo, 'Tipo': ("Transferencia entre cuentas -"), 'Balance':balance_i}, ignore_index=True)
            print(df)
        elif opcion == 10:
            recibo = float(input("Cuantía del recibo a pagar: "))
            balance_i = recib(balance_i, recibo)
            conteo = conteo + 1
            df = df.append({'Transacción': conteo, 'Tipo': ("Recibo"), 'Balance':balance_i}, ignore_index=True)
            print(df)
        elif opcion == 11:
            tarj = float(input("Cargo con tarjeta: "))
            balance_i = tarjeta(balance_i, tarj)
            conteo = conteo + 1
            df = df.append({'Transacción': conteo, 'Tipo': ("Pago con tarjeta"), 'Balance':balance_i}, ignore_index=True)
            print(df)
        elif opcion == 12:
            df.to_csv('ATM.csv',mode = 'a', index = False)
            exit()
        elif opcion == 13:
            exit()
        else:
            break