arr=[12,4,7,9,15]

target=9

def index_of_target(arr,target):
    found=False
    for i in range(len(arr)-1):
        if arr[i]==target:
            found=True
            return i
        else:
            continue
    if not found:
        return -1
index=index_of_target(arr,target)

print(index)

    
