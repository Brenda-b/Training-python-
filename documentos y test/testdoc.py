def sumas(numero1, numero2):
    """
    Esta funcion recibe dos numeros como parametros
    y devuelve su suma.
    >>> sumas(4,3)
    7
    """
    return numero1+numero2

resultado= sumas(2,4)
print(resultado)

import doctest
doctest.testmod()