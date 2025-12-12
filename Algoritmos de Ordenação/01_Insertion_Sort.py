# EXERCÍCIO 1 — INSERTION SORT
# Enunciado:
# "Modifique o algoritmo de Insertion Sort para imprimir a quantidade
# de TESTES e TROCAS realizadas durante a ordenação."

def insertion_sort(arr):
    a = arr[:]           
    testes = 0           
    trocas = 0           

    for i in range(1, len(a)):
        chave = a[i]
        j = i - 1
        testes += 1
        while j >= 0 and a[j] > chave:
            testes += 1
            a[j+1] = a[j]
            trocas += 1
            j -= 1
        a[j+1] = chave  
    return a, testes, trocas


if __name__ == "__main__":
    listas = [
        [12, 42, 83, 25, 67, 71, 3, 4, 94, 53],
        [100, 48, 19, 61, 86, 33, 13, 43, 84, 28]
    ]

    print("\n=========== INSERTION SORT ===========")
    for i, lista in enumerate(listas, start=1):
        ordenada, testes, trocas = insertion_sort(lista)
        print(f"\nLista {i}:")
        print("Original:", lista)
        print("Ordenada:", ordenada)
        print("Testes:", testes)
        print("Trocas:", trocas)
