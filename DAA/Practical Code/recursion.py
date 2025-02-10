# Factorial
def factorial(n):
    if n < 0:
        return False
    if n <= 1:
        return n
    return n * factorial(n-1)
print("The Factorial Of 5: ",factorial(5))
print("The Factorial Of 10: ",factorial(10))
print("The Factorial Of 15: ",factorial(15))

# Fibonacci

def fibonacci(n):
    if n < 0:
        return False
    if n <= 1:
        return n
    return fibonacci(n-2)+fibonacci(n-1)

n = int(input("Enter A Number For Fibonacci Series : "))
for i in range(0,n+1):
    print(fibonacci(i),end =" ")
    
    
