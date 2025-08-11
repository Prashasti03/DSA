def selectionSort(arr):
    size = len(arr)
    for i in range(size):
        min_index=i
        for j in range(i+1, size):
            if (arr[j]<arr[min_index]):
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
        
        

arr = [1, 34, 52, 22, 67, 34, 5, 8, 3]
selectionSort(arr)
for i in range(len(arr)):
    print(arr[i], end=' ')