#This program is a selfcheckout which will calculate not only total but total after tax
taxPer = 5.5
x = False
#Initialize
while True:
    print("Please input how many items you bought ")
    input1 = input()
    try:
        num = int(input1)
        if num < 0:
            print("please input a positive number")
            continue
        else:
            break
    except ValueError:
        print("please input a whole number")


#nested while loop so it can repeat teh questions depending how many items they have
for i in range (1,int(num)+1):
    x == False

    while x == False:
        try:
            price = float(input("please enter the price of the item"))
            quant = float(input("please enter how many of that item do you have"))
            if (price > 0) and (quant > 0):
                print("Got it")
                x = True
            else:
                print("Please input a positive number")
        except ValueError:
            print("please input a whole number")

#Calculations
subTotal = (price) * (quant)
tax = subTotal * (taxPer/100)
total = subTotal + tax

#Displaying information to user
print ("""SubTotal : $%s
Tax : $%s
Total:$ %s""" % (subTotal, tax, total))
