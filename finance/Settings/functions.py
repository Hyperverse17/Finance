import os
import functools
from Settings.properties import *
from typing import Union
from datetime import date, datetime
import calendar

workingDate = today.strftime("%y-%m-%d ")

monthA = paymentDay.month
monthB = nextPayDay.month
monthName = calendar.month_name[monthA][:3]

if monthA == monthB:
    payment = "1"
else:
    payment = "2"

logPath     = "./logs/"
fileName    = "log_" + monthName + "_" + str(paymentDay.year) + "_" + payment + ".txt"
filePointer = logPath + fileName

def loggerArgs(filePointer):
    """Decorador para funciones que reciben parámetros y que retornan valores"""
    def decorator(func):
        @functools.wraps(func) 
        def wrapper(*args, **kwargs):
            dateTimeMark = datetime.now().strftime("%H:%M:%S") #Objeto tipo date time (genera una marca de tiempo)
            sDateTimeMarkFmt = workingDate + dateTimeMark # formato a la marca de tiempo, genera string YYMMDDhhmmss
            result = func(*args, **kwargs)
            message = "[LOG " + sDateTimeMarkFmt + f"] {result}"
            with open(filePointer, "a") as file:
                file.write(message + "\n")
            return result
        return wrapper
    return decorator

@loggerArgs(filePointer)
def logging(inMessage:str)-> str:
    """Funcion auxiliar que guarda en un log el string que se le pasa"""
    outMessage = inMessage
    return outMessage

def WantToRepeat(goAhead:bool) -> bool:
    """Funcion auxiliar para repetir un proceso"""
    print()
    os.system("pause")
    os.system("cls")
    if goAhead == True:
        userAnswer = input("Deseas repetir el proceso? (s/n) 🤔 :")
        if userAnswer == 's' or userAnswer == 'S':
            os.system("cls")
        else:
            goAhead = False
        logging("Repeat : " + str(goAhead))
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

