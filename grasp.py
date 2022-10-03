import sys
from parseInput import parseInput
from checkInput import checkInput
from greedy import greedy


def main():

    # Revisa el número de argumentos
    if len(sys.argv) != 5:
        print("Error en la cantidad de argumentos, intente de la siguiente forma:")
        print("Windows: python main.py -i <archivo de entrada> -th <threshold>")
        print("Linux: python3 main.py -i <archivo de entrada> -th <threshold>")
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

    # Ejecuta el algoritmo greedy
    sol = greedy(m, n, th, lineasGenoma)








if __name__ == "__main__":
    main()
