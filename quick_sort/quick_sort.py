# QuickSort:
# Will take one pivot number, comapre left to right if greater or smaller,
# repeat until solved

def quick_sort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()

    items_greater = []
    items_lower = []

    for item in sequence:
        if item > pivot:
            items_greater.append(item)

        else:
            items_lower.append(item)

    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)

# Array to sort
array = [1,4,2,3,6,5,7,9,8,0]

print()
print('Input: ',array)
print('Output: ',quick_sort(array))