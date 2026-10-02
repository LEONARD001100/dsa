Check if Array is Sorted

This program checks whether an array is sorted in ascending order.

Problem

Given an array of integers, determine whether the elements are arranged in ascending order.

The function returns:

- "True" → if the array is sorted in ascending order.
- "False" → if the array is not sorted in ascending order.

Example

Input:
[1, 2, 3, 5, 4]

Output:
False

The array is not sorted because:

5 > 4

Approach

The program compares each element with the element immediately after it.

For every index "i":

arr[i] > arr[i + 1]

If this condition is true, the array is not sorted, so the function immediately returns "False".

If no such pair is found, the function returns "True".

Code

def check_array_sorted_ascending(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False

    return True


def main():
    arr = [1, 2, 3, 5, 4]
    print(check_array_sorted_ascending(arr))


if __name__ == "__main__":
    main()

Output

False

Example Walkthrough

For:

[1, 2, 3, 5, 4]

The program checks adjacent elements:

1 < 2  → Correct
2 < 3  → Correct
3 < 5  → Correct
5 > 4  → Not sorted

As soon as "5 > 4" is detected, the function returns:

False

Another Example

arr = [1, 2, 3, 4, 5]

print(check_array_sorted_ascending(arr))

Output:

True

Algorithm

1. Start from the first element.
2. Compare the current element with the next element.
3. If current element > next element:
      Return False.
4. Continue until the second-last element.
5. If no decreasing pair is found:
      Return True.

Complexity

Time Complexity

O(n)

In the worst case, every element needs to be checked.

The algorithm can terminate early if it finds an unsorted pair.

Space Complexity

O(1)

Only a loop variable is used, so no additional array or data structure is required.

Key Concept

An array is sorted in ascending order if:

arr[i] <= arr[i + 1]

for every valid index "i".

Therefore, finding even one pair where:

arr[i] > arr[i + 1]

is enough to conclude that the array is not sorted.