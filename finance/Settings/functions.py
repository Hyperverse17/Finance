import os
import functools
from Settings.properties import *
from typing import Union
from datetime import datetime
import calendar

def getFilePointer(scriptName):
    logPath = "./logs/"
    ext     = ".txt"
    os.makedirs(logPath, exist_ok=True)
    
    monthA    = paymentDay.month
    monthB    = nextPayDay.month
    monthName = calendar.month_name[monthA][:3]

    if monthA == monthB:
        payment = "1"
    else:
        payment = "2"

    if scriptName == "todaysBalance.py":
        fileName = "balance_log_" + monthName + "_" + str(paymentDay.year) + "_" + payment + ext
        
    elif scriptName == "toInvest.py":
        fileName = "invest_" + str(investRule) + "_log_" + str(today.year) + "_" + ext
    
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

@writeLog
def log(inMessage:str, scriptName:str)-> str:
    """Funcion auxiliar que guarda en un log el string que se le pasa"""
    outMessage = inMessage
    return outMessage

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

def getAge(birthDay:str) -> int:
    """Recibe un string con una fecha de nacimiento YYYY-MM-DD y devuelve un entero con la edad en años"""
    today     = datetime.today()
    birthDate = datetime.strptime(birthDay, "%Y-%m-%d")
    age = int(today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))) # Se hace un comparativo entre mes y día (del día) y de mes y dia del cumpleaños, si el resultado es true, al evaluarse se considera como 1, si es false, 0
    return age

def toInvest():
    myAge = getAge(myBirthDay)
    toInvestPerc = investRule-myAge
    return toInvestPerc

def getMdgs():
    months = (  1, 3, 6,12,24,symbolicLimit)
    mdgs   = [x * monthly for x in months]
    return mdgs

def splitter(total):
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

    emerPerc  = emePerces[position]
    nextLevel = mdgs[position]
    
    return emerPerc
