# Verify The Gmail And Password 

# Using Regular Way
backend_gmail= "Aman Gupta147@gmail.com"
backend_password= "U04IL22S0147"

user_gmail= input("Enter Your Gmail ID : ")
user_password= input("Enter Your Password : ")

if "@gmail.com" in user_gmail :
    if backend_gmail== user_gmail :
        if backend_password== user_password :
            print("Login Successfull")
        else :
            print("Invalid Password")
    else :
        print("Invalid Gmail So We Can't Go For Password")
else :
    print("Your Gmail Must Contain @gmail.com")


# Using Function
back_gmail= "Raj Gupta74@gmail.com"
back_pswd= "U04IL22S0150"

def check_gmail_password(back_gmail, back_pswd, use_gmail, use_pswd):
    if "@gmail.com" in use_gmail :
        if back_gmail== use_gmail :
            if back_pswd== use_pswd :
                return "Login Successful"
            else : 
                return 'Invalid Password'
        else :
            return "Invalid Gmail so We Can't Go For Password"
    else :
        return "Your Gmail Must Contain @gmail.com"

use_gmail= input("Enter Your Gmail : ")
use_pswd= input("Enter Your Password : ")

result= check_gmail_password(back_gmail, back_pswd, use_gmail, use_pswd)
print(result)