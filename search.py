def linear_search(elements, target):
    for el in elements:
        if target == el:
            return True
    
    return False

def binary_search(elements, target):
    middle = len(elements) // 2
    middle_element = elements[middle]
    if middle_element == target:
        return True
    
    if len(elements) <=1:
        return False

    if middle_element > target:
        return binary_search(elements[:middle], target)
    else:
        return binary_search(elements[middle:], target)
