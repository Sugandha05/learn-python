
"""question
Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is,
it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

Solution """

num = int(input("Provide a number to divide: "))
x = list(range(1,num+1))  # num +1 ????
print(x)
divisorList = []

for elem in x:
    if num % elem == 0:
        divisorList.append(elem)
print(divisorList)




numb = int(input("Provide a number to divide: "))
x = list(range(1,numb))
divisorList = []

for elem in x:
    if numb % elem == 0:
        divisorList.append(elem)
        print(divisorList)

