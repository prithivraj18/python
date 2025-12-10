string = input("enter a string:")
rev = ""
for i in range(len(string)-1,-1,-1):
    rev = rev+string[i]
print("the reversed string is:",rev)
if rev == string:
    print("the given string is a palindrome !")
else:
    print("the given string is not a palindrome !")