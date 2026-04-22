def mergesort(arr):
    if len(arr) <= 1:
        return
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    mergesort(left)
    mergesort(right)
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


def mergesort_otimizado(arr):
    # Usa insertion sort para vetores pequenos
    def insertion(a, left, right):
        for i in range(left + 1, right + 1):
            key = a[i]
            j = i - 1
            while j >= left and a[j] > key:
                a[j + 1] = a[j]
                j -= 1
            a[j + 1] = key

    def _ms(a, left, right):
        if right - left <= 32:
            insertion(a, left, right)
            return
        mid = (left + right) // 2
        _ms(a, left, mid)
        _ms(a, mid + 1, right)
        temp = []
        i, j = left, mid + 1
        while i <= mid and j <= right:
            if a[i] <= a[j]:
                temp.append(a[i]); i += 1
            else:
                temp.append(a[j]); j += 1
        while i <= mid:
            temp.append(a[i]); i += 1
        while j <= right:
            temp.append(a[j]); j += 1
        a[left:right+1] = temp

    if len(arr) <= 1:
        return
    _ms(arr, 0, len(arr) - 1)


def heapsort(arr):
    n = len(arr)

    def sift_down(a, start, end):
        root = start
        while True:
            child = 2 * root + 1
            if child > end:
                break
            if child + 1 <= end and a[child] < a[child + 1]:
                child += 1
            if a[root] < a[child]:
                a[root], a[child] = a[child], a[root]
                root = child
            else:
                break

    # construi o heap
    for start in range((n - 2) // 2, -1, -1):
        sift_down(arr, start, n - 1)

    # extrai os elementos do heap
    for end in range(n - 1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]
        sift_down(arr, 0, end - 1)


def heapsort_otimizado(arr):
    # heapify reduzindo trocas mantendo o valor da raiz
    n = len(arr)

    def sift_down_optimized(a, start, end):
        root = start
        value = a[root]
        while True:
            child = 2 * root + 1
            if child > end:
                break
            if child + 1 <= end and a[child] < a[child + 1]:
                child += 1
            if a[child] > value:
                a[root] = a[child]
                root = child
            else:
                break
        a[root] = value

    for start in range((n - 2) // 2, -1, -1):
        sift_down_optimized(arr, start, n - 1)

    for end in range(n - 1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]
        sift_down_optimized(arr, 0, end - 1)


def quicksort(arr):
    def _qs(a, low, high):
        if low < high:
            mid = (low + high) // 2
            a[mid], a[high] = a[high], a[mid]
            pivot = a[high]
            i = low
            for j in range(low, high):
                if a[j] <= pivot:
                    a[i], a[j] = a[j], a[i]
                    i += 1
            a[i], a[high] = a[high], a[i]
            _qs(a, low, i - 1)
            _qs(a, i + 1, high)

    if len(arr) <= 1:
        return
    _qs(arr, 0, len(arr) - 1)


def quicksort_otimizado(arr):
    # quicksort com a mediana de três, insertion para partições pequenas e ordenando a partição menor primeiro
    def insertion(a, left, right):
        for i in range(left + 1, right + 1):
            key = a[i]
            j = i - 1
            while j >= left and a[j] > key:
                a[j + 1] = a[j]
                j -= 1
            a[j + 1] = key

    def media_de_tres(a, i, j):
        mid = (i + j) // 2
        if a[mid] < a[i]:
            a[i], a[mid] = a[mid], a[i]
        if a[j] < a[i]:
            a[i], a[j] = a[j], a[i]
        if a[j] < a[mid]:
            a[mid], a[j] = a[j], a[mid]
        return mid

    def qs(a, low, high):
        while low < high:
            if high - low <= 32:
                insertion(a, low, high)
                break
            m = media_de_tres(a, low, high)
            a[m], a[high] = a[high], a[m]
            pivot = a[high]
            i = low
            for j in range(low, high):
                if a[j] <= pivot:
                    a[i], a[j] = a[j], a[i]
                    i += 1
            a[i], a[high] = a[high], a[i]
            # ordena primeiro a partição menor
            if i - 1 - low < high - (i + 1):
                qs(a, low, i - 1)
                low = i + 1
            else:
                qs(a, i + 1, high)
                high = i - 1

    if len(arr) <= 1:
        return
    qs(arr, 0, len(arr) - 1)

def counting_sort_numeros(arr, pos): 
    n = len(arr)
    saida = [0] * n
    count = [0] * 10  

    for i in range(n):
        digit = (arr[i] // pos) % 10 
        count[digit] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        digit = (arr[i] // pos) % 10 
        saida[count[digit] - 1] = arr[i] 
        count[digit] -= 1 

    for i in range(n):
        arr[i] = saida[i]


def radix_sort(arr):
    # ordenação radix para inteiros não-negativos
    if not arr:
        return
    pos = 1
    max_num = max(arr)
    while max_num // pos > 0:
        counting_sort_numeros(arr, pos)
        pos *= 10

def counting_sort(arr):
    # counting sort para inteiros não-negativos (in-place)
    if not arr:
        return
    max_val = max(arr)
    n = len(arr)
    count = [0] * (max_val + 1)
    saida = [0] * n
    for num in arr:
        count[num] += 1
    for i in range(1, max_val + 1):
        count[i] += count[i - 1]
    for i in range(n - 1, -1, -1):
        saida[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
    for i in range(n):
        arr[i] = saida[i]

def insertion_sort(bucket):
    for i in range(1, len(bucket)):
        key = bucket[i]
        j = i - 1
        while j >= 0 and bucket[j] > key:
            bucket[j + 1] = bucket[j]
            j -= 1
        bucket[j + 1] = key

def bucket_sort(arr):


    min_val = min(arr)
    max_val = max(arr)

    if min_val == max_val:
        return arr

    n = len(arr)
    bucket_range = (max_val - min_val) / n
    buckets = [[] for _ in range(n + 1)]  
    for num in arr:

        if num == max_val:
            index = n - 1  
        else:
            index = int((num - min_val) / bucket_range) 
        buckets[index].append(num)

    for i in range(n):
        insertion_sort(buckets[i])

    k = 0
    for bucket in buckets: 
        for num in bucket: 
            arr[k] = num
            k += 1
