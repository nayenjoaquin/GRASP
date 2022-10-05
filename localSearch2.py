from math import ceil
from random import randint
from secrets import randbelow
import time
from greedy import getCalidadSolucion

intToChar = ["A", "C", "G", "T"]
charToInt = {
    "A": 0,
    "C": 1,
    "G": 2,
    "T": 3
}

def localSearch(sol, lineasGenoma, th, m, bestSoFar, totalTime):

    threshold = int(ceil(m*th))

    mejorSol = sol
    mejorCalidad = bestSoFar
    start = time.time()
    while time.time() - start < 5 and time.time() - totalTime < 60:
        gap = randint(1, 5)
        i = randbelow(m - gap)
        j = i + gap
        replace = "".join([intToChar[randbelow(4)] for _ in range(gap)])
        solAux = mejorSol[:i] + replace + mejorSol[j:]
        calidadAux = getCalidadSolucion(lineasGenoma, solAux, threshold)
        if calidadAux > mejorCalidad:
            mejorSol = solAux
            mejorCalidad = calidadAux
            start = time.time()
            print(f"nueva calidad {mejorCalidad} transcurrido {time.time() - totalTime} segundos")

    return mejorSol, mejorCalidad