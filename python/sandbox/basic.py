import sys

def average(scores):
    if len(scores) == 0 :
        return 0.0
    sum = 0.0
    for score in scores:
        sum += score
    average = sum / len(scores)
    return average
def test_average ():
    if average([91.0, 89.0, 77.0, 96.0, 94.0]) != 89.4:
        return False
    if average([98.0, 100.0, 100.0, 97.0, 99.0, 95.0, 99.0, 100.0]) != 98.5:
        return False
    if average([78.0, 90.0, 85.0, 88.9]) != 85.475:
        return False
    if average([])!=0.0:
        return False
    return True
def calculate_median(l):
    l = sorted(l)
    l_len = len(l)
    if l_len < 1:
        return None
    if l_len % 2 == 0 :
        return ( l[(int)((l_len-1)/2)] + l[(int)((l_len+1)/2)] ) / 2.0
    else:
        return l[(int)((l_len-1)/2)]
def test_median ():
    if (calculate_median([3,1,2]) )!= 2:
        return False
    if (calculate_median([4,3,1,2]) )!= 2.5:
        return False
    if (calculate_median([1,1,1,1,1]) )!= 1:
        return False
    return True
def sort(nums):
    if (len(nums) == 0) or (len(nums) == 1):
        return nums
    for i in range(0,len(nums)):
        for j in range (i,len(nums)):
            if (nums[i] > nums[j]):
                tmp = nums[j]
                nums[j] = nums[i]
                nums[i] = tmp
    return nums

def issorted(nums):
    if (len(nums) == 0) or (len(nums) == 1):
        return True
    for i in range(0,len(nums)-1):
        if (nums[i] > nums[i+1]):
            return False
    return True

def test_sort ():
    if not issorted ([1,1,1,1]):
        return False
    if sort ([5,4,7,10]) != [4,5,7,10]:
        return False
    if issorted([5,4,7,10]):
        return False
    return True
if (not test_average ()):
    print ("AVERAGE FAILED")
    sys.exit(1)
if (not test_sort ()):
    print ("SORT FAILED")
    sys.exit(2)
if (not test_median ()):
    print ("MEDIAN FAILED")
    sys.exit(3)
sys.exit (0)