# EXERCÍCIO 1 — QUICK SORT
# Enunciado:
# "Modifique o Quick Sort para contar TESTES e TROCAS."

def quick_sort(arr):
    a = arr[:]
    testes = 0
    trocas = 0

    def qs(lo, hi):
        if lo < hi:
            p = partition(lo, hi)
            qs(lo, p-1)
            qs(p+1, hi)

    def partition(lo, hi):
        nonlocal testes, trocas
        pivot = a[hi]
        i = lo

        for j in range(lo, hi):
            testes += 1
            if a[j] < pivot:
                a[i], a[j] = a[j], a[i]
                trocas += 1
                i += 1

        a[i], a[hi] = a[hi], a[i]
        trocas += 1
        return i

    qs(0, len(a)-1)
    return a, testes, trocas


if __name__ == "__main__":
    lista = [76,73,16,95,35,87,68,69,51,92]
    ordenada, testes, trocas = quick_sort(lista)
    print("\nQUICK SORT:")
    print("Original:", lista)
    print("Ordenada:", ordenada)
    print("Testes:", testes, "Trocas:", trocas)
