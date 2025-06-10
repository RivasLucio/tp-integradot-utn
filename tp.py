def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Intercambio de elementos si están en el orden incorrecto
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid  # Devuelve la posición
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1  # Si no se encuentra el valor

# Datos de prueba
datos = [45, 12, 78, 4, 33, 56, 9]
print("Lista original:", datos)

# Ordenamiento
bubble_sort(datos)
print("Lista ordenada:", datos)

# Búsqueda de un número
valor_buscado = 33
pos = binary_search(datos, valor_buscado)
if pos != -1:
    print(f"El número {valor_buscado} fue encontrado en la posición {pos}.")
else:
    print(f"El número {valor_buscado} no fue encontrado.")
