class solution():

    def prifixSum(self, arr, queries, n):
        prifix = [arr[0]]
        summ = arr[0]

        for i in range(1, len(arr)):
            summ += arr[i]
            prifix.append(summ)

        for i in range(n):
            a = queries[i][0]
            b = queries[i][1]

            if a == 0:
                print(f"sum of the index {a} to {b} is : {prifix[b]}")
            else:
                print(
                    f"sum of the index {a} to {b} is : "
                    f"{prifix[b] - prifix[a-1]}"
                )


def main():
    print("Enter the array elements")
    arr = list(map(int, input().split()))

    n = int(input("Enter the number of queries : "))

    queries = []

    for _ in range(n):
        query = list(map(int, input().split()))
        queries.append(query)

    so = solution()
    so.prifixSum(arr, queries, n)


if __name__ == "__main__":
    main()
