#This program will prompt for length and width of a room and then calculate the area in feet it will then convert the feet into meters

#Initializing variables and fail safe
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

# calculating the area and convertion
area_in_feet = lRoom * wRoom
area_in_meters = (area_in_feet) * (0.09290304)

#Display data to User
print("You entered dimensions of %s feet by %s." % (lRoom, wRoom))
print("The area is %s square feet or %s square meters." % (area_in_feet, area_in_meters))
