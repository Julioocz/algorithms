def insertion_sort(array):
    for slot in range(1, len(array)):
        element = array[slot]
        for sorted_slot in range(slot - 1, -1, -1):
            sorted_element = array[sorted_slot]
            if element < sorted_element:
                array[sorted_slot] = element
                array[sorted_slot + 1] = sorted_element
            elif element >= sorted_element:
                break

    return array

def selection_sort(array):
    for slot in range(0, len(array)):
        min_val = None
        prev_min_val_index = None
        for i in range(slot, len(array)):
            curr = array[i]
            if min_val is None or min_val > array[i]:
                min_val, prev_min_val_index = curr, i

        buffer = array[slot]
        array[slot] = min_val
        array[prev_min_val_index] = buffer

    return array


def bubble_sort(array):
    swap = True
    while swap:
        swap = False
        for i in range(1, len(array)):
            prev = array[i - 1]
            curr = array[i]
            if prev > curr:
                array[i] = prev
                array[i - 1] = curr
                swap = True

    return array
