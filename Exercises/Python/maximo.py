def maximo(n1, n2):
    """Dados dos números, se retorna el mayor de ellos.

    Args:
        n1 (int): Primer número
        n2 (int): Segundo número
    Returns:
        int: Mayor de ambos números
    """
    if n1 < n2:
        return n2
    elif n2 < n1:
        return n1
    elif n1 == n2:
        raise Exception("Los valores son iguales.")
    raise Exception("Algo malió sal :P")

print (maximo(200, 200))
