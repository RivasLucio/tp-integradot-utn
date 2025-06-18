import time

# Algoritmo 1: Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Algoritmo 2: Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        actual = arr[i]
        j = i - 1
        while j >= 0 and actual < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = actual
    return arr

# Algoritmo 3: Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivote = arr[0]
        menores = [x for x in arr[1:] if x <= pivote]
        mayores = [x for x in arr[1:] if x > pivote]
        return quick_sort(menores) + [pivote] + quick_sort(mayores)

# Búsqueda 1: Lineal
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Búsqueda 2: Binaria (requiere lista ordenada)
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Lista de prueba (simula un catálogo de precios)
productos = [4500, 12000, 7800, 4000, 3300, 5600, 9000]

print("📦 Lista original de precios:", productos)

# Comparación de algoritmos de ordenamiento
for nombre, funcion in [("Bubble Sort", bubble_sort), ("Insertion Sort", insertion_sort), ("Quick Sort", quick_sort)]:
    datos = productos.copy()
    inicio = time.time()
    ordenada = funcion(datos)
    fin = time.time()
    print(f"\n🧮 {nombre}:")
    print("Lista ordenada:", ordenada)
    print(f"Tiempo: {fin - inicio:.6f} segundos")

# Prueba de búsqueda
precio_buscado = 5600
print(f"\n🔍 Buscando el precio {precio_buscado}...")

# Búsqueda lineal
pos = linear_search(productos, precio_buscado)
if pos != -1:
    print(f" Encontrado por búsqueda lineal en la posición {pos}")
else:
    print(" No encontrado por búsqueda lineal.")

# Búsqueda binaria (sobre lista ordenada con Quick Sort)
ordenada = quick_sort(productos)
pos_bin = binary_search(ordenada, precio_buscado)
if pos_bin != -1:
    print(f" Encontrado por búsqueda binaria en la posición {pos_bin} (lista ordenada)")
else:
    print(" No encontrado por búsqueda binaria.")
