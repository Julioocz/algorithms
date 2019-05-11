def brute_force_inversion_counter(array):
    inversions = 0
    for i, element in enumerate(array):
        for j in range(i + 1, len(array)):
            inner_element = array[j]
            if element > inner_element:
                inversions += 1
    return inversions


def merge_and_count_split_inversions(left_array, right_array):
    j = 0
    i = 0
    result = []
    inversions_count = 0
    for k in range(len(left_array) + len(right_array)):
        if i == len(left_array):
            result.extend(right_array[j:])
            break
        elif j == len(right_array):
            result.extend(left_array[i:])
            break

        left_el = left_array[i]
        right_el = right_array[j]
        if left_el <= right_el:
            result.append(left_el)
            i += 1
        elif right_el < left_el:
            result.append(right_el)
            inversions_count += len(left_array) - i
            j += 1

    return inversions_count, result


def recursive_inversions_counter(array):
    if len(array) == 1:
        return 0, array

    half = len(array) // 2
    left_count, left_sorted = recursive_inversions_counter(array[:half])
    right_count, right_sorted = recursive_inversions_counter(array[half:])
    split_count, merged_array = merge_and_count_split_inversions(
        left_sorted, right_sorted
    )
    return left_count + right_count + split_count, merged_array


def inversions_counter(array):
    return recursive_inversions_counter(array)[0]


test_array = [1, 3, 5, 2, 4, 6]
print(brute_force_inversion_counter(test_array))
