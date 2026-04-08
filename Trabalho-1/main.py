import random
import time

# função para gerar valores aleatorios
def gerador_aleatorio(inicial, final, numeros):

  random.seed(2026) # necessario para termos sempre os mesmos numeros gerados

  numeros_aleatorios = []
  for _ in range(numeros):
    numeros_aleatorios.append(random.randint(inicial, final)) #cria um valor aleatorio e adiciona ao nosso vetor
  return numeros_aleatorios


def bubble_sort(arr):
    tam = len(arr)
    for i in range(tam):
        for j in range(0, tam - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
 
def selection_sort(arr):
    tam = len(arr)
    for i in range(tam):
        min_idx = i
        for j in range(i + 1, tam):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
 
def insertion_sort(arr):
    tam = len(arr)
    for i in range(1, tam):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
 
def shell_sort(arr):
    tam = len(arr)
    gap = tam // 2
    while gap > 0:
        for i in range(gap, tam):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

def bubble_sort_otimizado(arr):
    # Bubble Sort com flag de troca — para verificar se ja esta ordenado
    tam = len(arr)
    for i in range(tam):
        trocou = False
        for j in range(0, tam - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                trocou = True
        if not trocou:
            break
 
def selection_sort_duplo(arr):
    # Selection Sort Duplo — encontra minimo e maximo a cada passagem
    left, right = 0, len(arr) - 1
    while left < right:
        min_idx, max_idx = left, right
        for i in range(left, right + 1):
            if arr[i] < arr[min_idx]:
                min_idx = i
            if arr[i] > arr[max_idx]:
                max_idx = i
        arr[left], arr[min_idx] = arr[min_idx], arr[left]
        if arr[min_idx] == arr[right]:  # max foi movido
            arr[right], arr[min_idx] = arr[min_idx], arr[right]
        else:
            arr[right], arr[max_idx] = arr[max_idx], arr[right]
        left += 1
        right -= 1

def insertion_sort_sentinel(arr):
    # Insertion Sort com sentinela — elimina checagem de limite no while
    min_idx = arr.index(min(arr))
    arr[0], arr[min_idx] = arr[min_idx], arr[0] 
    for i in range(2, len(arr)):
        key = arr[i]
        j = i - 1
        while arr[j] > key:   
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def shell_sort_gap3(arr):
    # Shell Sort com gap 3 — converge mais rápido que com o gap 2
    tam = len(arr)
    gap = tam // 3 + 1
    while gap > 0:
        for i in range(gap, tam):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap = gap // 3 + 1 if gap > 1 else 0

def main(): 
    n = 5000

    dados_random    = gerador_aleatorio(1, 100_000, n)
    dados_ordenado  = sorted(dados_random)
    dados_invertido = sorted(dados_random, reverse=True)

    algoritmos = [
        ("Bubble Sort",         bubble_sort),
        ("Selection Sort",      selection_sort),
        ("Insertion Sort",      insertion_sort),
        ("Shell Sort",          shell_sort),
        ("Bubble Otimizado",    bubble_sort_otimizado),
        ("Selection Duplo",     selection_sort_duplo),
        ("Insertion Sentinela", insertion_sort_sentinel),
        ("Shell Gap/3",         shell_sort_gap3),
    ]

    print(f"{'Algoritmo':<25} {'Aleatório':>12} {'Ordenado':>12} {'Invertido':>12}")
    print("-" * 65)

    for nome, func in algoritmos:

        copia = dados_random[:]
        inicio = time.time()
        func(copia)
        t_random = time.time() - inicio

        copia = dados_ordenado[:]
        inicio = time.time()
        func(copia)
        t_ordenado = time.time() - inicio

        copia = dados_invertido[:]
        inicio = time.time()
        func(copia)
        t_invertido = time.time() - inicio

        print(f"{nome:<25} {t_random:>11.4f}s {t_ordenado:>11.4f}s {t_invertido:>11.4f}s")

    print("-" * 65)


if __name__ == "__main__":
    main()