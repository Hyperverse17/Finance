try:
    import time
    import os
    from finance.core.properties import * #<carpetaorigen>.<nombreArchivoPy>
    from finance.core.functions import *
    from finance.models.classes import noSuchRecord, Budget

    scriptName = "todaysBalance.py" # os.path.basename(__file__)
    log(sStars*3,scriptName)
    log("Obteniendo inversor...",scriptName)
    investor = getInvestorById(defaultId)

    if investor is None:
        raise noSuchRecord
    else:
        name = investor.name
        log(f"Inicia sesion      : [{defaultId}] {name}",scriptName)
        paymentDay  = datetime.strptime(getParameters(defaultId,1), "%Y-%m-%d").date()
        nextPayDay  = datetime.strptime(getParameters(defaultId,2), "%Y-%m-%d").date()
        totalBudget = float(getParameters(defaultId,3))

    budget = Budget(totalBudget, paymentDay, nextPayDay)
    currDay = budget.current_day
    elapsedDays = budget.elapsed.days
    daysDuration = budget.all.days
    remainingDays = budget.remaining.days

    while goAhead:
        print()
        print(sStars + " Calculos del dia " + str(currDay) +" ("+ sDateMarkFmt + ") " + sStars)
        print(f"                         Hola, {name}!")
        print()
        if budget.remaining.days >= one:
            currentAmount, tddAmt = addition()
            budget.status(currentAmount)
            if currentAmount > 0:
                os.system("cls")
                shouldAmount     = budget.should_amount
                difference       = budget.difference
                dailyBudget      = budget.daily_budget

                to_add_substract, action, origin = to_add_substract(dailyBudget, difference, tddAmt)
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
                        print(log("Hoy puedes gastar tus ${:,.2f}".format(dailyBudget) + " diarios mas ${:,.2f}".format(difference),scriptName))
                        print(log("${:,.2f}".format(dailyBudget + difference) + " en total!" ,scriptName))
                    elif difference == zero:
                        print(log("Vas bien, hoy solo puedes gastar tu presupuesto diario: ${:,.2f}".format(dailyBudget),scriptName))
                    elif difference < zero:
                        currentDaily = (dailyBudget + difference)
                        if currentDaily > zero:
                            print(log("Cuidado, hoy solo tienes: ${:,.2f}".format(currentDaily),scriptName))
                            
                        elif currentDaily <= zero:
                            print(log("Mejor no gastes nada!",scriptName))
                            print(log("Te faltan: ${:,.2f}".format(shouldAmount-currentAmount),scriptName))
                            
                elif remainingDays == one:
                    print(log("Llegaste al final, hoy puedes gastar: ${:,.2f}".format(currentAmount),scriptName))
                
                print(log("{action} ${amount:,.2f} {origin} tu TDD".format(action=action, amount=abs(to_add_substract), origin=origin),scriptName))
                
            else:
                pass
        else:
            pass
        
        goAhead = WantToRepeat(goAhead)

except noSuchRecord as e:
    os.system("cls")
    print()
    print(log(f"{e}: {defaultId}",scriptName))

except(FileNotFoundError) as error:
    print("Parece que algo salio mal con el archivo")
    print(f"{error}")

finally:
    print()
    print(log(sStars + " Fin del programa " + sStars,scriptName))
    time.sleep(2)
    print()
