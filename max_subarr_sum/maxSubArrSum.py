class Solution:
    def kadane(self, arr):
        if not arr:
            return None

        current_sum = arr[0]
        max_sum = arr[0]

        for i in range(1, len(arr)):
            if current_sum <= 0:
                current_sum = arr[i]
            else:
                current_sum += arr[i]

            if current_sum > max_sum:
                max_sum = current_sum

        return max_sum


def main():
    arr = [3, -2, 5, -1, 6, -3]
    so = Solution()
    print(so.kadane(arr))


if __name__ == "__main__":
    main()
