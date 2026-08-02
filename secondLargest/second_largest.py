#------------------------------------------------------------------------------finding the second largset number and index------------------------------------------------------------------

from bubble_sort import bubble_sort

def index_second_largest(arr):
    n=len(arr)
    index_dict={}
    i=0
    for i in range(n):
        index_dict[arr[i]]=i
    sec_largest=second_largest(arr)
    return index_dict[sec_largest]


def second_largest(arr):
    yarr=arr
    n=len(yarr)
    sorted_arr=bubble_sort(yarr)
    second_largest=sorted_arr[n-2]
    return second_largest

def main():
    arr=[64,25,12,22,11]
    yarr=[64,25,12,22,11]
    print(f"The second largest number is :{second_largest(arr)}")
    print(f"The index is :{index_second_largest(yarr)}")

if __name__ == "__main__":
    main()


