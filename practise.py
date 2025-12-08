string = input("enter the string:")
words = string.split()

if len(words) == 0:
    print("no words found")
else:
    longest = words[0]
    for i in words[1:]:
        if len[words] > longest:
            longest = len[words]
print("the longest word is:",longest)