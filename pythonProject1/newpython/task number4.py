lst = [21, 12, 10, 9, 6, 3]
target = 9

def binary_search(lst, target):
    left = 0
    right = len(lst) - 1

    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] > target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# Example usage
index = binary_search(lst, target)
print(index)  # Output: 3
