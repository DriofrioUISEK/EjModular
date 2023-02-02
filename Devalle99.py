def fibonacci(len):
    arreglo = [1, 1]
    for i in range(0, len-2):
        temp = arreglo[i] + arreglo[i+1]
        arreglo.append(temp)
    print("[", end='')
    for i in arreglo:
        if(i < arreglo[-1]):
            print(str(i) + ', ', end='')
        else:
            print(str(i) + "]")
