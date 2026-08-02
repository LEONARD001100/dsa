def check_array_sorted_ascending(arr):
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            return False
    return True


def main():
    arr = [1, 2, 3, 5, 4]
    print(check_array_sorted_ascending(arr))

if __name__ == "__main__":
    main()


