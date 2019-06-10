def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if not ints or len(ints) == 0:
        return None # Handle invalid cases
    result = [ints[0], ints[0]]
    for ele in ints[1:]:
        if result[0] > ele:
            result[0] = ele
        elif result[1] < ele:
            result[1] = ele
    print(result)
    return tuple(result)
        

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 100)]  # a list containing 0 - 99
random.shuffle(l)
print ("Pass" if ((0, 99) == get_min_max(l)) else "Fail")

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

l = [i for i in range(0, 6)]  # a list containing 0 - 5
random.shuffle(l)
print ("Pass" if ((0, 5) == get_min_max(l)) else "Fail")