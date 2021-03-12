# But in Python 3 we have only input() method and raw_input() method is not available.
# Python3 input() function behaviour exactly same as raw_input() method of Python2.
# i.e every input value is treated as str type only.
# raw_input() function of Python 2 is renamed as input() function in Python 3.

# Contorl Flow:
# 1.Conditional Statements
# 2.Transfer Statements
# 3.Iterative Statements

#Conditional Statements
# 1. if
# 2. if-elif
# 3. if-elif-else

# 1) if : If condition is true then statements will be executed.
# if condition : statement
# OR
# if condition :
#     statement-1
#     statement-2
#     statement-3

name=input("Enter your name :")
if name=="Ali":
    print("Yes")

# if-else: if condition is true then Action-1 will be executed otherwise Action-2 will be executed.
# if condition:
#     Action-1
# else:
#     Action-2

numb=input("Enter your lucky number:")
if numb=='7':
    print("Congrats yu won")
else:
    print("Sorry.Please try again")
