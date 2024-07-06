import random

def branchPrediction():
    count = 0
    arr = [random.randint(1,100) for e in range(10000000)]
    for e in arr:
        if e >= 50:
            count += 1
    print(count)

def branchPrediction2():
    count = 0
    arr = sorted([random.randint(1,100) for e in range(10000000)])
    for e in arr:
        if e >= 50:
            count += 1
    print(count)

branchPrediction2()    