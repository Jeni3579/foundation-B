#1 Ask a two integer number with user and a function should return their addition 

# num=int(input("Please provide first number"))
# num_2=int(input("Please provide second number"))

# print(type(num))

# print("The sum of two number is: {int(num)+int(num_2)}")

#creation of addition function
# def addition(num,num2):
    # return sum

#calling addition fuctionn
# print(f"the sum return by the function is: (addition(num,num_2)) ")    

#Ask an information of your laptop and a function should return like this:

# """Brand_Name Model_Name available_at Price 
# Ex: Dell Vostro @ Rs. 80000

# brand_name=input("Please provide your brand name ")
# model_name=input("Please provide your model name ")
# price=input("Please provide your price  ")

# def laptop_info(brand,model,price):
    # return f"{brand} {model} @ Rs. {price}"

# print(laptop_info(brand_name,model_name,price))


#loops in python
#range function in python
print(f"the range from 1 to 10 is: {range(1,10+1)}")

#list object 
num_list =[]

week_days_list=[
"Sunday",
"Monday",
"Tuesday",
"Wednesday",
"Thursday",
"Friday",
"Saturday"]

for num in range(1,11):
    print("The number in range is: --> {num}")
    num_list.append(num)

print(num_list)    

counter = 0
for day in week_days_list:
    counter += 1
    print(f"The {counter} day is: -->{day}")

#same program with the help of range function
for position in range(0, len(week_days_list)):
    print(f"The {position} position in day is: -->{week_days_list[position]}")    


#enumerate function 
# for position,day in enumerate(week_days_list): 
    # print(f"The {position+1} ####### day is: -->{day} ")

#
odd_list = []
even_list = []
def filter_odd_even(user_provided_num):
    for num in range(1,user_provided_num+1):
        if num % 2 == 0:   
            even_list.append(num)
        else: 
            odd_list.append(num)


any_num = int(input("Please provide anu number:-->:"))
filter_odd_even(any_num)

print(f"Now, the odd list is: {odd_list}")
print(f"Now, the even list is: {even_list}") 





