
import time
import os
from Settings.properties import * #<carpetaorigen>.<nombreArchivoPy>

while goAhead == True:
    print()
    print(sStars + " Calculos del dia " + str(currDay) +" ["+ str(today) + "] " + sStars)
    print()
    if remainingDays >= one:
        currentAmount = float(input("Saldo actual       : ")) # Nu debit + bx+ + yay + efectivo
        shouldAmount  = totalBudget-(dailyBudget*elapsedDays)
        difference    = currentAmount-shouldAmount
        print("Dias transcurridos : " + str(elapsedDays))
        time.sleep(one)
        print()
        print("Presupuesto diario : ${:,.2f}".format(dailyBudget))
        print("Deberias tener     : ${:,.2f}".format(shouldAmount))
        print("Tienes             : ${:,.2f}".format(currentAmount))
        time.sleep(one)
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
        print("Error: Actualizar fecha de pago y fecha de proximo pago")
        goAhead = False

    print()
    os.system("pause")
    
    if goAhead == True:
        print()
        userAnswer = input("¿Deseas repetir el proceso? (s/n): ")
        if userAnswer == 's' or userAnswer == 'S':   
            os.system("cls")
        else:
            goAhead = False

print()
print("******** Fin del programa ********")
time.sleep(2)
print()
