#This program will calculate teh amount of gallons needed to paint a room
import math

#Initialize and fail safe
while True:
    print("what is the length of the room in feet")
    input1 = input()
    try:
        lRoom= int(input1)
        if lRoom < 0:
            print("Please input a Positive number")
            continue
        else:
            break
    except ValueError:
        print("you need a whole number")

while True:
    print("what is the width of the room in feet")
    input1 = input()
    try:
        wRoom= int(input1)
        if wRoom < 0:
            print("Please input a Positive number")
            continue
        else:
            break
    except ValueError:
        print("you need a whole number")

#Calculations
area_of_room = (lRoom) * (wRoom)
pGallons = (area_of_room) / 360
math.ceil(pGallons)

#Displaying data to user
print("you will need to purchase %s gallons of paint to cover %s square feet." % (math.ceil(pGallons), area_of_room))

print(math.ceil(pGallons))
