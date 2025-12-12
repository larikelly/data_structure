# EXERCÍCIO 1 — COUNTING SORT
# Enunciado:
# "Modifique o Counting Sort para contar TESTES e TROCAS."

def counting_sort(arr):
    a = arr[:]
    testes = 0
    trocas = 0

    k = max(a)
    count = [0] * (k+1)

    for num in a:
        testes += 1
        count[num] += 1

    i = 0
    for num in range(len(count)):
        while count[num] > 0:
            trocas += 1
            a[i] = num
            i += 1
            count[num] -= 1

    return a, testes, trocas


if __name__ == "__main__":
    lista = [15,97,14,29,7,24,31,59,78,85]
    ordenada, testes, trocas = counting_sort(lista)
    print("\nCOUNTING SORT:")
    print("Original:", lista)
    print("Ordenada:", ordenada)
    print("Testes:", testes, "Trocas:", trocas)
