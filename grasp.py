import sys
import time
from parseInput import parseInput
from checkInput import checkInput
from greedy import greedy
from localSearch import localSearch


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

    soluciones = []

    while time.time() - start < 60:
        sol,tiempo,calidad = greedy(m,n,th,lineasGenoma,0.1)
        soluciones.append(localSearch(sol, lineasGenoma, th, m, n, calidad, start)) 





    # # Ejecuta el algoritmo greedy determinista
    # sol1 = greedy(m, n, th, lineasGenoma)

    # # Ejecuta el algoritmo greedy estocástico
    # sol2 = greedy(m, n, th, lineasGenoma, 0.1)









if __name__ == "__main__":
    main()
