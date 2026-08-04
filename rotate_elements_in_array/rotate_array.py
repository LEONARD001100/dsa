def rotate_array_lr(arr):
    save=arr[0]
    current=0
    nextt=1
    length=len(arr)
    while nextt < length:
        arr[current]=arr[nextt]
        current+=1
        nextt+=1
    arr[length-1]=save
    return arr

def rotate_array_rl(arr):
    length=len(arr)
    save=arr[length-1]
    current=length-1
    nextt=length-2
    while nextt>=0:
        arr[current]=arr[nextt]
        current-=1
        nextt-=1
    arr[0]=save
    return arr

def main():
    arr = [1, 2, 3, 4, 5]
    yarr= [1, 2, 3, 4, 5]
    print(rotate_array_lr(arr))
    print(rotate_array_rl(yarr))

if __name__ == "__main__":
    main()

