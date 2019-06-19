#Program will prompt for current age and year you can retire it should then display amount of years left for retirement
import datetime

currentDt = datetime.datetime.now()
currentYear = currentDt.year


#Creating Fail safe
while True:
    print("whats your current Age")
    input1 = input()
    try:
        cAge= int(input1)
        if cAge < 0:
            print("You can already Retire!")
            continue
        else:
            break
    except ValueError:
        print("you need a whole number")

while True:
    print("What age do you want to retire in")
    input2 = input()
    try:
        rAge= int(input2)
        if rAge < 0:
            print("You can already Retire!")
            continue
        else:
            break
    except ValueError:
        print("you need a whole number")

#Calculating Retirment
years_until_retirement = (rAge - cAge)
retirement_year = (currentYear + years_until_retirement)

#presenting information to user
print("You have %s years left until you can retire." % (years_until_retirement))
print("It's %s, so you can retire in %s" % (currentYear, retirement_year))
