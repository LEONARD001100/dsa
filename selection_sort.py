arr=[64,25,12,22,11]

def selection_sort(arr):
    n=len(arr)
    for i in range(n-1):
        index=index_of_smallest(arr[i:])+i
        arr[i],arr[index]=arr[index],arr[i]
    return arr

def index_of_smallest(arr):
    n=len(arr)
    small=arr[0]
    index=0
    for j in range(n):
        if arr[j]<small:
            small=arr[j]
            index=j
    return index

print(selection_sort(arr))

