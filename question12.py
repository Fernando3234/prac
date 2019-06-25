#This program will calculate interest
from functions import *

#initialize
pAmount = checkInput("Whats the Initial Amount?")
iRate = checkInput_float ("Whats the interest rate in percentage?")
tYears = checkInput ("For how many years?")

 #calculations
taInvestment = pAmount * (1 + (iRate/100)* tYears)

#display information to user
print ("After %s years at %s%%, the investment will be worth $%s" % (tYears, iRate, taInvestment))
