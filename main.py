import random
import py_list
#comment - printing text
print("Hello \n" + "Manish");
#comment - printig the lenght of text entered in input
# print( len(input()))
variable_1=input("Please provide your name below:  ");
#variable name cannot start numeric e.g 1_variable is invalid
print("Hello!! " + variable_1)
print(type(variable_1))
name_len=len(variable_1)
print("Your Name has " + str(name_len) + " Characters.")

# PEMDAS Calculation Order- () *   **  /  +  -
print(8/3) # this will print a floating number
print(round(8/3))
print (8 // 3 ) # this will return integer

#f-string

print(f"Your Name has { name_len} Characters.")

if name_len < 4 :
  print("Name is short adding XXXX at the end ")
else:
  random_int=random.randint(1,1000)
  print(f"Thank you for Registering {random_int} ")
  print(f"{py_list.user}")


