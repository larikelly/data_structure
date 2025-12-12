# EXERCÍCIO 1 — MERGE SORT
# Enunciado:
# "Modifique o Merge Sort para contar TESTES e TROCAS."
# 

def merge_sort(arr):
    testes = 0
    trocas = 0

    def merge(a):
        nonlocal testes, trocas
        if len(a) <= 1:
            return a

        mid = len(a)//2
        left = merge(a[:mid])
        right = merge(a[mid:])
        merged = []

        i = j = 0
        while i < len(left) and j < len(right):
            testes += 1
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
                trocas += 1

        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged

    final = merge(arr[:])
    return final, testes, trocas


if __name__ == "__main__":
    lista = [88,77,26,62,30,96,56,65,98,99]
    ordenada, testes, trocas = merge_sort(lista)
    print("\nMERGE SORT:")
    print("Original:", lista)
    print("Ordenada:", ordenada)
    print("Testes:", testes, "Trocas:", trocas)
