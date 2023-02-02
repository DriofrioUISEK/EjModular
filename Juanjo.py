def funcionjuanjo ():
    numero = int(input("ingresa un numero\n"))
    numero2 = int(input("ingresa otro numero :D\n"))
    numero3 = int(input("ingresa un ultimo numero\n"))
    print("por favor selecciona lo que quieres hacer con estos numeros\n")
    print("1. Sumarlos\n2. Multiplicarlos\n3. Sacar su promedio\n4. Todas las anteriores\n5. No hacer nada\n")
    print("elige cada opcion escribiendo el numero asignado\n")
    eleccion=int(input())
    if eleccion == 1:
        eleccion1=numero+numero3+numero2
        print(eleccion1)
    elif eleccion == 2:
        eleccion2=numero*numero2*numero3
        print(eleccion2)
    elif eleccion == 3:
        eleccion3=(numero+numero3+numero2)/3
        print(eleccion3)
    elif eleccion == 4:
        eleccion1 = numero + numero3 + numero2
        print(eleccion1)
        eleccion2 = numero * numero2 * numero3
        print(eleccion2)
        eleccion3 = (numero + numero3 + numero2) / 3
        print(eleccion3)
    elif eleccion == 5:
        print("Ok no hare nada")
    else:
        print("elige cada opcion escribiendo el numero asignado\n")
        funcionjuanjo()