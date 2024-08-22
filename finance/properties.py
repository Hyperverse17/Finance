from datetime import date
zero         = 0
one          = 1
#######################################
total        = 4000
daysDuration = 14
dailyBudget  = 250 #round(total/daysDuration,2)
########## Calculo de fechas ###########
paymentDay  = date(2024,8,12)  # Tipo date
today       = date.today()     # Tipo date
deltaDays   = today-paymentDay # Tipo date
elapsedDays = deltaDays.days # el atributo .days devuelve un entero
######################################
sStars = "**************"

