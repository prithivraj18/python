num = int(input("enter the number to be reverses:"))
temp = num
rev = 0
while num != 0:
    rem = num % 10
    num = num //10
    rev = rev * 10 + rem
print("the reversed number is",rev)
if rev == temp:
    print("the given number is an palindrome")
else:
    print("the goven number is not an palindrome")