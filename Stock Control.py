# EXAMEN INTRODUCCION A LA PROGRAMACION
# 16 DE MAYO DE 2019
# JAVIER ARTILES MANRIQUE DE LARA

def Busqueda_De_Pieza(catalogo, cod_pieza):
    if cod_pieza not in catalogo:

        x = 0

        print("ERROR: EL CODIGO MARCADO NO SE ENCUENTRA EN EL CATALOGO")

    else:
        x = 1

    return x


def main():
    global f1
    catalogo = {
    }

    num_catalogo = int(input("¿Cuantas piezas hay en el catalogo? "))

    while num_catalogo <= 0:
        print("ERROR: NO PUEDE HABER SOTCK NEGATIVO DE UN PRODUCTO")

        num_catalogo = int(input("¿Cuantas piezas hay en el catalogo? "))

    for i in range(num_catalogo):
        cod_pieza = int(input("Introduzca el CODIGO de la pieza {}: ".format(i + 1)))
        pvp = float(input("Introduzca el PRECIO de la pieza {}: ".format(i + 1)))

        catalogo.update({cod_pieza: pvp})

    print(catalogo)

    cont = "si"

    while cont == "si" or cont == "Si":

        cod_pieza = int(input("Introduzca el CODIGO de la pieza que desea analizar: "))
        num_almacen = int(input("Introduzca el STOCK de dicho producto en el almacen: "))

        stock_almacen = []

        x = Busqueda_De_Pieza(catalogo, cod_pieza)

        if x == 1:

            if cod_pieza not in stock_almacen:
                stock_almacen.append(cod_pieza)
                stock_almacen.append(num_almacen)

        else:
            print("El codigo que ha introducido ya se ha dado de alta en el servidor")

        cont = input("¿Querria dar de alta otro producto del stock? (s/n):")

    print("MENU")
    print("\n1.- Venta de piezas")
    print("2.- Informe de almacen")
    print("3.- Copia de seguridad")
    print("4.- Salir")

    opc = int(input("Introduzca una opcion por favor: "))

    while opc != 4:

        if opc == 1:

            cod_pieza = int(input("Introduzca el codigo de la pieza la cual quiere vender: "))
            num = int(input("Introduzca la cantidad de producto a vender: "))

            if cod_pieza not in stock_almacen:
                print("ERROR: EL PRODUCTO INTRODUCIDO NO EXISTE")

            else:
                pos = stock_almacen.index(cod_pieza)

                if stock_almacen[pos + 1] < num:
                    print("ERROR: LAS UNIDADES EXISTENTES EN EL ALMACEN SON MENORES")

                else:
                    stock_almacen[pos + 1] -= num

            print("MENU")
            print("\n1.- Venta de piezas")
            print("2.- Informe de almacen")
            print("3.- Copia de seguridad")
            print("4.- Salir")

        elif opc == 2:

            print("Informe ALMACEN")
            print(20 * "=")
            print("Codigo     Unidades     Total(EUROS)")
            print(20 * "=")

            for i in range(0, len(stock_almacen) - 1, 2):
                print(stock_almacen[i], stock_almacen[i + 1], stock_almacen[i + 1] * catalogo[stock_almacen[i]])

            print("MENU")
            print("\n1.- Venta de piezas")
            print("2.- Informe de almacen")
            print("3.- Copia de seguridad")
            print("4.- Salir")


        elif opc == 3:

            import pickle

            f1 = open("almacen.dat", "wb+")

            for i in range(0, len(stock_almacen) - 1, 2):
                lista = [stock_almacen[i], stock_almacen[i + 1]]
                pickle.dump(lista, f1)

        opc = int(input("Introduzca una opcion por favor: "))

        print("MENU")
        print("\n1.- Venta de piezas")
        print("2.- Informe de almacen")
        print("3.- Copia de seguridad")
        print("4.- Salir")

    f1.seek(0)

    print("Informe FICHERO")
    print(20 * "=")
    print("Codigo    Unidades")
    print(20 * "=")

    try:
        while not False:
            lista = pickle.load(f1)
            print(lista[0], lista[1])
    except:
        f1.close()

    print("El programa ha finalizado con exito")


main()
