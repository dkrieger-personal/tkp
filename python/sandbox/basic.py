import sys

def average(scores):
    sum = 0.0
    for score in scores:
        sum += score
    average = sum / len(scores)
    return average


print(sys.version)
print("HI MOM!")

# grade average
scores = [98.0, 100.0, 100.0, 97.0, 99.0, 95.0,99.0, 100.0]
evan = [78.0, 90.0, 85.0, 88.9]


print("AVERAGE OF " + str(len(scores)) + " : " + str(average(scores)))
print("AVERAGE OF " + str(len(evan)) + " : " + str(average(evan)))

def sort(nums):
    if (len(nums) == 0) or (len(nums) == 1):
        return nums
    for i in range(0,len(nums)):
        for j in range (i,len(nums)):
            if (nums[i] > nums[j]):
                tmp = nums[j]
                nums[j] = nums[i]
                nums[i] = tmp

def issorted(nums):
    if (len(nums) == 0) or (len(nums) == 1):
        return True
    for i in range(0,len(nums)):
        for j in range (i,len(nums)):
            if (nums[i] > nums[j]):
                return False
    return True


nums = [5,4,7,10]
for num in nums:
    print(num)
sort(nums)
print("SORT:")
for num in nums:
    print(num)
print(issorted(nums))


