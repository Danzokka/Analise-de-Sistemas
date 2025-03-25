# Quick Sort Function
import math
import time
import random

def quick_sort(arr: list[int]) -> list[int]:
    # Caso base
    if len(arr) <= 1:
        return arr
    
    # Caso recursivo
    pivo = math.floor(len(arr) / 2)
    left = pegar_esquerda_pivo(arr, arr[pivo])
    meio = pegar_meio_pivo(arr, arr[pivo])
    right = pegar_direita_pivo(arr, arr[pivo])
    
    return quick_sort(left) + meio + quick_sort(right)

def pegar_esquerda_pivo(arr: list[int], pivo: int) -> list[int]:
    esquerda_pivo = []
    for i in range(len(arr)):
        if arr[i] < pivo:
            esquerda_pivo.append(arr[i])
    return esquerda_pivo

def pegar_direita_pivo(arr: list[int], pivo: int) -> list[int]:
    direita_pivo = []
    for i in range(len(arr)):
        if arr[i] > pivo:
            direita_pivo.append(arr[i])
    return direita_pivo

def pegar_meio_pivo(arr: list[int], pivo: int) -> list[int]:
    meio_pivo = []
    for i in range(len(arr)):
        if arr[i] == pivo:
            meio_pivo.append(arr[i])
    return meio_pivo

def gerar_array_com_numeros_aleatorios(tamanho: int) -> list[int]:
    arr = []
    for i in range(tamanho):
        arr.append(random.randint(0, 10000))
    return arr

# Test
arr = gerar_array_com_numeros_aleatorios(100)
start_time = time.time()
print(quick_sort(arr))
print("--- %s seconds ---" % (time.time() - start_time))