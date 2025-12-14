import os
import functools
import calendar
import csv


from finance.core.properties import *
from typing import Union
from datetime import datetime, date
from finance.core.db import get_connection

conn   = get_connection()
cursor = conn.cursor()

def getParameters(userId:int, value:int) -> Union[int,float,str]:
    """Función que devuelve datos de la tabla de parámetros"""
    
    field  = ""
    
    if value == 1: # Fecha de pago 
        field = "payment_day"

    elif value == 2: # Fecha de siguiente pago
        field = "next_payment_day"
        
    elif value == 3: # Gastos del periodo
        field = "free_spending"

    else:
        pass

    command = f"SELECT {field} FROM parameters WHERE user_id = ? ORDER BY id DESC LIMIT 1;"
    cursor.execute(command, (userId,))
    row = cursor.fetchone()

    if row:
        value = row[0]
    else:
        command = f"SELECT {field} FROM parameters ORDER BY id DESC LIMIT 1;"
        cursor.execute(command)
        value = cursor.fetchone()[0]

    conn.close

    return value

def getFilePointer(scriptName):
    logPathBase = "./logs/"
    ext         = ".txt"
    

    paymentDay  = datetime.strptime(getParameters(defaultId,1), "%Y-%m-%d").date()
    nextPayDay  = datetime.strptime(getParameters(defaultId,2), "%Y-%m-%d").date()

    monthA    = paymentDay.month
    monthB    = nextPayDay.month
    monthName = calendar.month_name[monthA][:3]

    if monthA == monthB:
        payment = "1"
    else:
        payment = "2"

    if scriptName == "todaysBalance.py":
        logPath  = logPathBase + "balance/"
        fileName = "balance_log_" + monthName + "_" + str(paymentDay.year) + "_" + payment + ext
        
    elif scriptName == "toInvest.py":
        logPath  = logPathBase + "invest/"
        fileName = "invest_log_" + str(today.year) + "_" + ext

    elif scriptName == "function":
        logPath  = logPathBase + "functions/"
        fileName = "function_log_" + str(today.year) + "_" + ext
    
    os.makedirs(logPath, exist_ok=True)
    filePointer = logPath + fileName
    
    return filePointer


def writeLog(func):
    @functools.wraps(func) 
    def wrapper(*args, **kwargs):
        workingDate      = today.strftime("%y-%m-%d ")
        dateTimeMark     = datetime.now().strftime("%H:%M:%S") #Objeto tipo date time (genera una marca de tiempo)
        sDateTimeMarkFmt = workingDate + dateTimeMark # formato a la marca de tiempo, genera string YYMMDDhhmmss
        result           = func(*args, **kwargs)
        message          = "[LOG " + sDateTimeMarkFmt + f"] {result}"
        filePointer = getFilePointer(args[1]) # Se pasa el segundo arg (posicion 1)
        with open(filePointer, "a") as file:
            file.write(message + "\n")
        return result
    return wrapper

def functionLog(func):
    @functools.wraps(func) 
    def wrapper(*args, **kwargs):
        workingDate      = today.strftime("%y-%m-%d ")
        dateTimeMark     = datetime.now().strftime("%H:%M:%S") #Objeto tipo date time (genera una marca de tiempo)
        sDateTimeMarkFmt = workingDate + dateTimeMark # formato a la marca de tiempo, genera string YYMMDDhhmmss
        result           = func(*args, **kwargs)

        funcName  = func.__name__
        argsStr   = ", ".join(repr(arg) for arg in args)
        kwargsStr = ", ".join(f"{k}={v!r}" for k, v in kwargs.items())
        allArgs   = ", ".join(filter(None, [argsStr, kwargsStr]))
        message   = f"[LOG {sDateTimeMarkFmt}] Function: {funcName}({allArgs}) -> {result}"

        filePointer = getFilePointer("function") 
        with open(filePointer, "a") as file:
            file.write(message + "\n")
        return result
    return wrapper

@writeLog
def log(inMessage:str, scriptName:str)-> str:
    """Funcion auxiliar que guarda en un log el string que se le pasa"""
    outMessage = inMessage
    return outMessage

@functionLog
def WantToRepeat(goAhead:bool) -> bool:
    """Funcion auxiliar para repetir un proceso"""
    print()
    os.system("pause")
    os.system("cls")
    if goAhead == True:
        userAnswer = input("Deseas repetir el proceso? (s/n) 🤔 : ")
        if userAnswer == 's' or userAnswer == 'S':
            os.system("cls")
        else:
            goAhead = False

    return goAhead

