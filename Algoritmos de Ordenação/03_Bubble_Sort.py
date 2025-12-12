# EXERCÍCIO 1 — BUBBLE SORT
# Contar TESTES e TROCAS.

def bubble_sort(arr):
    a = arr[:]
    testes = 0
    trocas = 0

    for i in range(len(a)):
        for j in range(0, len(a)-1-i):
            testes += 1
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                trocas += 1

    return a, testes, trocas

if __name__ == "__main__":
    lista = [81,60,6,49,40,41,38,64,44,36]
    ordenada, testes, trocas = bubble_sort(lista)
    print("\nBUBBLE SORT:")
    print("Original:", lista)
    print("Ordenada:", ordenada)
    print("Testes:", testes, "Trocas:", trocas)