Binary Search

This program uses the Binary Search algorithm to find the index of a target element in a sorted array.

Problem

Given a sorted array and a target value, find the index of the target using Binary Search.

Example

Input:
arr = [2, 5, 8, 10, 14, 19, 22, 30]
target = 19

Output:
found in index 5

Since "19" is present at index "5", the program returns "5".

How Binary Search Works

Binary Search works by repeatedly dividing the search range into two halves.

1. Set "first" to the first index.
2. Set "last" to the last index.
3. Find the middle index.
4. Compare the middle element with the target.
5. If the target is greater:
   - Search the right half.
6. If the target is smaller:
   - Search the left half.
7. If the middle element equals the target:
   - Return its index.
8. If the search range becomes empty:
   - Return "-1".

Code

arr = [2, 5, 8, 10, 14, 19, 22, 30]
target = 19


def binary_search(arr, taregt):
    n = len(arr)
    first = 0
    last = n - 1

    while first <= last:
        middle = (last + first) // 2

        if target > arr[middle]:
            first = middle + 1

        elif target < arr[middle]:
            last = middle - 1

        elif target == arr[middle]:
            return middle

    return -1


index = binary_search(arr, target)

print(f"found in index {index}")

Output

found in index 5

Example Walkthrough

For:

arr = [2, 5, 8, 10, 14, 19, 22, 30]
target = 19

Step 1

first = 0
last = 7
middle = 3

arr[3] = 10

"19 > 10", so search the right half.

first = 4

Step 2

first = 4
last = 7
middle = 5

arr[5] = 19

Target found.

index = 5

Complexity

Time Complexity

O(log n)

The search space is divided by half during every iteration.

Space Complexity

O(1)

The iterative implementation uses only a constant amount of extra memory.

Important Requirement

Binary Search requires the array to be sorted.

For example:

Correct:
[2, 5, 8, 10, 14, 19, 22, 30]

Incorrect:
[10, 2, 19, 5, 30, 8]

Note

There is a small typo in the function parameter:

def binary_search(arr, taregt):

It should be:

def binary_search(arr, target):

Also, the function currently uses the global "target" variable instead of its parameter. A cleaner version is:

def binary_search(arr, target):
    first = 0
    last = len(arr) - 1

    while first <= last:
        middle = (first + last) // 2

        if target > arr[middle]:
            first = middle + 1
        elif target < arr[middle]:
            last = middle - 1
        else:
            return middle

    return -1