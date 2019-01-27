
# coding: utf-8

# <h><b>Assignment 1: CEBD1250</b></h>
# <br>Receipt date: January 19th, 2019
# <br>Submission date: January 26th, 2019

# # Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message.
# 

# In[73]:


number_s = input("Please enter any integer greater than 0 :")
number_s = int(number_s)
#modulo operator divides by two and returns remainder
number_s1 = number_s%2 

if (number_s1 !=0):
    result_s = "odd"
else:
    result_s = "even"

print("\nThis number is " + str(result_s))


# # Exercise number 2

# Expanding the previous exercise, let’s say I give you a list saved in a variable: 
# a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. 
# Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.

# In[33]:


a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(a[:11])


# # Create a function that takes a list of numbers. Return the largest number in the list.
# 

# In[50]:


#print("Please enter an integer greater than 0 (e.g. 1 2 3 4):")

#Ref.: https://stackoverflow.com/questions/4663306/get-a-list-of-numbers-as-input-from-the-user
number_s = [int(x) for x in input().split()]
len_s = len(number_s)

#first approach for testing
print("\nThe highest number from the number sequence")
print(max(number_s))
i=0

#second approach
for x in range (0,len_s):
    if (number_s[x] > i):
        i = number_s[x]
        
print("\nThe highest number from the number sequence " + str(i))


# # Ask the user for a string and print out whether this string is a palindrome or not.

# (A palindrome is a string that reads the same forwards and backwards.)

# In[26]:


#Verify if string is a palindrom string
sample_s1 = str(input("Please input sample string :"))

#reverse a string
#ref.: https://www.w3schools.com/python/python_howto_reverse_string.asp
sample_s2 = sample_s1[::-1]

if (sample_s2 == sample_s1):
    print ("\nThis is a palindrome string")
else:
    print ("\nThis is not a palindrome string")
    


# # Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. 

# In[34]:


#Generate fibonacci numbers
print("Please input (a positive integer number greater than 2) how many Fibonnaci numbers need to be generated :")
F_number = input()
F_number = int(F_number)

# create a list of size F_number with null values
# Ref. https://stackoverflow.com/questions/10712002/create-an-empty-list-in-python-with-certain-size
F_sequence = [0] * F_number

F_sequence[0] = 0
F_sequence[1] = 1

for x in range(2,F_number):
    F_sequence[x] = F_sequence[x-1] + F_sequence[x-2]
    
print("\nThe Fibonnaci numbers are the following")
print(F_sequence)


# # Write a program that takes a number and print its square.

# In[4]:


# Number squared

import math #import math library

print("Please input a number :")
number_s1 = input()
number_s1 = float(number_s1)

number_s2 = number_s1**2 #alternate method math.pow(number_s1,2)

print("\nThis square of " + str(number_s1) + " is " + str(number_s2))


# # Given an list of positive integers with higher than 0 the answer should contain average values.

# In[74]:


#print("Please enter an integer greater than 0 (e.g. 1 2 3 4):")

#Ref.: https://stackoverflow.com/questions/4663306/get-a-list-of-numbers-as-input-from-the-user
number_s = [int(x) for x in input().split()]

length_s = len(number_s)
sum_s = sum(number_s)
avg_s = (sum_s / length_s)
print(avg_s)


# # Return the number of vowels per string.

# In[72]:


#Number of vowels per string (to be continued)
print ("Please input sample string :")
sample_s = input()
sample_s = str(sample_s)
length_s = len(sample_s)

vowels = ['a','A','e','E','i','I','o','O','u','U']
length_v = len(vowels)

vowel_count = 0

for x in range(1,length_s+1):
    
    for y in range (0, length_v):
        
        if (sample_s[x-1:x] == vowels[y]):
            vowel_count += 1 
            

 
print("\nThere are " + str(vowel_count)+" vowels")


# # Write a program to convert degrees of Fahrenheit to Celsius.

# In[76]:


#Farenheit to celcius
temp_F = input("Please input temperature in Farenheit :")
temp_F = float(temp_F)
temp_C = ((temp_F-32)*(5/9.0))
temp_C = round(temp_C,2)
print("\n"+str(temp_C) + " degrees C are approximately equivalent "+str(temp_F)+" degrees F")

