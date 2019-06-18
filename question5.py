# simple calculator that will prompt for 2 number and then add subtract multiply and divide them

# Make sure user doesnt input negative input
while True:
    print("whats the first number")
    input1 = input()
    try:
        num1 = int(input1)
        if num1 < 0:
            print("You entered a negative number")
            continue
        else:
            break
    except ValueError:
        print("You entered a string")
        continue\

while True:
    print('Whats the second number')
    input2 = input()
    try:
        num2 = int(input1)
        if num2 < 0:
            print("You entered a negative number")
            continue
        else:
            break
    except ValueError:
        print("You entered a string")
        continue

#Calculate and Present data to user
print (""" %s + %s = %s
 %s - %s = %s
 %s * %s = %s
 %s / %s = %s """ % (num1, num2, num1 + num2,  num1, num2, num1 - num2, num1, num2, num1 * num2,num1, num2, num1 / num2 ))
