nums= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def find_even(n):
    if n% 2== 0:
        return n
    
even_no= list(filter(find_even, nums))

print("Even Numbers Are =", even_no)

print("Even Numbers Are =")
for e_n in even_no:
    print(e_n)