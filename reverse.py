num = int(input("enter a number"))
temp = num
rev = 0
while num!= 0 :
    rem = num % 10
    rev = rev*10+rem
    num = num // 10
print("the reverse of the given number is: ",rev)
    

