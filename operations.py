import math

def es_primo(n):
    """
    Verifica si un número es primo.
    
    Args:
    n (int): El número a verificar.
    
    Returns:
    bool: True si n es primo, False en caso contrario.
    """
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def inverso_modular(a, p):
    """
    Calcula el inverso modular de a módulo p usando el algoritmo euclidiano extendido.
    
    Args:
    a (int): El número para el cual calcular el inverso.
    p (int): El módulo primo.
    
    Returns:
    int: El inverso modular de a módulo p.
    
    Raises:
    ValueError: Si no existe el inverso modular.
    """
    if math.gcd(a, p) != 1:
        raise ValueError(f"El inverso modular de {a} módulo {p} no existe.")
    
    def egcd(a, b):
        if a == 0:
            return b, 0, 1
        else:
            g, y, x = egcd(b % a, a)
            return g, x - (b // a) * y, y

    g, x, _ = egcd(a, p)
    if g != 1:
        raise ValueError(f"El inverso modular de {a} módulo {p} no existe.")
    else:
        return x % p

def validar_entradas(a, b, p):
    """
    Valida las entradas para las operaciones modulares.
    
    Args:
    a, b, p (int): Los números a validar.
    
    Raises:
    ValueError: Si alguna entrada no es un entero no negativo o si p no es primo.
    """
    for val, name in [(a, 'a'), (b, 'b'), (p, 'p')]:
        if not isinstance(val, int):
            raise ValueError(f"{name} debe ser un entero.")
        if val < 0:
            raise ValueError(f"{name} debe ser no negativo.")
    
    if not es_primo(p):
        raise ValueError(f"p ({p}) debe ser un número primo.")

def suma_modular(a, b, p):
    """
    Calcula (a + b) mod p.
    
    Args:
    a, b (int): Los números a sumar.
    p (int): El módulo primo.
    
    Returns:
    int: El resultado de (a + b) mod p.
    
    Raises:
    ValueError: Si las entradas no son válidas.
    """
    validar_entradas(a, b, p)
    return (a + b) % p

def resta_modular(a, b, p):
    """
    Calcula (a - b) mod p.
    
    Args:
    a, b (int): Los números para la resta.
    p (int): El módulo primo.
    
    Returns:
    int: El resultado de (a - b) mod p.
    
    Raises:
    ValueError: Si las entradas no son válidas.
    """
    validar_entradas(a, b, p)
    return (a - b) % p

def multiplicacion_modular(a, b, p):
    """
    Calcula (a * b) mod p.
    
    Args:
    a, b (int): Los números a multiplicar.
    p (int): El módulo primo.
    
    Returns:
    int: El resultado de (a * b) mod p.
    
    Raises:
    ValueError: Si las entradas no son válidas.
    """
    validar_entradas(a, b, p)
    return (a * b) % p

def division_modular(a, b, p):
    """
    Calcula (a * b^(-1)) mod p usando el inverso modular.
    
    Args:
    a, b (int): Los números para la división.
    p (int): El módulo primo.
    
    Returns:
    int: El resultado de (a * b^(-1)) mod p.
    
    Raises:
    ValueError: Si las entradas no son válidas o si no existe el inverso modular.
    ZeroDivisionError: Si b es 0.
    """
    validar_entradas(a, b, p)
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero.")
    b_inv = inverso_modular(b, p)
    return (a * b_inv) % p

def potencia_modular(a, b, p):
    """
    Calcula a^b mod p usando el algoritmo de exponenciación rápida.
    
    Args:
    a (int): La base.
    b (int): El exponente.
    p (int): El módulo primo.
    
    Returns:
    int: El resultado de a^b mod p.
    
    Raises:
    ValueError: Si las entradas no son válidas.
    """
    validar_entradas(a, b, p)
    resultado = 1
    a = a % p
    while b > 0:
        if b % 2 == 1:
            resultado = (resultado * a) % p
        a = (a * a) % p
        b = b // 2
    return resultado

