def insertionSort(arr):
    size =len(arr)
    for i in range(1,size):
        key = arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key

arr = [100, 34, 52, 22, 67, 34, 5, 8, 3]
insertionSort(arr)
for i in range(len(arr)):
    print(arr[i], end=' ')