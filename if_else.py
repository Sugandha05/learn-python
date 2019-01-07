marks = 80
grades = int(input("Please enter marks : "))
if (grades >= 80):
    print("Grade A")

elif (grades >= 60) and (grades <= 79):
     print ("Grade B")

elif (grades >= 40) and (grades <= 59):
     print("Grade C")

else:
    print("Grade D")