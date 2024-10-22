import os
from datetime import date, datetime
############## De Flujo ##############
goAhead = True
addFlag = True
############### Operativos ############
zero         = 0
one          = 1
totalBudget  = 4000
########## Calculo con fechas ###########
paymentDay    = date(2024,10,11) # Fecha de pago [Tipo date]
nextPayDay    = date(2024,10,25) # Proxima fecha de pago
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
amounts       = []
################ Formato ######################
sStars      = "**************"
sDottedLine = "---------------------------------"
fmtCnt      = zero
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

# Calculos iniciales
t        = T/100
f        = t/360
dayCnt   = 0
counter2 = 0

def WantToRepeat(goAhead):
    print()
    os.system("pause")
    os.system("cls")
    if goAhead == True:
        userAnswer = input("Deseas repetir el proceso? (s/n) 🤔:")
        if userAnswer == 's' or userAnswer == 'S':
            os.system("cls")
        else:
            goAhead = False
    return goAhead

def addition():
    addFlag = True
    fmtCnt  = zero
    totalSum = zero
    while addFlag:
        fmtCnt += 1
        currAmt = input("Ingresa monto " + str(fmtCnt) + ": ") # Nu debit + bx+ + yay + efectivo
        if currAmt == "":
            currAmt = 0
            addFlag = False
        totalSum += float(currAmt)
    return totalSum
    