Best Time to Buy and Sell Stock

This program finds the maximum profit that can be obtained by buying a stock on one day and selling it on a later day.

Problem

Given an array "arr" where:

- "arr[i]" represents the stock price on day "i".
- You can buy the stock only once.
- You can sell the stock only after buying it.
- Find the maximum possible profit.

Example

Input:
[6, 5, 4, 3, 2, 10]

Output:
8

The best transaction is:

Buy  →  2
Sell → 10

Profit = 10 - 2 = 8

Approach

The algorithm keeps track of:

- "buy" → the lowest stock price seen so far.
- "profit" → the maximum profit found so far.

For every price:

1. If the current price is greater than "buy", calculate the current profit.
2. Update "profit" if the current profit is greater.
3. If the current price is lower than "buy", update "buy".
4. Continue until the end of the array.

Code

class solution():
    def buySellStock(self, arr):
        buy = arr[0]
        sell = 0
        profit = 0

        for i in range(1, len(arr)):
            if not arr:
                return None

            if arr[i] > buy:
                sell = arr[i]
                currentProfit = sell - buy

                if currentProfit > profit:
                    profit = currentProfit
            else:
                buy = arr[i]

        return profit


def main():
    arr = [6, 5, 4, 3, 2, 10]

    so = solution()
    print(so.buySellStock(arr))


if __name__ == "__main__":
    main()

Output

8

Complexity

Time Complexity

O(n)

The array is traversed only once.

Space Complexity

O(1)

Only a few variables are used regardless of the input size.

Algorithm

1. Set buy = first element.
2. Set profit = 0.
3. Traverse the array from the second element.
4. If current price > buy:
      Calculate currentProfit = current price - buy
      Update maximum profit if necessary.
5. Otherwise:
      Update buy with the current price.
6. Return maximum profit.

Note

The check:

if not arr:

is currently inside the loop, so it cannot handle an empty array because "arr[0]" is accessed before the loop.

A safer version would check for an empty array at the beginning:

def buySellStock(self, arr):
    if not arr:
        return None

    buy = arr[0]
    profit = 0

    for i in range(1, len(arr)):
        if arr[i] > buy:
            profit = max(profit, arr[i] - buy)
        else:
            buy = arr[i]

    return profit