from datetime import date, datetime
############## De Flujo ##############
goAhead = True
############### Operativos ############
zero         = 0
one          = 1
totalBudget  = 3600
########## Calculo con fechas ###########
paymentDay    = date(2024,8,26)  # Fecha de pago [Tipo date]
nextPayDay    = date(2024,9,11)  # Proxima fecha de pago
today         = date.today()     # Fecha de hoy
dateTimeMark  = datetime.now() #Objeto tipo date, time
sDateMarkFmt  = dateTimeMark.strftime("%d/%m/%Y") # Funcion para dar formato a objetos tipo date y date time. Genera string YY MM DD
deltaDays1    = today-paymentDay # Diferencia entre fechas [Tipo Date]
deltaDays2    = nextPayDay-paymentDay
elapsedDays   = deltaDays1.days # el atributo .days devuelve un entero operable
daysDuration  = deltaDays2.days
remainingDays = daysDuration-elapsedDays
currDay       = elapsedDays + one
dailyBudget   = round(totalBudget/daysDuration,2)
################ Formato ######################
sStars = "**************"

####### Propiedades Calculadora Interes compuesto #######
# Variables de inicio
T          = 13.25   # Tasa anualizada
detailFlag = False

# Variables de incremento
incrementFlag = False
incrementDay  = 15 # cada cuantos dias hay incremento

# Calculos iniciales
t        = T/100
f        = t/360
dayCnt   = 0
counter2 = 0
