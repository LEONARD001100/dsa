def second_largest(arr):
    if len(arr)<2:
        return None
    largest=arr[0]
    second_largest=None
    for current in arr:
        if current >largest:
            second_largest=largest
            largest=current
        elif current != largest and (second_largest is None or current > second_largest):
            second_largest=current
    return second_largest

def main():
    arr=[64,25,12,22,11]
    print(second_largest(arr))

if __name__ == "__main__":
    main()
        
