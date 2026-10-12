# Function add two numbers
def add_numbers(a,b):
    return a+b  

#Function sub two numbers
def sub_numbers(a,b):
    return a-b

##Function mul two numbers
def mul_numbers(a,b):
    return a*b

#Function div two numbers
def div_numbers(a,b):
    return a/b
#Function to find avg
def avg_numbers(a,b):
    return(a+b)/2

# Step-2: User input 

print("Please select a operation:\n "\
    "1.addition\n "\
    "2.subtraction\n "\
    "3.multiplication\n "\
    "4.division\n "\
    "5.average\n ")

select =int(input("Select operation from 1,2,3,4,5:"))

number1 = int (input("Enter first number:"))
number2 = int (input("Enter second nimber:"))

#step-3 print the result
if select ==1:
    print("Sum of two number is:",add_numbers(number1,number2))

elif select ==2:
    print("Sub of two number is:",sub_numbers(number1,number2))

elif select ==3:
    print("mul of two number is:",mul_numbers(number1,number2))

elif select ==4:
    print("div of two number is:",div_numbers(number1,number2))
          
if select ==5:
    print("avg of two number is:",avg_numbers(number1,number2))

else:
    print("invalid operation! pls select again!")