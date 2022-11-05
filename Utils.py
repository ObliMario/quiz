def getIntput():
    while True:
        num = input("Ingrese una opción: ")
        try:
            val = int(num)
            return val
        except ValueError:
            print("Ingrese solamente números")
                