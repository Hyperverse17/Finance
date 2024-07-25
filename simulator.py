
from properties import *

print()
print("** Calculadora para el retiro **")
print()
remainYears = int(input("Años : "))
print("Monto Inicial: ${:,.2f}".format(GrandTotal))
print()

mainRuleFactor     = mainRule/100
avgAnnualInfFactor = avgAnnualInf/100
avgIntRateFactor   = (avgIntRate/100)
oldAmount          = (GrandTotal*mainRuleFactor)

for counter in range(0,remainYears):
    year       = counter + 1

    # Calculo del monto a retirar considerando la inflacion
    if year == 1:
        currAmount = oldAmount
        
    else:
        currAmount = oldAmount * (1 + avgAnnualInfFactor)
        GrandTotal = GrandTotal * (1 + avgIntRateFactor)

    remaining = (GrandTotal - currAmount)
    
    print()
    print("----- Año " + str(year)+" -----")

    if remaining >= 0:
        print("Actual  : ${:,.2f}".format(GrandTotal))
        print("Retirar : ${:,.2f}".format(currAmount))
        print("Restan  : ${:,.2f}".format(remaining))
    else:
        print("Actual  : ${:,.2f}".format(GrandTotal))
        print("Retirar : ${:,.2f}".format(currAmount))
        print("Restan  : ${:,.2f}".format(remaining))
        print("*** Have a nice death ***")
        break

    oldAmount = currAmount
    GrandTotal = remaining

print()
#   print("(1+"+str(avgAnnualInfFactor)+")**"+str(counter))

#    
    
 #   

    

    





