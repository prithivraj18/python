n = int(input("enter the number:"))
t = n
a = 0

while n != 0:
    r = n % 10
    a = a + (r**3)
    n = n // 10

if t == a:
    print("the given number is an armstrong number")
else:
    print("the given number is not an armstrong number")

        
