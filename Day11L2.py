import math
from collections import Counter
from typing import List, Union, Any

# 1
def pares_e_impares(numero: int) -> str:
    """
    Cuenta la cantidad de números pares e impares desde 0 hasta el número dado.
    Args:
    numero: Entero positivo hasta el cual contar   
    Returns:
        Cadena con el conteo de pares e impares
    """
    pares = sum(1 for i in range(numero + 1) if i % 2 == 0)
    impares = numero + 1 - pares
    return f"El número de impares es {impares}.\nEl número de pares es {pares}."

# 2
def factorial(n: int) -> int:
    """
    Calcula el factorial de un número entero no negativo.
    Args:
    n: Número entero para calcular factorial
    Returns:
    Factorial del número
    """
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos")
    return 1 if n == 0 else n * factorial(n - 1)

# 3
def esta_vacio(objeto: Any) -> bool:
    """
    Determina si un objeto está vacío.
    Args:
    objeto: Cualquier objeto de Python a verificar
    Returns:
    lTrue si el objeto está vacío, False en caso contrario
    """
    if isinstance(objeto, (list, tuple, str, dict, set)):
        return len(objeto) == 0
    return objeto is None

# Funciones estadísticas para listas
def calcular_media(datos: List[Union[int, float]]) -> float:
    """Calcula la media aritmética de una lista de números."""
    if not datos:
        raise ValueError("La lista de datos está vacía")
    return sum(datos) / len(datos)

def calcular_mediana(datos: List[Union[int, float]]) -> float:
    """Calcula la mediana de una lista de números."""
    if not datos:
        raise ValueError("La lista de datos está vacía")
    
    datos_ordenados = sorted(datos)
    n = len(datos_ordenados)
    mitad = n // 2
    
    if n % 2 == 1:
        return datos_ordenados[mitad]
    else:
        return (datos_ordenados[mitad - 1] + datos_ordenados[mitad]) / 2

def calcular_moda(datos: List[Union[int, float]]) -> List[Union[int, float]]:
    """Calcula la moda(s) de una lista de números."""
    if not datos:
        raise ValueError("La lista de datos está vacía")
    
    contador = Counter(datos)
    max_frecuencia = max(contador.values())
    modas = [k for k, v in contador.items() if v == max_frecuencia]
    
    return modas if len(modas) > 1 else modas[0]

def calcular_rango(datos: List[Union[int, float]]) -> float:
    """Calcula el rango de una lista de números."""
    if not datos:
        raise ValueError("La lista de datos está vacía")
    return max(datos) - min(datos)

def calcular_varianza(datos: List[Union[int, float]], poblacional: bool = True) -> float:
    """Calcula la varianza de una lista de números."""
    if not datos:
        raise ValueError("La lista de datos está vacía")
    
    media = calcular_media(datos)
    n = len(datos)
    divisor = n if poblacional else n - 1
    return sum((x - media) ** 2 for x in datos) / divisor

def calcular_desviacion_estandar(datos: List[Union[int, float]], poblacional: bool = True) -> float:
    """Calcula la desviación estándar de una lista de números."""
    return math.sqrt(calcular_varianza(datos, poblacional))