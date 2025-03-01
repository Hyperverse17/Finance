import os
import functools
from Settings.properties import *
from typing import Union

logPath = "./logs/"
fileName = "log_2502_1.txt"
filePointer = logPath + fileName

def loggerArgs(filePointer):
    """Decorador para funciones que reciben parámetros y que retornan valores"""
    def decorator(func):
        @functools.wraps(func) 
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            message = f"[LOG] {result}"
            with open(filePointer, "a") as file:
                file.write(message + "\n")
            return result
        return wrapper
    return decorator

def WantToRepeat(goAhead:bool) -> bool:
    print()
    os.system("pause")
    os.system("cls")
    if goAhead == True:
        userAnswer = input("Deseas repetir el proceso? (s/n) 🤔 :")
        if userAnswer == 's' or userAnswer == 'S':
            os.system("cls")
        else:
            goAhead = False
    return goAhead


def addition() -> Union[int, float]:
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

@loggerArgs(filePointer)
def loggingBypass(inMessage:str)-> str:
    outMessage = inMessage
    return outMessage
