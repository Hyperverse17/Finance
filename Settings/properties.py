from datetime import date, datetime
import git

repo = git.Repo(search_parent_directories=True)
branch = repo.active_branch

print(branch.name)
print(type(branch.name))

############## De Flujo ##############
goAhead  = True
addFlag  = True
saveData = False

if branch.name == "main":
    mainDbName = "MyFinances.db"
else:
    mainDbName = "Dummy.db"

table1     = "investors"
print()
defaultId  = int(input("Id de usuario: "))

############### Operativos ############
zero         = 0
one          = 1
totalBudget  = 3500
########## Calculo con fechas ###########
paymentDay    = date(2025,9,12) # Fecha de pago [Tipo date]
nextPayDay    = date(2025,9,26) # Proxima fecha de pago
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
sStars      = "*****************"
sDottedLine = "---------------------------------"
fmtCnt      = zero
null        = ""
####### Propiedades Calculadora Interes compuesto #######
T = 9   # Tasa anualizada
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
t             = T/100
f             = t/360
dayCnt        = 0
counter2      = 0
#monthly       = 34600 # Gastos Mensuales a julio 2025

############ Invest Rule #########
#investRule    = 110 # Aggresive!
#myBirthDay    = "1991-07-17"
symbolicLimit = 10000 # mdgs simbólico límite

########### Errors ##############
class updateDateError(Exception):
    def __init__(self) -> None:
        self.message = "Actualizar fecha de pago y fecha de proximo pago"
        super().__init__(self.message)

class greaterThanZeroError(Exception):
    def __init__(self) -> None:
        self.message = "El monto total debe ser mayor que cero"
        super().__init__(self.message)

class noSuchRecord(Exception):
    def __init__(self) -> None:
        self.message = "No existe el id"
        super().__init__(self.message)

dateError = updateDateError()
zeroValueError = greaterThanZeroError()

    