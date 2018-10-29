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


print(sys.version)
print("HI MOM!")

# grade average





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
    for i in range(0,len(nums)):
        for j in range (i,len(nums)):
            if (nums[i] > nums[j]):
                return False
    return True

def test_sort ():
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
sys.exit (0)

