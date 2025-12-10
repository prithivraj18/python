string = input("enter the string:")
term = len(string)
for i in range(0,term):
    count = 0
    for j in range(0,term):
        if string[i] == string[j]:
            count = count+1
    print(string[i], "=" , count)