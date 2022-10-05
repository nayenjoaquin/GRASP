import sys
import time
from parseInput import parseInput
from checkInput import checkInput
from greedy import greedy
from localSearch import localSearch
from localSearch2 import localSearch as localSearch2


def main():

    # Revisa el número de argumentos
    if len(sys.argv) != 13:
        print("Error en el formato de entrada, pruebe de la siguiente forma:")
        print("Windows: python grasp.py -i <archivo de entrada> -th <threshold> -d <determinismo> -tL <tiempo límite> -lsL <limite busqueda local> -tunning <1:tunning, 0:debug>")
        print("Linux: python3 grasp.py -i <archivo de entrada> -th <threshold> -d <determinismo> -tL <tiempo límite> -lsL <límite busqueda local> -tunning <1:tunning, 0:debug>")
        return

    # Lee los argumentos
    fileName = sys.argv[2]
    th = sys.argv[4]
    determinismo = sys.argv[6]
    timeLimit = int(sys.argv[8])
    localSearchLimit = int(sys.argv[10])
    tunning = int(sys.argv[12])



    # checkea que el threshold sea un número entre 0 y 1
    th = checkInput(th)

    # checkea que el determinismo sea un número entre 0 y 1
    determinismo = checkInput(determinismo)

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
    while time.time() - start < timeLimit:
        sol,calidad = greedy(m,n,th,lineasGenoma, determinismo)
        sol, calidad = localSearch2(sol, lineasGenoma, th, m, bestSoFar, start, timeLimit, localSearchLimit,tunning)
        if calidad > bestSoFar:
            bestSoFar = calidad

    if tunning == 1:
        print(bestSoFar)





if __name__ == "__main__":
    main()
