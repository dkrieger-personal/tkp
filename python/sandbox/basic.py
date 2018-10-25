import sys

def average(scores):
    if len(scores) == 0 :
        return 0.0
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


alex = [91.0, 89.0, 77.0, 96.0,94.0]

print("AVERAGE OF " +  str(len(alex)) + " : " + str(average(alex)))

david = []
print("AVERAGE OF " +  str(len(david)) + " : " + str(average(david)))