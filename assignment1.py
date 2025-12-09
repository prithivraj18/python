x = int(input("enter the number of elements:"))
element = []
for i in range(1,x+1):
    value = int(input("enter the element:"))
    element.append(i)
print(element)
even = []
for i in range(0,x):
    if element[i]%2==0:
        even.append(i)
print(even)