def mv_zero_to_end(arr):
    length=len(arr)
    #zero<-----pointer
    #non_zero<--------pointer
    zero=0
    for current in range(length):
            if arr[current] != 0:
                arr[zero],arr[current]=arr[current],arr[zero]
                zero+=1
    return arr
def main():
    arr = [2, 1, 0, 3, 12]
    print(mv_zero_to_end(arr))
if __name__ == "__main__":
    main()

























































