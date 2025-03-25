# Merge Sort Function

def merge_sort(arr: list[int]) -> list[int]:
    # Caso base
    if len(arr) <= 1:
        return arr
    
    # Caso recursivo
    meio = len(arr) // 2
    
    esquerda = []
    direita = []
    
    for i in range(meio):
        esquerda.append(arr[i])
        
    for i in range(meio, len(arr)):
        direita.append(arr[i])
        
    esquerda = merge_sort(esquerda)
    direita = merge_sort(direita)
    
    return merge(esquerda, direita)

# Merge Function
def merge(esquerda: list[int], direita: list[int]) -> list[int]:
    merged = []
    esquerda_index = 0
    direita_index = 0
    
    while esquerda_index < len(esquerda) and direita_index < len(direita):
        if esquerda[esquerda_index] < direita[direita_index]:
            merged.append(esquerda[esquerda_index])
            esquerda_index += 1
        else:
            merged.append(direita[direita_index])
            direita_index += 1
    
    merged += esquerda[esquerda_index:]
    merged += direita[direita_index:]
    
    return merged

# Test
arr = [1, 14, 2, 5, 2, 18]
print(merge_sort(arr))
