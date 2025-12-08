num = int(input("enter the number:"))
a = 0
b = 1
for i in range(1,num):
    print(a,end = "")
    a,b = b,a+b
