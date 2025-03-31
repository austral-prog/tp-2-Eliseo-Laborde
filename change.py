def change():
    expense = 23.75
    money = 100
    change = money - expense
    pesos = int(change)
    centavos = int((change-pesos)*100)
    print(f"Ingresar gasto:\n{expense}")
    print(f"Dinero recibido\n{money}")
    print("\nVuelto\n")
    print(f"Pesos:\n{pesos}")
    print(f"Centavos:\n{centavos}")
