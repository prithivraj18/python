string = input("enter the string to be reversed:")
rev = ""
for i in range(len(string)-1,-1,-1):
    rev = rev+string[i]
print("the reversed string is:",rev)