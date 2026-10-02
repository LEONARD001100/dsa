Bubble Sort

This program implements the Bubble Sort algorithm in Python to sort an array in ascending order.

Problem

Given an unsorted array, arrange its elements in ascending order using Bubble Sort.

Example

Input:
[5, 1, 4, 2, 8]

Output:
[1, 2, 4, 5, 8]

How Bubble Sort Works

Bubble Sort repeatedly compares two adjacent elements.

- If the left element is greater than the right element, they are swapped.
- After each complete pass, the largest unsorted element moves to the end of the array.
- The process continues until the entire array is sorted.

Code

# bubble sort

def bubble_sort(arr):
    yarr = arr
    n = len(yarr)

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if yarr[j] > yarr[j + 1]:
                yarr[j], yarr[j + 1] = yarr[j + 1], arr[j]

    return yarr


def main():
    arr = [5, 1, 4, 2, 8]
    yyarr = bubble_sort(arr)
    print(yyarr)


if __name__ == "__main__":
    main()

Output

[1, 2, 4, 5, 8]

Algorithm

1. Start with the unsorted array.
2. Compare adjacent elements.
3. If the first element is greater than the second:
      Swap them.
4. Continue comparing adjacent elements until the end.
5. The largest element reaches the end of the unsorted portion.
6. Repeat the process for the remaining elements.
7. Return the sorted array.

Example Walkthrough

Given:

[5, 1, 4, 2, 8]

Pass 1

5 > 1  → [1, 5, 4, 2, 8]
5 > 4  → [1, 4, 5, 2, 8]
5 > 2  → [1, 4, 2, 5, 8]
5 < 8  → [1, 4, 2, 5, 8]

The largest element "8" is now at the end.

Pass 2

1 < 4  → [1, 4, 2, 5, 8]
4 > 2  → [1, 2, 4, 5, 8]
4 < 5  → [1, 2, 4, 5, 8]

Pass 3

1 < 2
2 < 4

The array is sorted:

[1, 2, 4, 5, 8]

Complexity

Time Complexity

Worst case:

O(n²)

Average case:

O(n²)

Best case:

O(n²)

for the current implementation because it does not stop early when the array is already sorted.

Space Complexity

O(1)

Bubble Sort sorts the array in place and requires constant extra space.

Important Note About the Code

There is a small issue in the swap statement:

yarr[j], yarr[j + 1] = yarr[j + 1], arr[j]

It is better to use "yarr" consistently:

yarr[j], yarr[j + 1] = yarr[j + 1], yarr[j]

In this particular program, "arr" and "yarr" refer to the same list, so the code still works. However, using the same variable makes the logic clearer.

Also:

yarr = arr

does not create a copy. Both variables refer to the same list.

If you want a separate copy, use:

yarr = arr.copy()

Improved Version

def bubble_sort(arr):
    yarr = arr.copy()
    n = len(yarr)

    for i in range(n - 1):
        for j in range(n - i - 1):
            if yarr[j] > yarr[j + 1]:
                yarr[j], yarr[j + 1] = yarr[j + 1], yarr[j]

    return yarr


def main():
    arr = [5, 1, 4, 2, 8]
    yyarr = bubble_sort(arr)
    print(yyarr)


if __name__ == "__main__":
    main()

Output

[1, 2, 4, 5, 8]