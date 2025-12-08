num = int(input("enter a number:"))
count = 0
square = num**2
temp = num
while temp > 0:
    temp = temp // 10
    count = count+1
if square % (10**count) == num:
    print("the given number is automorphic number")
else:
    print("the given number i not an automorphic number")