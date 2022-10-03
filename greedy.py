from math import ceil
import time


def setupColumnas( n, m, lineasGenoma):

    columnas = []

    for i in range(m):

        charFreq = {
            "A": 0,
            "C": 0,
            "G": 0,
            "T": 0
        }

        for j in range(n):
            charFreq[lineasGenoma[j][i]] += 1

        charMenosFrecuente = min(charFreq, key=charFreq.get)

        columna = {
            "posicion": i,
            "charMenosFrecuente": charMenosFrecuente,
            "charFreq": charFreq[charMenosFrecuente]
        }

        columnas.append(columna)

    return columnas



# metodo greedy para FFMSP
def greedy(m,n,th,lineasGenoma):

    # solucion inicial "XXXXX" 
    sol = "X" * m

    # lista que almacena el char menos frecuente de cada columna
    # y la frecuencia que tiene
    columnas = setupColumnas(n, m, lineasGenoma)
    
    # ordena las columnas por el char menos frecuente
    columnas.sort(key=lambda columna: columna["charFreq"])

    # lista que contiene el porcentaje de diferencia de cada linea del genoma con la solucion
    gradoDiferenciaLineas = [0] * n

    # medir tiempo
    start = time.time()


    threshold = int(ceil(th * m))
    # agregamos a la solución los caracteres menos frecuentes de las primeras m*th - 1 columnas
    # y actualizamos los valores en gradoDiferenciaLineas
    for i in range(threshold - 1):

        # cambio de caracter en la solucion en la posicion de la columna menos frecuente
        sol = sol[:columnas[i]["posicion"]] + columnas[i]["charMenosFrecuente"] + sol[columnas[i]["posicion"] + 1:]

        # actualizamos los valores de gradoDiferenciaLineas
        for j in range(n):
            if lineasGenoma[j][columnas[i]["posicion"]] != columnas[i]["charMenosFrecuente"]:
                gradoDiferenciaLineas[j] += 1

    # borramos las columnas que ya fueron agregadas a la solucion
    columnas = columnas[threshold - 1:]

    # probamos con las columnas restantes y guarda el caracter que maximiza la calidad de la solucion
    gradoDiferenciaLineasAux = gradoDiferenciaLineas.copy()
    mayorCalidad = -1

    while len(columnas) > 0 and mayorCalidad < n:

        mayorCalidad = -1
        solAux = sol
        
        # probamos con cada columna
        for i in range(len(columnas)):
            calidad = 0
            solAux = solAux[:columnas[i]["posicion"]] + columnas[i]["charMenosFrecuente"] + solAux[columnas[i]["posicion"] + 1:]

            # calculamos la calidad de la solucion
            for j in range(n):
                # si el caracter de la linea es diferente al de la solucion actualizamos el grado de diferencia
                if lineasGenoma[j][columnas[i]["posicion"]] != columnas[i]["charMenosFrecuente"]:
                    gradoDiferenciaLineasAux[j] += 1
                # si el grado de diferencia es mayor o igual al treshold, sumamos 1 a la calidad
                if gradoDiferenciaLineasAux[j] >= threshold:
                    calidad += 1

            # si la calidad es mayor a la mejor calidad hasta ahora, guardamos la posicion de la columna
            if calidad > mayorCalidad:
                mayorCalidad = calidad
                posicionMejorColumna = i

            # restauramos el grado de diferencia de las lineas
            gradoDiferenciaLineasAux = gradoDiferenciaLineas.copy()
            solAux = sol

        # agregamos el caracter de la mejor columna a la solucion
        sol = sol[:columnas[posicionMejorColumna]["posicion"]] + columnas[posicionMejorColumna]["charMenosFrecuente"] + sol[columnas[posicionMejorColumna]["posicion"] + 1:]

        for j in range(n):
            if lineasGenoma[j][columnas[posicionMejorColumna]["posicion"]] != columnas[posicionMejorColumna]["charMenosFrecuente"]:
                gradoDiferenciaLineasAux[j] += 1
        
        gradoDiferenciaLineas = gradoDiferenciaLineasAux.copy()

        # borramos la columna que ya fue agregada a la solucion
        columnas.pop(posicionMejorColumna)

    # si encuentra una solucion completa antes de terminar de recorrer las columnas rellenamos con A
    if mayorCalidad == n:
        for i in range(m):
            if sol[i] == "X":
                sol = sol[:i] + "A" + sol[i + 1:]

    # medir tiempo
    end = time.time()

    # solucion
    print(sol)

    # tiempo de ejecucion
    print("Tiempo de ejecucion: ", (end - start)*1000, "ms")

    # calidad de la solucion
    print("Calidad de la solucion: ", mayorCalidad)



    return sol