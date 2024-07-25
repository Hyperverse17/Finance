
from properties import *

#    Ingreso de datos manual 

print()
print("** Calculadora para el retiro **")
print()
currAge      = int(input("Edad actual             : "))
retireAge    = int(input("Edad de retiro          : "))
annualExpend = int(input("Gastos anuales actuales : "))

if annualExpend == 0:
    annualExpend = myCurrentExpend

# Maths...
mainRuleFactor     = mainRule/100
avgAnnualInfFactor = avgAnnualInf/100
remainYears        = (retireAge - currAge)
inflationFactor    = ((1+avgAnnualInfFactor)**remainYears)
GrandTotal         = (annualExpend*inflationFactor/mainRuleFactor)

print()
print("El gran total es: ${:,.2f}".format(GrandTotal))
print()
