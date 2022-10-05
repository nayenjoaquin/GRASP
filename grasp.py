import sys
import time
from parseInput import parseInput
from checkInput import checkInput
from greedy import greedy
from localSearch import localSearch
from localSearch2 import localSearch as localSearch2


def main():

    # Revisa el número de argumentos
    if len(sys.argv) != 5:
        print("Error en la cantidad de argumentos, intente de la siguiente forma:")
        print("Windows: python grasp.py -i <archivo de entrada> -th <threshold>")
        print("Linux: python3 grasp.py -i <archivo de entrada> -th <threshold>")
        return

    # Lee los argumentos
    fileName = sys.argv[2]
    th = sys.argv[4]

    # checkea que el threshold sea un número entre 0 y 1
    th = checkInput(th)
    if th < 0:
        return

    # Lee el archivo de entrada
    lineasGenoma, m, n  = parseInput(fileName)

    start = time.time()
    bestSoFar = 0

    # GRASP utilizando busqueda local 1
    # while time.time() - start < 60:
    #     sol,calidad = greedy(m,n,th,lineasGenoma,0.1)
    #     sol, calidad = localSearch(sol, lineasGenoma, th, m, bestSoFar, start)
    #     if calidad > bestSoFar:
    #         bestSoFar = calidad

    # GRASP utilizando busqueda local 2
    while time.time() - start < 60:
        sol,calidad = greedy(m,n,th,lineasGenoma,0.1)
        sol, calidad = localSearch2(sol, lineasGenoma, th, m, bestSoFar, start)
        if calidad > bestSoFar:
            bestSoFar = calidad






    # # Ejecuta el algoritmo greedy determinista
    # sol1 = greedy(m, n, th, lineasGenoma)

    # # Ejecuta el algoritmo greedy estocástico
    # sol2 = greedy(m, n, th, lineasGenoma, 0.1)









if __name__ == "__main__":
    main()
