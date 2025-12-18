try:
    import time
    import os
    from finance.core.properties import * #<carpetaorigen>.<nombreArchivoPy>
    from finance.core.functions import *
    from finance.models.classes import noSuchRecord, dateError, updateDateError, greaterThanZeroError, zeroValueError

    scriptName = os.path.basename(__file__)

    if recordExistance(table1, defaultId) == True:
        investor   = getInvestorById(defaultId)
        name       = investor.name
        log(f"Inicia sesion        : [{defaultId}] {name}",scriptName)
        paymentDay  = datetime.strptime(getParameters(defaultId,1), "%Y-%m-%d").date()
        nextPayDay  = datetime.strptime(getParameters(defaultId,2), "%Y-%m-%d").date()
        totalBudget = float(getParameters(defaultId,3))
    else:
        raise noSuchRecord()

    deltaDays1 = today-paymentDay # Diferencia entre fechas [Tipo Date]
    deltaDays2 = nextPayDay-paymentDay

    elapsedDays   = deltaDays1.days # el atributo .days devuelve un entero operable
    daysDuration  = deltaDays2.days

    remainingDays = daysDuration-elapsedDays
    currDay       = elapsedDays + one

    dailyBudget = round(totalBudget/daysDuration,2)

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

except noSuchRecord as e:
    os.system("cls")
    print()
    print(log(f"{e} {defaultId} en {table1}",scriptName))

except(greaterThanZeroError):
    print(log(zeroValueError.message,scriptName))

except(updateDateError):
    print(log(dateError.message,scriptName))
    print(updateDates())

except(FileNotFoundError) as error:
    print("Parece que algo salio mal con el archivo")
    print(f"{error}")

finally:
    print()
    print(log(sStars + " Fin del programa " + sStars,scriptName))
    time.sleep(2)
    print()
