import numpy as np

def calculate(lista):
    if len(lista) != 9:
        raise ValueError("La lista debe contener nueve números.")
    
    # Convertir la lista en una matriz 3x3
    matriz = np.array(lista).reshape(3, 3)
    
    # Calcular las estadísticas
    media = [np.mean(matriz, axis=0).tolist(), np.mean(matriz, axis=1).tolist(), np.mean(matriz)]
    varianza = [np.var(matriz, axis=0).tolist(), np.var(matriz, axis=1).tolist(), np.var(matriz)]
    desviacion_estandar = [np.std(matriz, axis=0).tolist(), np.std(matriz, axis=1).tolist(), np.std(matriz)]
    maximo = [np.max(matriz, axis=0).tolist(), np.max(matriz, axis=1).tolist(), np.max(matriz)]
    minimo = [np.min(matriz, axis=0).tolist(), np.min(matriz, axis=1).tolist(), np.min(matriz)]
    suma = [np.sum(matriz, axis=0).tolist(), np.sum(matriz, axis=1).tolist(), np.sum(matriz)]
    
    # Crear el diccionario de resultados
    resultados = {
        'mean': media,
        'variance': varianza,
        'standard deviation': desviacion_estandar,
        'max': maximo,
        'min': minimo,
        'sum': suma
    }
    
    return resultados
# Llamada a la función e impresión del resultado
if __name__ == "__main__":
    try:
        resultado = calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])
        print(resultado)
    except ValueError as e:
        print(e)