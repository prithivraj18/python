n = int(input("enter a number:"))
temp = n
rem = 0
sum = 0
for i in range (1,n):
    rem = n%10
    sum = sum+rem
    n = n // 10
print("the sum of digit is:",sum)
    