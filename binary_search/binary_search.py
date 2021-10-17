# Binary Search:
# Search algorithm that finds the position of a target value within a sorted array.
# Binary search compares the target value to the middle element of the array.

def binary_search(sequence, item):
    begin_index = 0
    end_index = len(sequence) - 1

    while begin_index <= end_index:
        midpoint = begin_index + (end_index - begin_index) // 2
        midpoint_value = sequence[midpoint]

        if midpoint_value == item:
            return midpoint
        elif item < midpoint_value:
            end_index = midpoint - 1

        else:
            begin_index = midpoint + 1

    return None


# Array to search (sorted)
sequence_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Item to find in the array
item_a = 12

print()
print('Input: ', sequence_a)
print('Item to search: ', item_a)
print('Found at position ', binary_search(sequence_a, item_a))
