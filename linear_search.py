# Linear Search

# Function
def linear_search(nums, target_element) :
    for i in range(0, len(nums)) :
        if nums[i]== target_element :
            return i
    return -1

number= [1, 2, 3, 4, 5]
t_element= 1

result= linear_search(number, t_element)

if result>= 0 :
    print(f"Target Element {t_element} is Found At The Index {result}")
else :
    print(f"Target Element {t_element} Is Not In The Array")
