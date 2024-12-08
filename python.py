# write a program that will tell when you are getting 100 years old
from datetime import datetime
x = datetime.now()
currentYear = x.year
name = input("Enter Name : ")
age = int(input("Enter Age : "))
result = currentYear+(100-age)
print(f"Hello {name}! You will turn 100 years old in the year {result}")
