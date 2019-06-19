#Program will prompt for current age and year you can retire it should then display amount of years left for retirement
import datetime

#Initializing Variables
currentDt = datetime.datetime.now()
currentYear = currentDt.year
cAge = int(input("Input your current Age"))
rAge = int(input("Input at what age you will retire"))

#Creating Retirment Calculator
years_until_retirement = (rAge - cAge)
retirement_year = (currentYear + years_until_retirement)

#presenting information to user
print("You have %s years left until you can retire." % (years_until_retirement))
print(" It's %s, so you can retire in %s" % (currentYear, retirement_year))
