num1= int(input("Enter 1st namer please: "))
num2= int(input("Enter 2st namer please: "))
num3= int(input("Enter 3st namer please: "))

if (num1 <= num2) and (num1<=num3):
    snum=num1
elif (num2 <= num1) and (num2 <= num3):
    snum=num2
else:
    snum = num3

print("The smallest number amomg", num1,",", num2, "and", num3, "is: ", snum)