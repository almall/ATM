import pandas as pd

balance = 10000
print("  ATM ")
print("\n")
print("Tu balance actual es +10.000€")
print("""
1)   Balance
2)   Retirada
3)   Depósito
4)   Salir
""")

df = pd.DataFrame()
df['Transacción','Balance'] = None
transac = []
bal = []

conteo = 0

while True:

    option = int(input("Elige una opción: "))
    
    if option == 1:
        print("balance €", balance)
        conteo = conteo + 1
        transac.append(conteo)
        bal.append(balance)

        df['Transacción'].append(transac, ignore_index = True)
        df['Balance'].append(bal, ignore_index = True)

        print(df)

    elif option == 2:
        print("Balance €", balance)
        withdraw = float(input("Enter withdraw amount €: "))
        if withdraw > 0:
            forewardbalance = (balance - withdraw)
            print("Foreward balance €", forewardbalance)
            transac.append(conteo)
            bal.append(forewardbalance)

            df['Transacción'].append(transac, ignore_index = True)
            df['Balance'].append(bal, ignore_index = True)

            print(df)

        elif withdraw > balance:
            print(" no funs in account")
        else:
            print("None withdraw made")
    elif option == 3:
        print("Balance €", balance)
        deposit = float(input("Enter deposit amount €: "))
        if deposit > 0:
            forewardbalance = (balance + deposit)
            print("Foreward balance €", forewardbalance)
            transac.append(conteo)
            bal.append(forewardbalance)

            df['Transacción'].append(transac, ignore_index = True)
            df['Balance'].append(bal, ignore_index = True)

            print(df)

        else:
            print("None deposit made")
    elif option == 4:
        exit()

    

    
