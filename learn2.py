
"""
Practice Python

Exercise -1

x = input("what is your name ")
y = int(input("what is your age "))
print("You will turn 100 yrs old in:" , (100-y), "yrs")
z = int(input("Provide a number"))
print(("You will turn 100 yrs old in : " + str(100-y) + "yrs\n")*z)

Exercise 2

Ask the user for a
number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

Extras:

If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
If check divides evenly into num, tell that to the user. If not, print a different appropriate message."""

a = int(input("Provide a number"))
if a%2 = 0:
   print("Given no. is even")
else:
    print("Provided number is odd")

num = int(input("Give Num"))
check = int(input("give check"))
if num%check=0:
    print("No. is divisible")

