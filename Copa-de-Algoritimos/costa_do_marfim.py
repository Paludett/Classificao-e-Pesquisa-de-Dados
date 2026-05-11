def Costa_do_Marfim(arr):  

    n = len(arr)
    if n <= 1:
        return arr

    #  Insertion para subarrays pequenos 
    def insertion(a, left, right):
        for i in range(left + 1, right + 1):
            key = a[i]
            j = i - 1
            while j >= left and a[j] > key:
                a[j + 1] = a[j]
                j -= 1
            a[j + 1] = key

    # counting sort para range pequeno
    def counting(a, mn, mx):
        size = mx - mn + 1
        count = [0] * size
        for x in a:
            count[x - mn] += 1
        idx = 0
        for i in range(size):
            while count[i] > 0:
                a[idx] = i + mn
                idx += 1
                count[i] -= 1

    # merge sort
    def merge_sort(a, left, right):
        if right - left <= 16:
            insertion(a, left, right)
            return
        mid = (left + right) // 2
        merge_sort(a, left, mid)
        merge_sort(a, mid + 1, right)
        buf = a[left:right + 1]
        i, j, k = 0, mid - left + 1, left
        end_l, end_r = mid - left + 1, right - left + 1
        while i < end_l and j < end_r:
            if buf[i] <= buf[j]:
                a[k] = buf[i]; i += 1
            else:
                a[k] = buf[j]; j += 1
            k += 1
        while i < end_l:
            a[k] = buf[i]; i += 1; k += 1
        while j < end_r:
            a[k] = buf[j]; j += 1; k += 1

    def heapify(a, n_h, i):
        largest = i
        l, r = 2 * i + 1, 2 * i + 2
        if l < n_h and a[l] > a[largest]:
            largest = l
        if r < n_h and a[r] > a[largest]:
            largest = r
        if largest != i:
            a[i], a[largest] = a[largest], a[i]
            heapify(a, n_h, largest)

    def heap_sort(a, left, right):
        sub = a[left:right + 1]
        n_h = len(sub)
        for i in range(n_h // 2 - 1, -1, -1):
            heapify(sub, n_h, i)
        for i in range(n_h - 1, 0, -1):
            sub[0], sub[i] = sub[i], sub[0]
            heapify(sub, i, 0)
        a[left:right + 1] = sub

    def media_de_tres(a, l, r):
        m = (l + r) // 2
        if a[l] > a[m]: a[l], a[m] = a[m], a[l]
        if a[l] > a[r]: a[l], a[r] = a[r], a[l]
        if a[m] > a[r]: a[m], a[r] = a[r], a[m]
        a[m], a[r - 1] = a[r - 1], a[m]
        return a[r - 1]

    def introsort(a, left, right, depth_limit):
        size = right - left + 1
        if size <= 16:
            insertion(a, left, right)
            return
        if depth_limit == 0:
            heap_sort(a, left, right)
            return
        pivo = media_de_tres(a, left, right)
        i, j = left, right - 1
        while True:
            i += 1
            while a[i] < pivo: i += 1
            j -= 1
            while a[j] > pivo: j -= 1
            if i >= j: break
            a[i], a[j] = a[j], a[i]
        a[i], a[right - 1] = a[right - 1], a[i]
        introsort(a, left, i - 1, depth_limit - 1)
        introsort(a, i + 1, right, depth_limit - 1)

    # detecção de cenário

    # verifica se já ordenado (cresente)
    sorted_flag = True
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            sorted_flag = False
            break
    if sorted_flag:
        return arr

    # verifica se já ordenado (decresente)
    reversed_flag = True
    for i in range(n - 1):
        if arr[i] < arr[i + 1]:
            reversed_flag = False
            break
    if reversed_flag:
        left, right = 0, n - 1
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1; right -= 1
        return arr

    # verifica se o range é pequeno, se for leva pro counting
    mn = arr[0]
    mx = arr[0]
    for x in arr:
        if x < mn: mn = x
        if x > mx: mx = x
    value_range = mx - mn

    if value_range <= 200:         
        counting(arr, mn, mx)
        return arr

    # verifica se o array é grande, se for leva pro Merge Sort 
    if n >= 100_000:
        merge_sort(arr, 0, n - 1)
        return arr

    # se o array for médio leva pro quick/heap sort hibrido (introsort)
    import math
    depth_limit = 2 * int(math.log2(n))
    introsort(arr, 0, n - 1, depth_limit)

    return arr  
