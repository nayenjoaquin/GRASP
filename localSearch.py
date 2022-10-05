from math import ceil
import time
from greedy import getCalidadSolucion


charMap = ["A", "C", "G", "T"]

def localSearch(sol, lineasGenoma, th, m, bestSoFar, start):

    threshold = int(ceil(m*th))
    solAux = sol
    mejorSol = sol
    mejorCalidad = bestSoFar
    for i in range(m):
        if time.time() - start > 60:
            return mejorSol,mejorCalidad
        for j in range(4):
            if charMap[j] != sol[i]:
                solAux = mejorSol[:i] + charMap[j] + mejorSol[i+1:]
                calidadAux = getCalidadSolucion(lineasGenoma, solAux, threshold)
                if calidadAux > mejorCalidad:
                    mejorSol = solAux
                    mejorCalidad = calidadAux
                    print(f"nueva calidad {mejorCalidad} transcurrido {time.time() - start} segundos")
        


    return mejorSol, mejorCalidad