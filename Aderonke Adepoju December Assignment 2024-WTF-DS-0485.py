#!/usr/bin/env python
# coding: utf-8

# # Exercise 1

# # 1

# In[1]:


print("\ta\tb\tc")


# In[2]:


print("\\\\")


# In[3]:


print("'")


# In[4]:


print("\"\"\"")


# In[5]:


print("C:\nin\the downward spiral")


# # 2

# In[6]:


print("/ \\" + " // \\\\ " + "/// \\\\\\")


# # 3

# In[7]:


print('This quote is from Irish poet Oscar Wilde:\n"Music makes one feel so romantic\n- at least it always gets on one\'s nerves – which is the same thing nowadays."')


# # 4

# In[8]:


print('A "quoted" String is \'much\' better if you learn')
print('the rules of "escape sequences." Also, "" represents an empty String. Don\'t forget: use \\" instead of " ! \'\' is not the same as "') 


# # 5

# In[9]:


9 / 5


# In[10]:


695 % 20


# In[11]:


7 + 6 * 5


# In[12]:


7 * 6 + 5


# In[13]:


248 % 100 / 5


# In[14]:


6 * 3 - 9 / 4


# In[15]:


(5 - 7) * 4


# In[16]:


6 + (18 % (17 - 12))


# # Exercise 3

# # 1

# In[17]:


def find_max_value(input_list):
    max_value = input_list[0]
    for num in input_list:
        if num > max_value:
            max_value = num
    return max_value

# Test with the given array
input_array = [2, 4, 7, 4, 23, 5, 1, 4, 8, 9]
max_value = find_max_value(input_array)
print("The maximum value in the given array is:", max_value)


# # 2

# In[18]:


# Function to calculate average
def calculate_average(num_list):
    total = sum(num_list)
    average = total / len(num_list)
    return average

# Input list of numbers
input_list = [4, 7, 1, 5, 11, 53, 12, 46, 84, 23]

# Calculate and print average
average_value = calculate_average(input_list)
print("Average value:", average_value)


# # 3

# In[19]:


# Define the list of integers
numbers = [2, 6, 7, 45, 23, 53, 14, 45, 89, 5]

# Print the list in reverse order
print(numbers[::-1])


# # 4

# In[20]:


def compare_lists(list1, list2):
    if len(list1) != len(list2):
        return False
    return all(x < y for x, y in zip(list1, list2))

# Example usage
list1 = [2, 4, 6, 8, 10]
list2 = [12, 14, 16, 18, 20]
print(compare_lists(list1, list2))  # This will print True


# # 5

# In[21]:


def swap_elements(arr, index1, index2):
    if 0 <= index1 < len(arr) and 0 <= index2 < len(arr):
        arr[index1], arr[index2] = arr[index2], arr[index1]
    return arr


# # 6

# In[22]:


def combine_lists(list1, list2):
    combined_list = list1 + list2
    return combined_list

# Example usage
list1 = [2, 4, 6]
list2 = [7, 8, 9]
result = combine_lists(list1, list2)
print(result)


# # 7

# In[23]:


def find_last_index(input_list, value):
    last_index = -1
    for i in range(len(input_list)):
        if input_list[i] == value:
            last_index = i
    print(last_index)

# Example usage
input_list = [74, 85, 102, 99, 101, 85, 56]
value = 85
find_last_index(input_list, value)


# # 8

# In[16]:


# def find_range_of_list(input_list):
    min_val = min(input_list)
    max_val = max(input_list)
    list_range = max_val - min_val + 1
    return list_range

# Test the function with the provided example
example_list = [36, 12, 25, 19, 46, 31, 22]
result = find_range_of_list(example_list)
print(result)


# # 9

# In[ ]:


#def count_elements_within_range(numbers, min_value, max_value):
    count = 0
    for num in numbers:
        if min_value <= num <= max_value:
            count += 1
    print(f'The count of elements between {min_value} and {max_value} (inclusive) is: {count}')

#Example
nums = [14, 1, 22, 17, 36, 7, -43, 5]
min_val = 4
max_val = 17
count_elements_within_range(nums, min_val, max_val)


# # 10

# In[26]:


def is_sorted(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

list1 = [16.1, 12.3, 22.2, 14.4]
list2 = [1.5, 4.3, 7.0, 19.5, 25.1, 46.2]

print(is_sorted(list1))  # Output: False
print(is_sorted(list2))  # Output: True


# # Exercise 4

# # 1

# In[1]:


a = """+----+

\\    /

/    \\

\\    /

/    \\

\\    /

/    \\

+----+"""
for x in a:
    pass
print(a)


# # 2

# In[2]:


b ="""**********

**********

**********

**********

**********"""
for x in b:
    pass
print(b)


# # 3

# In[3]:


for x in range(1,7):
  print(x)


# In[4]:


for x in range(2,14,2):
  print(x)


# In[7]:


for x in range(4,80,15):
  print(x)


# In[8]:


for x in range(30,-30,-10):
  print(x)


# In[9]:


for x in range(-7,14,4):
  print(x)


# In[10]:


for x in range(97,81,-3):
  print(x)


# In[11]:


for x in range(-4,87,18):
  print(x)


# # 4

# In[12]:


class Constant:
    line_num = 7
for c in range(1, Constant.line_num + 1):
    for d in range(c):
        print(c, end="")
    print()


# # 5

# In[14]:


def pay(salary, work_hours):
    if work_hours <= 8:
        total_pay = salary * work_hours
    else:
        overtime_hours = work_hours - 8
        total_pay = (salary * 8) + (1.5 * salary * overtime_hours)
    return total_pay
print(pay(5.50,6))
print(pay(4.00,11))
print(pay(6.30,10))


# # 6

# In[17]:


import math 

def area_of_circle(radius):
    return math.pi * radius * radius
radius = float(input("Enter the value of the radius"))
answer = area_of_circle(radius)
print("The area is", answer)


# # 7

# In[23]:


low = 1
high = 1001
sum = 0
for i in range(low,high):
 sum += i

print("sum = " , sum)


# # 8

# In[32]:


values = []

while True:
    value = int(input("Enter your values, end at 0 when satisfied "))
    if value == 0:
        break
    values.append(value)

answer = sum(values)
print("The sum of your values is", answer)


# # 9

# In[41]:


f = []

while True:
    value = int(input("Enter your values, end at -1 when satisfied "))
    if value == -1:
        break
    f.append(value)

answer = sum(f)
print("The sum of your values is", answer)


# # 10

# In[40]:


def repl(String, number):
    return String * number
String = str(input("Enter the word"))
number = int(input("Enter the iterator"))
answer = repl(String, number)
print (answer)


# # 12

# In[33]:


def smallestLargest ():
    count = int(input("How many numbers do you want to enter? "))
    values = [int(input(f"Number {i}:")) for i in range(1, count + 1)]
    print(f"smallest = {min(values)}")
    print(f"Largest = {max(values)}")
smallestLargest()


# # 14

# In[34]:


def numUnique(a, b, c):
    if a == b or a == c or b ==c:
        print("There are 2 unique numbers")
    elif a == b == c:
        print("There is 1 unique number")
    else:
        print("There are 3 unique numbers")
        
a = int(input("Enter the first integer"))
b = int(input("Enter the second integer"))
c = int(input("Enter the third integer"))

numUnique(a, b, c)

