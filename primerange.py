num = int(input("enter the number:"))
limit = int(input("enter the limit: "))
count = 0
for i in range(1,limit+1):
    if num % i == 0:
        count = count+1
if count == 2 :
    print("the given number is an prime number")
else:
    print("the given number is not an prime number")
          
          

    