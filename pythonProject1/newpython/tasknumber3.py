lst = [6, 10, 3, 12, 21, 9]

def bubble_sort_descending(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] < lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

# Example usage
sorted_lst = bubble_sort_descending(lst)
print(sorted_lst)   # Output: [21, 12, 10, 9, 6, 3]
