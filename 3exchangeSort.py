def exchangeSort(arr):
    size = len(arr)
    for i in range(size-1):
        for j in range(i+1, size):
            if arr[i]>arr[j]:
                arr[i],arr[j] = arr[j],arr[i]

arr = [34, 4, 43, 6, 33, 6]
exchangeSort(arr)
for i in range(len(arr)):
    print(arr[i], end=' ')