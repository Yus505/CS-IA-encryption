def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1  # target not found

# Example usage
my_list = [6, 10, 3, 12, 21, 9]
target_element = 9
index = linear_search(my_list, target_element)
if index != -1:
    print(f"The index of {target_element} in the list is {index}")
else:
    print(f"{target_element} is not found in the list.")
