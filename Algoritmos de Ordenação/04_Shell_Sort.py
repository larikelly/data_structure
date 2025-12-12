# EXERCÍCIO 1 — SHELL SORT
# Enunciado:
# "Modifique o Shell Sort para contar TESTES e TROCAS."

def shell_sort(arr):
    a = arr[:]
    testes = 0
    trocas = 0
    gap = len(a) // 2

    while gap > 0:
        for i in range(gap, len(a)):
            temp = a[i]
            j = i
            testes += 1
            while j >= gap and a[j-gap] > temp:
                testes += 1
                a[j] = a[j-gap]
                trocas += 1
                j -= gap
            a[j] = temp
        gap //= 2

    return a, testes, trocas


if __name__ == "__main__":
    lista = [45,27,11,89,63,39,9,58,52,17]
    ordenada, testes, trocas = shell_sort(lista)
    print("\nSHELL SORT:")
    print("Original:", lista)
    print("Ordenada:", ordenada)
    print("Testes:", testes, "Trocas:", trocas)
