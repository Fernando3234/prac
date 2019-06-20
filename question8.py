#This Program will evenly divize pizza, will prompt for # of people, pizzas, and amount of slices per pizzas

# Initializing variables and fail safe
while True:
    print("How many people are sharing the pizzas")
    input1 = input()
    try:
        nPeople = int(input1)
        if nPeople < 0:
            print("Their cant be negative people silly")
            continue
        else:
            break
    except ValueError:
        print("you need a whole number")

while True:
    print("How many pizzas are getitng shared")
    input1 = input()
    try:
        nPizzas = int(input1)
        if nPizzas < 0:
            print("Their cant be negative pizzas")
            continue
        else:
            break
    except ValueError:
        print("you need a whole number")

while True:
    print("How many slices are in one pizza")
    input1 = input()
    try:
        nSlices = int(input1)
        if nSlices < 0:
            print("Please input a Positive number")
            continue
        else:
            break
    except ValueError:
        print("you need a whole number")

#Calculations
total_slices = (nPizzas) * (nSlices)
slice_per_person = (total_slices) // (nPeople)
remaining_slices = (total_slices) % (nPeople)

#Display Data to User
print ("%s people with %s pizzas" % (nPeople, nPizzas))
print ("Each person gets %s pieces of pizza." % (slice_per_person))
print("There are %s leftover pieces." % (remaining_slices))
