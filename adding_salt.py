# Adding Salt In A Given Password

#Using Regular Way
password= "veeresh"
salt= "@123"
merg= password +  "" + salt
print(merg)


# Using Function
def adding_salt(pswd, slt):
    return pswd + "" + slt

pw= input("Enter The Password : ")
sl= "@123"
after_salt= adding_salt(pw, sl)
print(f"After Adding Salt The PAssword Wil Be = {after_salt}")