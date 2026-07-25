
arr = [2,5,8,10,14,19,22,30]
target = 19

def binary_search(arr,taregt):
    n=len(arr)
    first=0
    last=n-1

    while (first<=last):
        middle=(last+first)//2
        if (target>arr[middle]):
            first=middle+1
        elif (target<arr[middle]):
            last=middle-1
        elif (target==arr[middle]):
            found=True
            return middle
    return -1

index=binary_search(arr,target)

print(f"found in index {index}")