@functionLog
def wannaSave(goAhead:bool) -> bool:
    """Solicita confirmacion"""
    print()
    if goAhead == False:
        userAnswer = input("Deseas guardar esta info en la base de datos? (s/n): ")
        if userAnswer == 's' or userAnswer == 'S':
            goAhead = True

    return goAhead

@functionLog
def addition() -> Union[int, float]:
    """Funcion auxiliar para realizar una suma de n valores"""
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

@functionLog
def recordExistance(table:str, recId:int) -> bool:
    """Evalua la existencia de determinado registro en determinada tabla"""
    command = f"SELECT 1 FROM {table} WHERE id = {recId};"
    cursor.execute(command)
    value = cursor.fetchone() # Puede regresar una tupla o nada

    if value:
        value = True
    else:
        value = False

    return value

@functionLog
def getInvestorData(investorId:int, value:int) -> Union[int,float,str]:
    """Función que devuelve datos del inversor"""
    field  = ""
    
    if value == 1: # Birthday 
        field = "birthday"

    elif value == 2: # Investment Rule
        field = "investment_rule"
        
    elif value == 3: # Monthly Expenses
        field = "monthly_expenses"

    elif value == 4: # Name
        field = "name"

    else:
        pass

    command = F"SELECT {field} FROM investors WHERE id = {investorId};"
    cursor.execute(command)
    value = cursor.fetchone()[0] # Se coloca para especificar la posición porque originalmente regresa una tupla
    conn.close

    return value

@functionLog
def getAge(birthDay:str) -> int:
    """Recibe un string con una fecha de nacimiento YYYY-MM-DD y devuelve un entero con la edad en años"""
    today     = datetime.today() 
    birthDate = datetime.strptime(birthDay, "%Y-%m-%d")
    age = int(today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))) # Se hace un comparativo entre mes y día (del día) y de mes y dia del cumpleaños, si el resultado es true, al evaluarse se considera como 1, si es false, 0
    return age

@functionLog
def toInvest():
    myAge = getAge(getInvestorData(defaultId,1)) # Segundo parametro = 1 para extraer la fecha de cumpleaños
    toInvestPerc = (getInvestorData(defaultId,2))-myAge # Segundo parametro = 2 para extraer la regla de inversión
    return toInvestPerc

@functionLog
def getMdgs():
    monthly = getInvestorData(defaultId,3)
    months = (1, 3, 6, 12, 24, symbolicLimit)
    mdgs   = [x * monthly for x in months]
    return mdgs

@functionLog
def splitter(total,mode):
    """Regresa el porcentaje que debe ser destinado al fondo de emergencias"""
    emePerces = (100,75,50,25,15,10)
    mdgs      = getMdgs()
    
    if total >= mdgs[0]:
        if (total >= mdgs[0] and total < mdgs[1]): # [1,3) MDG
            position = 1

        elif (total >= mdgs[1] and total < mdgs[2]): # [3,6) MDG
            position = 2

        elif (total >= mdgs[2] and total < mdgs[3]): # [6,12) MDG
            position = 3

        elif (total >= mdgs[3] and total < mdgs[4]): # [12, 24) MDG
            position = 4

        elif total >= mdgs[4]: # [24, inf) MDG
            position = 5

        else: # cero meses de tus gastos
            position = 0
            
        if mode == True: # Just Investments
            emerPerc = 0 
        else:
            emerPerc  = emePerces[position]
            
        nextLevel = int(mdgs[position])

    return emerPerc, nextLevel

@functionLog
def investAdjust(currVariable:float, currFixed:float, toAdd:float):
    """Funcion que determina cuando destinar a Renta Variable y Renta Fija"""
    variablePer = toInvest()
    fixedPer    = 100-variablePer

    investTotal  = currVariable + currFixed
    shldVariable = investTotal*(variablePer/100)
    shldFixed    = investTotal*(fixedPer/100)
        
    variableDiff = shldVariable-currVariable
    fixedDiff    = shldFixed-currFixed
            
    toAddVariable = toAdd*(variablePer/100)
    toAddFixed    = toAdd*(fixedPer/100)

    toInvestVar   = toAddVariable + variableDiff
    toInvestFixed = toAddFixed + fixedDiff

    if toInvestVar <= 0 and toInvestFixed > 0:
            print(f"Atencion en Renta Fija")
            if toAdd <= shldFixed:
                toInvestFixed = toAdd
                toInvestVar   = 0

            elif toAdd > shldFixed:
                toInvestFixed = shldFixed
                toInvestVar   = toAdd - shldFixed

    elif toInvestVar > 0 and toInvestFixed <= 0:
        print("Atencion en Renta Variable")
        if toAdd <= shldVariable:
            toInvestVar   = toAdd
            toInvestFixed = 0

        elif toAdd > shldVariable:
            toInvestVar   = shldVariable
            toInvestFixed = toAdd - shldVariable

    return toInvestVar, toInvestFixed

