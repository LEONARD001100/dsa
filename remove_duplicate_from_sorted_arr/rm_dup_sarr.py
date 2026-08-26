class Solution:

    def duplicateRemover(self, arr):
        n = len(arr)

        if n == 0:
            return 0

        if n == 1:
            return 1

        mptr = 1
        cptr = 1
        count = 1
        element = arr[0]

        for i in range(1, n):

            if element != arr[cptr]:
                element = arr[cptr]

                arr[mptr] = arr[cptr]

                count += 1
                mptr += 1

            cptr += 1

        return count


def main():
    arr = list(map(int, input().split()))

    so = Solution()

    count = so.duplicateRemover(arr)

    print("Number of unique elements:", count)
    print("Array:", arr)


if __name__ == "__main__":
    main()
