# Converting Lower Case Strings To Upper CAse

# Using Regular Way
strings= ["aman", "raj", "ravi", "sham", "suraj"]

n= int(input("How Many You Want To Enter : "))
strings= list()

print("Enter The Name Which You Want To Convert Into Upper Case : ")
for i in range(0, n) :
    strings.append(input())

upper_case= list()

for str in strings :
    upper_case.append(str.upper())

# Printing In List Format
print(f"Upper CAse Strings Are= {upper_case}")

# Printing In Loop Format
for name in upper_case :
     print(name)


# Using Fumctions
upper_case= list()
def convert_to_upper(strings) :
    for str in strings :
        upper_case.append(str.upper())
    return upper_case


strings= list()

n= int(input("How Many Names You Want To Enter : "))
print("Enter The Names Which You Want To Convert Into Upper CAse : ")
for i in range(0, n) :
    strings.append(input())

print(f"Upper CAse Names Are= {convert_to_upper(strings)}")



# Using Map
def convert_into_upper(name) :
    return name.upper()

names= ["sampath", "sundar", "anjali", "shrusti", "deepa"]
upper_case= list(map(convert_into_upper, names))
print(f"Upper Case Names Are= {upper_case}")


# Using Lambda
names= ["anjali", "bhuvan", "chanda", "deepak", "eshwar"]
upper_case= list(map(lambda name: name.upper(), names))
print(f"Upper Case Names Are= {upper_case}")