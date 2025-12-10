string = input("enter the string to be stored:")
count = 0
v_element = []
vowels = "aeiouAEIOU"
for i in range(len(string)):
    if string[i] in vowels:
        v_element.append(string[i])
        count = count+1
print("the number of vowels in the string is ",count)
print("the letter are:",v_element)