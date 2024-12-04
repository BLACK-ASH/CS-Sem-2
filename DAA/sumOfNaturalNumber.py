import time

# Sum Algorithm Using Loop
def sumAlgorithm1(n):
    sum = 0
    startTime = time.perf_counter()
    for i in range(1,n+1):
        sum += i
    endTime = time.perf_counter()
    timeUsed = endTime - startTime
    print("The Sum Of Natural Number From 1 To ",n,"Is ",sum,)
    print("Time Used ",timeUsed)

# Sum Algorithm Using Formula
def sumAlgorithm2(n):
    sum = 0
    startTime = time.perf_counter()
    sum = (n * (n + 1)) / 2
    endTime = time.perf_counter()
    timeUsed = endTime - startTime
    print("The Sum Of Natural Number From 1 To ",n,"Is ",sum)
    print("Time Used ",timeUsed)
    
