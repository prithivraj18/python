term = int(input("enter the number of terms:"))
value = []
for i in range(1,term+1):
    element = int(input("enter the terms:"))
    value.append(element)
print(value)
reverse = []
for i in range(len(value)-1,-1,-1):
    reverse.append(value[i])
print(reverse)