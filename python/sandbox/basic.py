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



