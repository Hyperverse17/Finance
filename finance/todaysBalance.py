
import time
import os
from Settings.properties import * #<carpetaorigen>.<nombreArchivoPy>

try:
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
                print(sStars + " Calculos del dia " + str(currDay) +" ("+ sDateMarkFmt + ") " + sStars)
                print()
                print("Dias transcurridos : " + str(elapsedDays)+" de " + str(daysDuration))
                print("Saldo Inicial      : {:,.2f}".format(totalBudget))
                print("Presupuesto diario : ${:,.2f}".format(dailyBudget))
                time.sleep(one)
                print(sDottedLine) 
                print("Deberias tener     : ${:,.2f}".format(shouldAmount))
                print("Tienes             : ${:,.2f}".format(currentAmount))
                time.sleep(2)
                print()
                if remainingDays > one:
                    if difference > zero:
                        print("Felicidades, hoy puedes gastar tus ${:,.2f}".format(dailyBudget) + " diarios mas ${:,.2f}".format(difference))        
                    elif difference == zero:
                        print("Vas bien, hoy solo puedes gastar tu presupuesto diario: ${:,.2f}".format(dailyBudget))
                    elif difference < zero:
                        currentDaily = (dailyBudget + difference)
                        if currentDaily > zero:
                            print("Cuidado, hoy solo tienes: ${:,.2f}".format(currentDaily))
                        elif currentDaily <= zero:
                            print("Mejor no gastes nada!")
                elif remainingDays == one:
                    print("Llegaste al final, hoy puedes gastar: ${:,.2f}".format(currentAmount))
            else:
                raise ZeroDivisionError  
        else:
            raise SystemError
        
        goAhead = WantToRepeat(goAhead)

except(ZeroDivisionError):
    os.system("cls")
    print("Error: Ingresa un valor mayor que cero")

except(SystemError):
    os.system("cls")
    print("Error: Actualizar fecha de pago y fecha de proximo pago")

finally:
    print()
    print(sStars + " Fin del programa " + sStars)
    time.sleep(2)
    print()
