from math import ceil
import time


charMap = ["A", "C", "G", "T"]

def getCalidadSolucion(lineasGenoma, solucion, th):

    n = len(lineasGenoma)
    m = len(lineasGenoma[0])
    calidad = 0

    for i in range(n):
        diferencia = 0
        for j in range(m):
            if lineasGenoma[i][j] != solucion[j]:
                diferencia += 1
        if diferencia >= th:
            calidad += 1

    return calidad

def localSearch(sol, lineasGenoma, th, m, n, calidad, start):

    threshold = int(ceil(m*th))

    print("")
    print("BUSQUEDA LOCAL")
    print(f"calidad inicial: {calidad}")
    solAux = sol
    mejorSol = sol
    for i in range(m):
        if time.time() - start > 60:
            return mejorSol
        for j in range(4):
            if charMap[j] != sol[i]:
                solAux = solAux[:i] + charMap[j] + solAux[i+1:]
                calidadAux = getCalidadSolucion(lineasGenoma, solAux, threshold)
                if calidadAux > calidad:
                    mejorSol = solAux
                    calidad = calidadAux
                    print(f"nueva calidad: {calidad} transcurrido: {time.time() - start} segundos")
        
        sol = mejorSol

    # print(f"nueva calidad: {calidad} transcurrido: {time.time() - start} segundos")

    return sol