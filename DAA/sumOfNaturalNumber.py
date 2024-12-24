import time
import matplotlib.pyplot as plt

# Time For Each Algorithm
sumAlgorithm1Time = []
sumAlgorithm2Time = []

# Sum Algorithm Using Loop
def sumAlgorithm1(n):
    sum = 0
    startTime = time.perf_counter()
    for i in range(1,n+1):
        sum += i
    endTime = time.perf_counter()
    timeUsed = endTime - startTime
    sumAlgorithm1Time.append(timeUsed)
    print("The Sum Of Natural Number From 1 To ",n,"Is ",sum,)
    print("Time Used ",timeUsed)

# Sum Algorithm Using Formula
def sumAlgorithm2(n):
    startTime = time.perf_counter()
    sum = (n * (n + 1)) / 2
    endTime = time.perf_counter()
    timeUsed = endTime - startTime
    sumAlgorithm2Time.append(timeUsed)
    print("The Sum Of Natural Number From 1 To ",n,"Is ",sum)
    print("Time Used ",timeUsed)
# For Testing Function    
#sumAlgorithm1(100000)
#sumAlgorithm2(100000)

# Creating Input List
inputList = range(1,250000,50000)

# Runing The Algorithm
for input in inputList:
    sumAlgorithm1(input)
    sumAlgorithm2(input)


# Plotting the time comparison between both algorithms
plt.plot(inputList, sumAlgorithm1Time, label="Algorithm 1 (Loop)", color='blue')
plt.plot(inputList, sumAlgorithm2Time, label="Algorithm 2 (Formula)", color='red')

plt.xlabel("Value of n")
plt.ylabel("Time (seconds)")
plt.title("Comparison of Sum Algorithms")
plt.legend()
plt.show()
