n = int(input("enter the number:"))
value = []
for i in range(n):
    num = int(input("enter the values:"))
    value.append(num)
print(value)
square = map(lambda x: x * x, value)
print(list(square))
