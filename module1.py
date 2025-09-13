#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      priya
#
# Created:     13-09-2025
# Copyright:   (c) priya 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
print("Priyanka Learning Python again for Placements")
print("So let's start learning so that i won't stuck anywhere in PIs or Ots")
print(("basic Python Program"))
print("i will try my best to complete the whole syllabus together")

print(". * . *")
print(" * . * ")
print(". * . *")


name = input("Enter your name: ")
age = input("Enter Your age : ")
print("Hello " + name + "\n" + "your age is " + age)

num1 = float(input("Enter num1: "))
num2 = float(input("Enter second number: "))
result = num1 + num2
print(result)

color = input("any color: ")
pluralname = input("names: ")
celebirty = input("your fav celeb: ")

print("Roses are of {color}")
print("Pluralaname is {pluralname}")
print("fav celebrity is {celebirty}")

LISTS

friends = ["Neelam", "Manju", "Aastha"]
lucky_number = [4, 5, 6, 16, 4]
for i in lucky_number:
    print(i)
print(friends)
for i in friends:
    print(i)
print(friends[-1])
print(friends[1:])
print(friends[0:3])
friends.extend(lucky_number)
friends[1] = "Prachi"
print(friends)

tuples
tuples can not be changed
immutable
coordinates = (0,0)
coordinates[0] = 1
print(coordinates[0])
coordinates = [(0,0), (8,9), (2,3)]
print(coordinates)

