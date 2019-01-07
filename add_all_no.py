
num = int(input("Provide a number: "))
sum = 0

if num < 0:
     print("Provide a valid number: ")

else:
    while(num > 0):
       sum+= num
       num = num - 1
print(sum)



