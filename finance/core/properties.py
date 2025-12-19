import sys
import os
import time
import git
from datetime import date, datetime

repo = git.Repo(search_parent_directories=True)
branch = repo.active_branch

############## De Flujo ##############
goAhead  = True
addFlag  = True
saveData = False


os.system("cls")
table1     = "investors"
defaultId  = int(input("\nId de usuario: "))

############### Operativos ############
zero         = 0
one          = 1
########## Calculo con fechas ###########
today         = date.today()    # Fecha de hoy
dateTimeMark  = datetime.now()  # Objeto tipo date, time
sDateMarkFmt  = dateTimeMark.strftime("%d/%m/%Y") # Funcion para dar formato a objetos tipo date y date time. Genera string YY MM DD
amounts       = []
################ Formato ######################
sStars      = "*****************"
sDottedLine = "---------------------------------"
fmtCnt      = zero
null        = ""
####### Propiedades Calculadora Interes compuesto #######
T = 7.75   # Tasa anualizada
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
symbolicLimit = 10000 # mdgs simbólico límite

