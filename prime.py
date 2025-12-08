num = int(input("enter the number :"))
count = 0
for i in range(1,num):
    if num%i == 0:
        count = count+1
if count > 2 :
    print("the given number is not a prime number")
else:
    print("the given number is a prime number")
