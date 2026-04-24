# Simulado Classificao e pesuqisa pre g1 

## 1 

n² log n 

## 2 
  
n  
n log n 
n2 
n2 
n2 log n 
n3 
n! 

## 3

Ta no bubble.py

## 4

O algoritimo de Counting sort ele funciona primeiro criando um array cheio de zeros com o tamanho do numero maior + 1, depois ele vai colocando o numero de vezes que aparece nesse array separado somando + 1, no index do numero, se por exemplo tiver dois numeros 5 no array a ser ordenado no array extra no index 5 sera somado dois. Depois disso ele vai pegando por frequencia 

## 5

Ele e importante pois o disco consegue fazer menos mudancas com a memoria, fazendo menos uso de memoria ram, por conta de fazer menos memory swap

## 6

def ??????(arr):
    # Pega o tamanho do array
    n = len(arr)
    # serve para pegar o gap do array para n precisar ler todo ele para a ordenacao
    gap = n // 2
    while gap > 0:

        for i in range(gap, n):
           

            # Aqui ele cria uma variavel temporaria para comparacao
            temp = arr[i]
            j = i
            # durante esse loop ele serve para verificar se o valor atual precisa ou n ser trocado pelo proximo 
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j – gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr
    #este e shell sort, ele n usa espaco extra e n log n

## 7

Sim, existem deversas otimizacoes que podem ser adicionados como aumentar o gap para 3 ou adicionar uma verificacao que verifica se o array ja esta ordenado