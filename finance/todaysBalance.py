
import time
import os
from Settings.properties import * #<carpetaorigen>.<nombreArchivoPy>
from Settings.functions import *

try:
    while goAhead:
        print()
        print(sStars + "Calculos del dia " + str(currDay) +" ("+ sDateMarkFmt + ") " + sStars)
        print()
        if remainingDays >= one:
            currentAmount = addition()
            if currentAmount > 0:
                os.system("cls")
                shouldAmount  = totalBudget-(dailyBudget*elapsedDays)
                difference    = currentAmount-shouldAmount
                print()
                print(logging("Calculos del dia " + str(currDay) +" ("+ sDateMarkFmt + ")"))
                print()
                print(logging("Dias transcurridos : " + str(elapsedDays)+" de " + str(daysDuration)))
                print(logging("Saldo Inicial      : {:,.2f}".format(totalBudget)))
                print(logging("Presupuesto diario : ${:,.2f}".format(dailyBudget)))
                time.sleep(one)
                print(sDottedLine) 
                print(logging("Deberias tener     : ${:,.2f}".format(shouldAmount)))
                print(logging("Tienes             : ${:,.2f}".format(currentAmount)))
                time.sleep(2)
                print()
                if remainingDays > one:
                    if difference > zero:
                        print(logging("Felicidades, hoy puedes gastar tus ${:,.2f}".format(dailyBudget) + " diarios mas ${:,.2f}".format(difference)))       
                    elif difference == zero:
                        print(logging("Vas bien, hoy solo puedes gastar tu presupuesto diario: ${:,.2f}".format(dailyBudget)))
                    elif difference < zero:
                        currentDaily = (dailyBudget + difference)
                        if currentDaily > zero:
                            print(logging("Cuidado, hoy solo tienes: ${:,.2f}".format(currentDaily)))
                        elif currentDaily <= zero:
                            print(logging("Mejor no gastes nada!"))
                elif remainingDays == one:
                    print(logging("Llegaste al final, hoy puedes gastar: ${:,.2f}".format(currentAmount)))
                
            else:
                raise zeroValueError  
        else:
            raise dateError
        
        goAhead = WantToRepeat(goAhead)

except(greaterThanZeroError):
    print(logging(zeroValueError.message))

except(updateDateError):
    print(logging(dateError.message))

finally:
    print()
    print(logging(sStars + " Fin del programa " + sStars))
    time.sleep(2)
    print()
