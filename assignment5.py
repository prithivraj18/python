list = [12,7,25,3,19]
term = len(list)
smallest = list[0]
largest = list[0]
for i in range(0,term):
    if smallest > list[i]:
        smallest = list[i]
print("the smallest element in the given list is:",smallest)
for i in range(0,term):
    if largest < list[i]:
        largest = list[i]
print("the largest element in the given list is:",largest)