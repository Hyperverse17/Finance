try:
    import os
    import time
    import sqlite3
    from Settings.properties import monthly, myBirthDay, sStars, investRule
    from Settings.functions import toInvest, splitter, investAdjust, WantToRepeat, getAge, log, saveDataCsv, saveDataBase
    scriptName = os.path.basename(__file__)
    
    e = ".v"
    goAhead = True
    log(sStars*3,scriptName)
    
    while goAhead:
        
        os.system("cls")
        print()
        print(sStars + f" Emergencias e Inersiones - {investRule} " + sStars)
        print()
        emerFunds    = float(input("Fondo de Emergencias    : "))
        currVariable = float(input("Total en Renta Variable : "))
        currFixed    = float(input("Total en Renta Fija     : "))
        toAdd        = float(input("Cuanto deseas añadir    : "))
        mdg          = round(emerFunds/monthly,2)

        os.system("cls")
        print()
        print(sStars + " Resumen " + sStars)
        print(log(f"Gastos Mensuales     : ${monthly:,.2f}",scriptName))
        print(log(f"Fondo de Emergencias : ${emerFunds:,.2f}",scriptName) + f" ({mdg} MDG)")
        log(f"MDG                  : {mdg}",scriptName)
        print(log(f"Renta Variable       : ${currVariable:,.2f}",scriptName))
        print(log(f"Renta Fija           : ${currFixed:,.2f}",scriptName))
        print(log(f"Edad                 : {getAge(myBirthDay)}",scriptName) + " Años")
        time.sleep(1)
        print()
        
#       Cálculos
        emerPerc, nextLevel = splitter(emerFunds)
        toJump = nextLevel-emerFunds
           
        if toAdd > toJump:
            log("*** Ajuste Fondo de Emergencias ***",scriptName)
            log(f"Se agrega            : ${toJump:,.2f}",scriptName)
            print(f"Primero agrega ${toJump:,.2f} a Emergencias y después")
            toAdd     = toAdd - toJump
            emerFunds = emerFunds + toJump
            emerPerc, nextLevel = splitter(emerFunds)
        
        log(f"Se trabaja con       : ${toAdd:,.2f}",scriptName)
            
        emergencias                = toAdd*(emerPerc/100) # Total para emergencias
        inversion                  = toAdd*((1-(emerPerc/100))) # Total pra inversiones
        toInvestVar, toInvestFixed = investAdjust(currVariable, currFixed, inversion) # Renta variable y renta fija
         
        emerAmount  = round(emergencias,2)
        etfAmount   = round(toInvestVar,2)
        cetesAmount = round(toInvestFixed,2)

        print(f"Destina los ${toAdd:,.2f} de la siguiente manera: ")
        print()
        print(f"{emerPerc}% a Emergencias y {(100-emerPerc)}% a Inversiones")
        log(f"Emergencias          : {round(emerPerc,2)}%",scriptName)
        log(f"Inversiones          : {round(100-(emerPerc),2)}%",scriptName)
        log(f"  - Renta variable   : {round(toInvest(),2)}%",scriptName)
        log(f"  - Renta fija       : {round((100-toInvest()),2)}%",scriptName)
        print(log("",scriptName))
        print(log(f"Emergencias          : ${emerAmount:,.2f}",scriptName))
        print("Inversiones")
        log(f"Total inversiones    : ${inversion:,.2f}",scriptName)
        print(log(f" - Renta Variable    : ${etfAmount:,.2f}",scriptName))
        print(log(f" - Renta Fija        : ${cetesAmount:,.2f}",scriptName))
        print(log("",scriptName))
        print(log(f"Siguiente objetivo   : ${nextLevel:,.2f}",scriptName))
        print()

        comments = input("Comentarios          : ")

        saveDataBase(monthly,emerFunds,mdg,currVariable,currFixed,toAdd,emerAmount,emerPerc,inversion,(100-emerPerc),etfAmount,cetesAmount,comments)

        goAhead = WantToRepeat(goAhead)
        log(f"Repeat: {goAhead}",scriptName)

except ImportError as e:
    os.system("cls")
    print()
    print("Algo anda mal con la importación...")
    print(log(f"{e}",scriptName))

except ValueError as e:
    os.system("cls")
    print()
    print("Tipo de dato no permitido!")
    print(log(f"{e}",scriptName))

except PermissionError as e:
    os.system("cls")
    print()
    print("Cierra el archivo csv!")
    print(log(f"{e}",scriptName))

except sqlite3.DatabaseError as e:
    os.system("cls")
    print()
    print("Problema con la BD")
    print(log(f"{e}",scriptName))

finally:
    print()
    print(log("Fin del programa",scriptName))
    print()
    time.sleep(2)