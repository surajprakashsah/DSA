def binary_search(arr,i,j,x):
    if j>=i:
        mid=(i+j)//2
        if arr[mid] == x:
            return mid
        elif arr[mid]>x:
            return binary_search(arr,i,mid-1,x)
        else :
            return binary_search(arr,mid+1,j,x)
    else:
        return -1
arr=[2,3,4,5,6,7,8,9]
x=10
result=binary_search(arr,0,len(arr)-1,x)
if result !=-1:
    print("Element is present in index ",str(result))
else:
    print("Element is not present in index")


