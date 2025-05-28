# Adding Of Two Numbers

#Using Regular Function
num1= int(input("Enter Number 1 \n"))
num2= int(input('Enter Number 2 \n'))

def sum_function(a, b):
    return a+ b

sum= sum_function(num1, num2)
print(f"Addition Of {num1} + {num2} = {sum}")


# Using Lambda Function
addition= lambda x, y: x+ y
number1= 200
number2= 200
print(f"Addition of {number1} + {number2} = {addition(number1, number2)}")


# Addition Of Two NUmbers Using Regular Form
a= 5
b= 5
add= a+b
print(f"Addition Of {a} + {b} = {add}")