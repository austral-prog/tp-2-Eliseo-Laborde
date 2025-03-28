def change():
    expense = 23.75
    money = 100
    change = money - expense
    print("Ingresar gasto:")
    print(expense)
    print("Dinero recibido")
    print(money)
    print("\nVuelto\n")
    print("Pesos:")
    print(change)
    print("Centavos:")
    print((change - 76)*100)
