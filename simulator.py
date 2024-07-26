
from properties import *

print()
print("** Simulador de años de retiro **")
print()

sDottedLine = "-------------------------"
sStarLine   = "********************"
retireAge   = int(input("Edad de retiro  : "))
GrandTotal  = int(input("Monto acumulado : "))
remainYears = Final - retireAge

print()

mainRule       = round((100/remainYears),2) # Porcentaje de la "regla" que se usará
mainRuleFactor = round((mainRule/100),2)

avgAnnualInfFactor = round((avgAnnualInf/100),2) # Inflación
avgIntRateFactor   = round((avgIntRate/100),2)   # Tasa promedio de crecimiento de patrimonio
oldAmount          = (GrandTotal*mainRuleFactor) # Monto de retiro del primer año

for counter in range(0,remainYears + 10): # Ciclo que se repittantas veces como años queden desde la edad de retiro hasta el final
    year       = counter + 1
    # Calculo del monto a retirar considerando la inflacion
    if year == 1:
        currAmount = oldAmount
        sMessage  = " (" + str(mainRule) + "%" + " del gran total)"
        sMessage2 = ""
    else:
        currAmount = oldAmount * (1 + avgAnnualInfFactor) # El monto a retirar equivale a lo retirado el año anterior más la inflación
        GrandTotal = GrandTotal * (1 + avgIntRateFactor) # Lo que resta del monto total mas sus intereses ganados en el año
        sMessage   = " (Anterior más " + str(avgAnnualInf) + "%" + " de inflación)"
        sMessage2  = " (Restante más " + str(avgIntRate) + "%" + " de intereses)" 
    remaining = (GrandTotal - currAmount) # Cálculo del monto total con sus interes ganados en un año menos lo que se retira este año considerando inflación
    
    print()
    print(sDottedLine + "Año " + str(year) + sDottedLine)

    if remaining >= 0:
        print("Actual  : $ {:,.2f}".format(GrandTotal) + sMessage2)
        print("Retirar : $ {:,.2f}".format(currAmount) + sMessage )
        print("Restan  : $ {:,.2f}".format(remaining)+"*")
    else:
        print("Actual  : $ {:,.2f}".format(GrandTotal) + sMessage2)
        print("Retirar : $ {:,.2f}".format(currAmount) + sMessage)
        print("Restan  : $ {:,.2f}".format(remaining) + " (insuficiente)")
        print(sStarLine + " Have a nice death " + sStarLine)
        break

    oldAmount = currAmount
    GrandTotal = remaining

print()

    