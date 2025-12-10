term = int(input("enter the number of terms:"))
value = []
for i in range(0,term):
    n = int(input("enter the value:"))
    value.append(n)
new = []
for i in range(0,term):
    if value[i]%3 == 0:
        new.append(value[i])
print("the list of number divisible by 3 are:",new)