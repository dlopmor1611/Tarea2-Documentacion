"""
Módulo de Calculadora Científica Simple.
Este módulo proporciona operaciones matemáticas básicas y manejo de errores.
"""

def sumar(a: float, b: float) -> float:
    """Suma dos números reales.

    Args:
        a (float): Primer sumando.
        b (float): Segundo sumando.

    Returns:
        float: El resultado de la suma de a y b.
    """
    return a + b

def dividir(a: float, b: float) -> float:
    """Divide el primer número entre el segundo.

    Args:
        a (float): Numerador.
        b (float): Denominador.

    Raises:
        ValueError: Si el denominador es cero.

    Returns:
        float: El cociente de la división.
    """
    if b == 0:
        raise ValueError("Error matemático: No se puede dividir entre cero.")
    return a / b