def saveDataCsv(monthly,emergencies,mdgs,currVariable,curFixed,working,emerAmount,emerPer,investment,invPerc,varAmount,fixedAmount,comments):
    """Funcion para escribir informacion en un csv"""
    filePath = "./dataBase/"
    fileExt  = ".csv"
    os.makedirs(filePath, exist_ok=True)
    fileName = "Investments_2" + str(today.year) + fileExt

    filePointer = filePath + fileName

    data = {
        "Edad":getAge(getInvestorData(defaultId,1)),
        "Regla":str(getInvestorData(defaultId,2)),
        "Gastos_Mensuales":monthly,
        "Fondo_Emergencias_Actual":emergencies,
        "Meses_Gastos":mdgs,
        "Renta_Variable_Actual":currVariable,
        "Renta_Fija_Actual":curFixed,
        "Adicion_Total":working,
        "Adicion_Emergencias":emerAmount,
        "Porentaje_Emergencias":emerPer,
        "Adicion_Inversiones":investment,
        "Porcentaje_Inversiones":invPerc,
        "Adicion_Renta_Variable":varAmount,
        "Adicion_Renta_Fija":fixedAmount,
        "Fecha":date.today().isoformat(),
        "Comentarios":comments
    }

    newFile = not os.path.exists(filePointer)

    with open(filePointer, "a", newline="") as file:
        writer = csv.DictWriter(file,fieldnames=data.keys())
        if newFile:
            writer.writeheader()
        writer.writerow(data)

@functionLog
def saveDataBase(monthly,emergencies,mdgs,currVariable,curFixed,working,emerAmount,emerPer,investment,invPerc,varAmount,fixedAmount,comments) -> int:
    """Guarda información en la Base de Datos y devuelve el id del registro"""
    values  = []

    command = """INSERT INTO investments (
        investor, 
        age, 
        rule, 
        monthly_expenses, 
        current_emergency, 
        moe_equivalence, 
        current_variable, 
        current_fixed, 
        total_add, 
        emergency_add, 
        investments_add, 
        variable_add, 
        fixed_add, 
        emergency_percentage, 
        investments_percentage, 
        variable_percentage, 
        fixed_perentage, 
        comments, 
        date) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""

    values.append(defaultId)
    values.append(getAge(getInvestorData(defaultId,1)))
    values.append(getInvestorData(defaultId,2))
    values.append(monthly)
    values.append(emergencies)
    values.append(mdgs)
    values.append(currVariable)
    values.append(curFixed)
    values.append(working)
    values.append(emerAmount)
    values.append(investment)
    values.append(varAmount)
    values.append(fixedAmount)
    values.append(emerPer)
    values.append(invPerc)
    values.append(getInvestorData(defaultId,2)-(getAge(getInvestorData(defaultId,1)))) # variable_percentage
    values.append(100-(getInvestorData(defaultId,2)-(getAge(getInvestorData(defaultId,1))))) # fixed_perentage
    values.append(comments) # comments
    values.append(date.today().isoformat()) # date
    values = tuple(values)
    
    cursor.execute(command,values)
    
    recId = cursor.lastrowid

    conn.commit()
    conn.close

    return recId

@functionLog
def updateInvestor(emerFund:float, variableAmt:float, fixedAmt:float):
    """Actualiza registros de la tabla investors"""
    totalValue = round((variableAmt + fixedAmt),2)
    command = f"UPDATE investors SET emergency_fund = {emerFund}, variable_amt = {variableAmt}, fixed_amt = {fixedAmt}, total_portfolio = {totalValue}, last_update = datetime('now','localtime') WHERE id = {defaultId};"
    cursor.execute(command)
    conn.commit()
    conn.close
