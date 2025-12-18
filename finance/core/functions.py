import os
import functools
import calendar
from typing import Union
from datetime import datetime, date
from finance.models.classes import Investor, User
from finance.core.properties import *
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
def getMdgs(monthly):
    """Regresa un arreglo con la escala de MDGS"""
    months = (1, 3, 6, 12, 24, symbolicLimit)
    mdgs   = [x * monthly for x in months]
    return mdgs

@functionLog
def splitter(total,monthly,mode):
    """Regresa el porcentaje que debe ser destinado al fondo de emergencias"""
    emePerces = (100,75,50,25,15,10)
    mdgs      = getMdgs(monthly)
    
    if total >= mdgs[0]: # si es mayor o igual a 1 MDG
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
def investAdjust(currVariable:float, currFixed:float, toAdd:float, variablePer:int):
    """Funcion que determina cuando destinar a Renta Variable y Renta Fija"""

    fixedPer     = 100-variablePer
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

@functionLog
def saveDataBase(investor: Investor,emergencies,mdgs,currVariable,curFixed,working,emerAmount,emerPer,investment,invPerc,varAmount,fixedAmount,comments) -> int:
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
    values.append(investor.age)
    values.append(investor.investment_rule)
    values.append(investor.monthly_expenses)
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
    values.append(investor.investment_rule-investor.age) # variable_percentage
    values.append(100-(investor.investment_rule-investor.age)) # fixed_perentage
    values.append(comments) # comments
    values.append(date.today().isoformat()) # date
    values = tuple(values)
    
    cursor.execute(command,values)
    
    recId = cursor.lastrowid

    conn.commit()
    conn.close

    return recId

@functionLog
def updateInvestor(investor: Investor):
    """Actualiza registros de la tabla investors"""
    totalValue = investor.getTotalPortfolio()
    command = f"UPDATE investors SET emergency_fund = {investor.emergency_fund}, variable_amt = {investor.variable_amt}, fixed_amt = {investor.fixed_amt}, total_portfolio = {totalValue}, last_update = '{investor.inv_last_update}' WHERE id = {defaultId};"
    cursor.execute(command)
    conn.commit()
    conn.close

@functionLog
def updateDates():
    """Función para actualizar fechas de operación"""
    userAnswer = input("\nDeseas actualizar las fechas? (s/n) 🤔: ")
    message = ""
    if userAnswer == 's' or userAnswer == 'S':
        os.system("cls")
        values = []
        paymentDate = input("Ingresa Fecha de Pago         : ")
        nextPaymentDate = input("Ingresa Fecha de Próximo Pago : ")
        budget = input("Ingresa Presupuesto           : ")
        command = """INSERT INTO parameters (payment_day, next_payment_day, free_spending, user_id) VALUES (?, ?, ?, ?);"""
        values.append(paymentDate)
        values.append(nextPaymentDate)
        values.append(budget)
        values.append(defaultId)
        values = tuple(values)

        cursor.execute(command,values)
        conn.commit()
        conn.close
        message = f"Informacion actualizada correctamente!"

        return message
    
@functionLog
def rowToUser(user_row) -> User:
    """Instancia un objeto de User a partir de un select"""
    user = User(id=user_row[0], name=user_row[1], last_name=user_row[2], birthday=user_row[3], gender=user_row[4], email=user_row[5])
    return user

@functionLog
def getUserById(user_id:int) -> User | None:
    """Hace select a users"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""SELECT id, name, last_name, birthday, gender, email, active FROM users WHERE id = ?""",(user_id,),)
    user_row = cursor.fetchone()
    conn.close()
    if user_row is None:
        return None
    else:
        return rowToUser(user_row)

@functionLog
def rowToInvestor(investor_row) -> Investor:
    """Instancia un objeto de Investor a partir de un select"""
    user_id = investor_row[0]
    user    = getUserById(user_id)
    investor = Investor(user, nickname=investor_row[1], investment_rule=investor_row[2], monthly_expenses=investor_row[3], emergency_fund=investor_row[4], variable_amt=investor_row[5], fixed_amt=investor_row[6])
    return investor

@functionLog
def getInvestorById(investor_id: int) -> Investor | None:
    """Hace select a Investors """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""SELECT user_id, nickname, investment_rule, monthly_expenses, emergency_fund, variable_amt, fixed_amt FROM investors WHERE id = ?""",(investor_id,),)
    investor_row = cursor.fetchone()
    conn.close()

    if investor_row is None:
        return None
    else:
        return rowToInvestor(investor_row)
    

