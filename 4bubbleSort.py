#ma'ams way
def bubbleSort(arr):
    # for i in range(len(arr)-1,0,-1):
    #     for j in range(i):
    #         if arr[j]>arr[j+1]:
    #             arr[j],arr[j+1]=arr[j+1],arr[j]

#W3schools's way
    n = len(arr)
    for i in range(n-1):
        swapped = False       # these lines are used if the array is sorted before the loop is      completed, so we don’t have to complete the whole loop
        for j in range(n-i-1):
            if arr[j] > arr [j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True     #
        if not swapped:             #
            break                          #

    # print("Sorted array:", arr)


arr = [1, 34, 52, 22, 67, 34, 5, 8, 3]
bubbleSort(arr)
for i in range(len(arr)):
    print(arr[i], end=' ')