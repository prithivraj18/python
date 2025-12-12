n = int(input("enter the number of values:"))
value = []

for i in range(n):
    term = int(input("enter the term:"))
    value.append(term)
print("the terms in the list are:",value)
even = filter(lambda x:x%2 == 0,value)
square = map(lambda x:x*x,even)
print(list(square))