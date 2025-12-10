def prime(n):
    count = 0
    for i in range(1, n):
        if n % i == 0:
            count = count + 1
    if count >= 2:
        print("the given number is not a prime number")
    else:
        print("the given number is prime number:")


number = int(input("enter a number:"))
prime(number)