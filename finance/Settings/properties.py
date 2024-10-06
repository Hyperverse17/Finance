import os
from datetime import date, datetime
############## De Flujo ##############
goAhead = True
############### Operativos ############
zero         = 0
one          = 1
totalBudget  = 4000
########## Calculo con fechas ###########
<<<<<<< HEAD
paymentDay    = date(2024,9,12) # Fecha de pago [Tipo date]
nextPayDay    = date(2024,9,26) # Proxima fecha de pago
=======
paymentDay    = date(2024,9,26) # Fecha de pago [Tipo date]
nextPayDay    = date(2024,10,11) # Proxima fecha de pago
>>>>>>> upg
today         = date.today()    # Fecha de hoy
dateTimeMark  = datetime.now()  # Objeto tipo date, time
sDateMarkFmt  = dateTimeMark.strftime("%d/%m/%Y") # Funcion para dar formato a objetos tipo date y date time. Genera string YY MM DD
deltaDays1    = today-paymentDay # Diferencia entre fechas [Tipo Date]
deltaDays2    = nextPayDay-paymentDay
elapsedDays   = deltaDays1.days # el atributo .days devuelve un entero operable
daysDuration  = deltaDays2.days
remainingDays = daysDuration-elapsedDays
currDay       = elapsedDays + one
dailyBudget   = round(totalBudget/daysDuration,2)
################ Formato ######################
sStars      = "**************"
sDottedLine = "---------------------------------"
####### Propiedades Calculadora Interes compuesto #######
T = 13.25   # Tasa anualizada
incrementDay = 15 # cada cuantos dias hay incremento
t = T/100
f = t/360

#################### Funciones Auxiliares #################
def clearVars():
    initValues = []
    detailFlag    = False
    incrementFlag = False
#   Calculos iniciales
    dayCnt   = 0
    counter2 = 0
    # Arrreglo para retornar los valores
    initValues.append(detailFlag)    # detailFlag posicion 0
    initValues.append(incrementFlag) # posicion 1
    initValues.append(dayCnt)        # posicion 2
    initValues.append(counter2)      # posicion 3
    
    return initValues

<<<<<<< HEAD
=======
# Calculos iniciales
t        = T/100
f        = t/360
dayCnt   = 0
counter2 = 0

>>>>>>> upg
def WantToRepeat(goAhead):
    print()
    os.system("pause")
    os.system("cls")
    if goAhead == True:
<<<<<<< HEAD
        userAnswer = input("Deseas repetir el proceso? (s/n): ")
=======
        userAnswer = input("Deseas repetir el proceso? (s/n) 🤔:")
>>>>>>> upg
        if userAnswer == 's' or userAnswer == 'S':
            os.system("cls")
        else:
            goAhead = False
    return goAhead
