# Check/ verify That The Entered Password Is Correct Or Incorrect


# Using Regular Way
password= input("Enter The Password : ")
backend_password= "RAM@123"

if backend_password== password:
    print("Entered Password Is Correct")

else:
    print("Entered Incorrect Password")


# Using Function
def check_for_password(psd, b_psd):
    if psd== b_psd:
        return 1
    else:
        return 0

pswd= input("Enter The Passwod : ")
back_pswd= "RAJENDRA@123"

final= check_for_password(pswd, back_pswd)

if final== 1:
    print("Entered password Is Correct")
else:
    print("Incorrect Password")


# Using Different Return Value
def check_for_password(psd, b_psd):
    if psd== b_psd:
        return "Entered Password Is Correct"
    else:
        return "Incorrect Password"

pswd= input("Enter The Passwod : ")
back_pswd= "RAJENDRA@123"

final= check_for_password(pswd, back_pswd)
print(final)


# USing Different Return Value 
def check_for_password(psd, b_psd):
    if psd== b_psd:
        return 1
    else:
        return 0
    
pswd= input("Enter The Password : ")
back_pswd= "VIRAt@123"

if (check_for_password(pswd, back_pswd)):
    print("Entered Correct Password")
else:
    print("Incorrect Password")