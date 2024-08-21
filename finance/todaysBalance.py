
from properties import *

# Nu debit + bx+ + yay + efectivo
print()
currentAmount = (200.63 + 477 + 1697.44 + 0) - 108 -150 -500 #int(input("Saldo actual     : ")) # 
currDay       = int(input("Dia actual : "))
elapsedDays   = currDay - one

shouldAmount = total-(dailyBudget*elapsedDays)
difference   = currentAmount-shouldAmount

print()
print(sStars + " Calculos al dia de hoy " + sStars)
print("Presupuesto diario : ${:,.2f}".format(dailyBudget))
print("Dias transcurridos : " + str(elapsedDays))
print()
print("Deberias tener     : ${:,.2f}".format(shouldAmount))
print("Tienes             : ${:,.2f}".format(currentAmount))
print()

# print("Actual  : $ {:,.2f}".format(GrandTotal) + sMessage2)

daysDiff = daysDuration-elapsedDays

if daysDiff > one:
    if difference > zero:
        print("Felicidades, hoy puedes gastar tus ${:,.2f}".format(dailyBudget) + " diarios mas ${:,.2f}".format(difference))        
    elif difference == zero:
        print("Vas bien, hoy solo puedes gastar tu presupuesto diario: ${:,.2f}".format(dailyBudget))
    elif difference < zero:
        currentDaily = (dailyBudget + difference)
        if currentDaily > zero:
            print("Cuidado, hoy solo tienes: ${:,.2f}".format(currentDaily))
        elif currentDaily <= zero:
            print("No gastes nada!")

elif daysDiff == one:
     print("Llegaste al final, hoy puedes gastar: ${:,.2f}".format(currentAmount))

elif daysDiff < one:
     print("Error")

print()
