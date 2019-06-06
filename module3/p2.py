# For this problem I assumed I had 2 sorted arrays in my initial array. Using binary search will give me the runtime of O(log(n)). But with the edge case that the
# array might be rotated, to account for this I cheked on the first iteraction if mid < num  -> before taking the right half of the array, check the last element.
# If the last element was still < mid then there wasn't a point of keep checking as the num won't be on that half, so check the left half of the array instead.

def rotated_array_search(arr, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    left = 0
    right = len(arr) - 1
    have_rotated = False

    while left <= right:

        mid = (left + (right - left) // 2)
        
        if arr[mid] == number:
            return mid
        
        if arr[mid] < number:
            if (not have_rotated) and arr[right] < number:
                have_rotated = True
                right = mid - 1
                continue
            left = mid + 1
        else:
            if (not have_rotated) and arr[left] > number:
                have_rotated = True
                left = mid + 1
                continue
            right = mid - 1
        
    return -1

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])