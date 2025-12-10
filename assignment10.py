def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
number = int(input("enter the number to find the factorial:"))
print("the factorial of",number,"is",factorial(number))