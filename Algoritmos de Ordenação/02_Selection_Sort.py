# EXERCÍCIO 1 — SELECTION SORT
# Contar TESTES e TROCAS.

def selection_sort(arr):
    a = arr[:]
    testes = 0
    trocas = 0

    for i in range(len(a)):
        min_i = i
        for j in range(i+1, len(a)):
            testes += 1
            if a[j] < a[min_i]:
                min_i = j
        if min_i != i:
            a[i], a[min_i] = a[min_i], a[i]
            trocas += 1

    return a, testes, trocas

if __name__ == "__main__":
    lista = [100,48,19,61,86,33,13,43,84,28]
    ordenada, testes, trocas = selection_sort(lista)
    print("\nSELECTION SORT:")
    print("Original:", lista)
    print("Ordenada:", ordenada)
    print("Testes:", testes, "Trocas:", trocas)