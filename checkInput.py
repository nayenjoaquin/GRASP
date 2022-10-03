def checkInput(threshold):
    # Revisa que el threshold sea un número
    try:
        threshold = float(threshold)
    except ValueError:
        print("El threshold debe ser un número")
        return -1

    # Revisa que el threshold esté entre 0 y 1
    if threshold < 0 or threshold > 1:
        print("El threshold debe estar entre 0 y 1")
        return -1

    return float(threshold)