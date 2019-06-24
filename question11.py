#This program will convert currency from euro to U.S Dollars
from functions import *

 #Initialize
euros = checkInput_float ("How many euros do you have?")
eRate = checkInput_float ("Whats the current exchange rate from Euro to Dollar?")


# Calculations
US_Dollars = round((euros * eRate) / (100), 2)

#display data to user
print("%s euros at an exchange rate of %s is %s U.S. dollars." % (euros, eRate, US_Dollars ))
