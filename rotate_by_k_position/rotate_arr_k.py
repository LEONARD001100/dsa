def rotateBy_kPos(arr,k):
    if not arr:
        return arr
    length=len(arr)
    l=k
    diff=length-k
    d=diff
    save=[]
    for i in range(k):
        save.append(arr[i])
    for i in range(diff):
        arr[i]=arr[l]
        l+=1
    for i in range(k):
        arr[d]=save[i]
        d+=1
    return arr

def rotateBy_kPos_optimized(arr,k):
    if not arr:
        return arr
    k=k % len(arr)
    arr=reversefn(arr,0,k-1)
    arr=reversefn(arr,k,len(arr)-1)
    arr=reversefn(arr,0,len(arr)-1)
    return arr

def reversefn(arr,start,end):
    while start < end :
        arr[start],arr[end]=arr[end],arr[start]
        start+=1
        end-=1
    return arr


def main():
    yarr=[1,2,3,4,5,6,7]
    arr=[1,2,3,4,5,6,7]
    k=4
    print(rotateBy_kPos(yarr,k))
    print(rotateBy_kPos_optimized(arr,k))

if __name__ == "__main__":
    main()

