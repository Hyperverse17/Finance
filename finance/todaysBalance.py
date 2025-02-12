
import time
import os
from Settings.properties import * #<carpetaorigen>.<nombreArchivoPy>
from Settings.functions import *

while goAhead:
    print()
    print(sStars + " Calculos del dia " + str(currDay) +" ("+ sDateMarkFmt + ") " + sStars)
    print()
    if remainingDays >= one:
        currentAmount = addition()
        if currentAmount > 0:
            os.system("cls")
            shouldAmount  = totalBudget-(dailyBudget*elapsedDays)
            difference    = currentAmount-shouldAmount
            print()
            print(loggingBypass(sStars + " Calculos del dia " + str(currDay) +" ("+ sDateMarkFmt + ") " + sStars))
            print()
            print(loggingBypass("Dias transcurridos : " + str(elapsedDays)+" de " + str(daysDuration)))
            print(loggingBypass("Saldo Inicial      : {:,.2f}".format(totalBudget)))
            print(loggingBypass("Presupuesto diario : ${:,.2f}".format(dailyBudget)))
            time.sleep(one)
            print(sDottedLine) 
            print(loggingBypass("Deberias tener     : ${:,.2f}".format(shouldAmount)))
            print(loggingBypass("Tienes             : ${:,.2f}".format(currentAmount)))
            time.sleep(2)
            print()
            if remainingDays > one:
                if difference > zero:
                    print(loggingBypass("Felicidades, hoy puedes gastar tus ${:,.2f}".format(dailyBudget) + " diarios mas ${:,.2f}".format(difference)))       
                elif difference == zero:
                    print(loggingBypass("Vas bien, hoy solo puedes gastar tu presupuesto diario: ${:,.2f}".format(dailyBudget)))
                elif difference < zero:
                    currentDaily = (dailyBudget + difference)
                    if currentDaily > zero:
                        print(loggingBypass("Cuidado, hoy solo tienes: ${:,.2f}".format(currentDaily)))
                    elif currentDaily <= zero:
                        print(loggingBypass("Mejor no gastes nada!"))
            elif remainingDays == one:
                print(loggingBypass("Llegaste al final, hoy puedes gastar: ${:,.2f}".format(currentAmount)))
                
        else:
            raise greaterThanZeroError  
    else:
        raise updateDateError
        
    goAhead = WantToRepeat(goAhead)


print()
print(sStars + " Fin del programa " + sStars)
time.sleep(2)
print()
