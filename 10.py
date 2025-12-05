height = float(input("enter the height of the student"))
weight = float(input("enter the weight of the student"))
bmi = weight/(height*height)
print("the bmi of the student is",bmi)
if bmi > 25:
    print("the individual is too obese")
elif bmi < 15:
    print("the individual is too light weight")
elif bmi >15 and bmi< 25:
    print("the ndividual is in correct shape")