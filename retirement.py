
from properties import *

#    Ingreso de datos manual 

print()
print("** Calculadora para el retiro **")
print()
currAge      = int(input("Edad actual             : "))
retireAge    = int(input("Edad de retiro          : "))

if retireAge < Final:
    annualExpend = int(input("Gastos anuales actuales : "))

    if annualExpend == 0:
        annualExpend = myCurrentExpend

    # Maths...
    remainYears        = (retireAge - currAge) # Años restantes hasta el retiro
    retireYears        = (Final - retireAge)   # Años que debería durar
    mainRule           = 100/retireYears

    mainRuleFactor     = round(mainRule/100,2)
    avgAnnualInfFactor = round((avgAnnualInf/100),2)
    inflationFactor    = round(((1+avgAnnualInfFactor)**remainYears),2)
    
    GrandTotal         = (annualExpend*inflationFactor/mainRuleFactor)

    print()
    print("Años hasta el retiro          : " + str(remainYears))
    print("Años de retiro                : " + str(retireYears))
    print("Porcentaje de la regla a usar : " + str(mainRule)+"%")
    print("Factor de inflación esperado  : " + str(inflationFactor))
    print()
    print("<< El gran total es: ${:,.2f}".format(GrandTotal) + " >>")
    print()

else:
    print()
    print("Edad de retiro muy lejana...")
    print()
