def bin_search(arr, low, high, key):
    while(low<=high):
        mid = (low+high)//2
        if(key < arr[mid]):
            high = mid-1
        elif (key>arr[mid]):
            low = mid+1
        else:
            return mid
        
arr=[1,5,6,9,11]
key = 1
result = bin_search(arr,0,len(arr)-1,key)
if(result!=-1):
    print("found at: ",result)
else:
    print("result is not found")