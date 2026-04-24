def bubble_sort(arr):
    tam = len(arr)
    for i in range(tam):
        for j in range(tam - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print(arr)


def main():
    array = [2,7,0,3,4,6,1,5]
    bubble_sort(array)

main()