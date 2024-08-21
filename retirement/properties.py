
# Propiedades de los calculos
mainRule     = 4 # % de retiro anual de acuerdo con la regla por default que se pretende usar
avgAnnualInf = 4 # % promedio de inflacion esperado
avgIntRate   = 5 # % promedio de tasa de interes ganado
Final        = 85

# Gasto anual actual
fixedCosts = 380000
myCurrentExpend = 380000 + 120000

GrandTotal = 37500000 #35000000
decimals = 2

# ************ Propiedades de la calculadora de interes compuesto **********

# Variables de inicio
T           = 14.25   # Tasa anualizada
detailFlag  = False

# Variables de incremento
incrementFlag = False
incrementDay  = 15 # cada cuantos dias hay incremento

# Calculos iniciales
t         = T/100
f         = t/360
dayCnt    = 0
counter2  = 0
