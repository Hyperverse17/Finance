try:
    import time
    import os
    from Settings.properties import * #<carpetaorigen>.<nombreArchivoPy>
    from Settings.functions import *
    scriptName = os.path.basename(__file__)

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
                print(log("Calculos del dia " + str(currDay) +" ("+ sDateMarkFmt + ")",scriptName))
                print()
                print(log("Dias transcurridos : " + str(elapsedDays)+" de " + str(daysDuration),scriptName))
                print(log("Saldo Inicial      : {:,.2f}".format(totalBudget),scriptName))
                print(log("Presupuesto diario : ${:,.2f}".format(dailyBudget),scriptName))
                time.sleep(one)
                print(sDottedLine) 
                print(log("Deberias tener     : ${:,.2f}".format(shouldAmount),scriptName))
                print(log("Tienes             : ${:,.2f}".format(currentAmount),scriptName))
                time.sleep(2)
                print()
                if remainingDays > one:
                    if difference > zero:
                        print(log("Felicidades, hoy puedes gastar tus ${:,.2f}".format(dailyBudget) + " diarios mas ${:,.2f}".format(difference),scriptName))       
                    elif difference == zero:
                        print(log("Vas bien, hoy solo puedes gastar tu presupuesto diario: ${:,.2f}".format(dailyBudget),scriptName))
                    elif difference < zero:
                        currentDaily = (dailyBudget + difference)
                        if currentDaily > zero:
                            print(log("Cuidado, hoy solo tienes: ${:,.2f}".format(currentDaily),scriptName))
                        elif currentDaily <= zero:
                            print(log("Mejor no gastes nada!",scriptName))
                elif remainingDays == one:
                    print(log("Llegaste al final, hoy puedes gastar: ${:,.2f}".format(currentAmount),scriptName))
                
            else:
                raise zeroValueError  
        else:
            raise dateError
        
        goAhead = WantToRepeat(goAhead)

except(greaterThanZeroError):
    print(log(zeroValueError.message,scriptName))

except(updateDateError):
    print(log(dateError.message,scriptName))

except(FileNotFoundError) as error:
    print("Parece que algo salio mal con el archivo")
    print(f"{error}")

finally:
    print()
    print(log(sStars + " Fin del programa " + sStars,scriptName))
    time.sleep(2)
    print()
