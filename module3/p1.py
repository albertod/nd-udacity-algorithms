# My first solution was to do a for loop that went from i=0 to n and tested if i was the sqrt(i) -> i * i == number, this loop increased i by i * i in every iteraction
# The runtime was O(sqrt(n)). As the intructions says we need a lower runtime, I thought then about binary search.

# My current solution uses binary search, instead of using an array to look for values I decided to search with the domain of number 0 to number, testing my candidate
# mid in every iteraction. As I'm halving my search space by n/(2^k) we know that the run time of this while loop k times -> k = log(n).


def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    try:
        number = int(number)
        if number < 0:
            return None # SQRT of negative number are imaginary numbers
        l = 0
        r = number
        while l <= r:
            mid  = l + ((r - l) // 2)
            if mid * mid == number:
                return mid
            if mid * mid < number:
                l = mid + 1
            else:
                r = mid - 1
        return mid
    except ValueError:
        return None

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
print ("Pass" if  (None == sqrt('hello')) else "Fail")