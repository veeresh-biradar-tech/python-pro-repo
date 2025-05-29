# Seprate Even And Odd Numbers From The List

# Using Regular Way
nums= [1, 2, 3, 4, 5]
even_num= list()
odd_num= list()

for i in range(0, len(nums)):
    if nums[i]% 2== 0:
        even_num.append(nums[i])
    else:
        odd_num.append(nums[i])
    
print(f"Even Numbers= {even_num} And Odd Numbers= {odd_num}")


# Using Functions
even_arr= list()
odd_arr= list()

def seprate_even_odd(numbers):
    for n in numbers:
        if n% 2== 0: 
            even_arr.append(n)
        else:
            odd_arr.append(n)

    print(f"Even Numbers= {even_arr}")
    print(f"Odd Array= {odd_arr}")

seprate_even_odd([1, 2, 3, 4, 5,])
seprate_even_odd([6, 7, 8, 9, 10])