def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    input_list = mergeSort(input_list)
    result = [0,0]
    is_right = False
    for ele in input_list:
        ele = str(ele)
        if is_right:
            result[1] = int(str(result[1]) + ele) ##append element not add
            is_right = False
        else:
            result[0] = int(str(result[0]) + ele) ##append element not add
            is_right = True
    return result

def mergeSort(arr):
    if len(arr) == 1:
        return arr
    a = mergeSort(arr[0:(len(arr) // 2)])
    b = mergeSort(arr[(len(arr) // 2):])
    return merge(a, b)

def merge(a, b):
    """
    Clasical merge section of merge sort, but we are sorting in descending order
    """
    result = []
    while a and len(a) > 0 and b and len(b) > 0:
        if a[0] > b[0]:
            result.append(a.pop(0))
        else:
            result.append(b.pop(0))
    while a and len(a) > 0:
        result.append(a.pop(0))
    while b and len(b) > 0:
        result.append(b.pop(0))
    
    return result

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[0,0], [0, 0]])