#bubble sort

def bubble_sort(arr):
    yarr=arr
    n=len(yarr)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if yarr[j]>yarr[j+1]:
                yarr[j],yarr[j+1]=yarr[j+1],arr[j]
    return yarr
   
def main():
    arr = [5, 1, 4, 2, 8]
    yyarr=bubble_sort(arr)
    print(yyarr)

if __name__ == "__main__":
    main()
