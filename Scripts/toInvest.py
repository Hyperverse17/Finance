try:
    import os
    import time
    import sqlite3
    from finance.core.properties import goAhead, sStars, saveData, table1, defaultId #<carpetaorigen>.<nombreArchivoPy>
    from finance.core.functions import splitter, investAdjust, WantToRepeat, getInvestorById, recordExistance, log, saveDataBase, wannaSave, updateInvestor
    from finance.models.classes import noSuchRecord, greaterThanZeroError

    scriptName = "toInvest.py" # os.path.basename(__file__)
    log(sStars*3,scriptName)
    log("Obteniendo inversor...",scriptName)
    investor   = getInvestorById(defaultId)
    if investor is None:
        raise noSuchRecord
    else:    
        age        = investor.age
        investRule = investor.investment_rule 
        monthly    = investor.monthly_expenses
        name       = investor.name
        log(f"Inicia sesion        : [{defaultId}] {name}",scriptName)

    while goAhead:
        saveData = False    
        os.system("cls")
        print()
        print(sStars + f" Emergencias e Inversiones - {investRule} " + sStars)
        print(f"                         Hola, {name}!")
        print()
        emerFunds    = float(input("Fondo de Emergencias    : "))
        currVariable = float(input("Total en Renta Variable : "))
        currFixed    = float(input("Total en Renta Fija     : "))
        toAdd        = float(input("Cuanto deseas agregar   : "))

        if toAdd <= 0:
            raise greaterThanZeroError
        
        justInvest   = input("Solo Inversion (s/n)?   : ")
        
        if justInvest == 's' or justInvest == 'S':
            justInvest = True
            message1 = " (Sólo inv)."
        else:
            justInvest = False
            message1 = ""

        mdg = round(emerFunds/monthly,2)

        os.system("cls")
        print()
        print(sStars + " Resumen " + sStars)
        print(log(f"Gastos Mensuales     : ${monthly:,.2f}",scriptName))
        print(log(f"Fondo de Emergencias : ${emerFunds:,.2f}",scriptName) + f" ({mdg} MDG)")
        log(f"MDG                  : {mdg}",scriptName)
        print(log(f"Renta Variable       : ${currVariable:,.2f}",scriptName))
        print(log(f"Renta Fija           : ${currFixed:,.2f}",scriptName))
        print(log(f"Edad                 : {age}",scriptName) + " Años")
        time.sleep(1)
        print()
        
#       Cálculos
        emerPerc, nextLevel = splitter(emerFunds,monthly,justInvest)
        toJump = nextLevel-emerFunds
           
        if toAdd > toJump:
            log("*** Ajuste Fondo de Emergencias ***",scriptName)
            log(f"Se agrega            : ${toJump:,.2f}",scriptName)
            print(f"Primero agrega ${toJump:,.2f} a Emergencias y después")
            toAdd     = toAdd - toJump
            emerFunds = emerFunds + toJump
            emerPerc, nextLevel = splitter(emerFunds,monthly,justInvest)
        
        log(f"Se trabaja con       : ${toAdd:,.2f}",scriptName)
            
        emergencias                = toAdd*(emerPerc/100) # Total para emergencias
        inversion                  = toAdd*((1-(emerPerc/100))) # Total pra inversiones
        variablePer                = (investRule-age)
        toInvestVar, toInvestFixed = investAdjust(currVariable, currFixed, inversion, variablePer) # Renta variable y renta fija
         
        emerAmount  = round(emergencias,2)
        etfAmount   = round(toInvestVar,2)
        cetesAmount = round(toInvestFixed,2)

        print(f"Destina los ${toAdd:,.2f} de la siguiente manera: ")
        print(f"{emerPerc}% a Emergencias y {(100-emerPerc)}% a Inversiones")
        log(f"Emergencias          : {round(emerPerc,2)}%",scriptName)
        log(f"Inversiones          : {round(100-(emerPerc),2)}%",scriptName)
        log(f"  - Renta variable   : {round(variablePer,2)}%",scriptName)
        log(f"  - Renta fija       : {round((100-variablePer),2)}%",scriptName)
        print(log("",scriptName))
        print(log(f"Emergencias          : ${emerAmount:,.2f}",scriptName))
        print("Inversiones")
        log(f"Total inversiones    : ${inversion:,.2f}",scriptName)
        print(log(f" - Renta Variable    : ${etfAmount:,.2f}",scriptName))
        print(log(f" - Renta Fija        : ${cetesAmount:,.2f}",scriptName))
        print(log("",scriptName))
        print(log(f"Siguiente objetivo   : ${nextLevel:,.2f}",scriptName))

        comments = input("Comentarios          : ")
        saveData = wannaSave(saveData)
        
        if saveData:
            newRec = saveDataBase(investor,emerFunds,mdg,currVariable,currFixed,toAdd,emerAmount,emerPerc,inversion,(100-emerPerc),etfAmount,cetesAmount,comments+message1)
            investor.emergency_fund = (emerFunds + emerAmount)
            investor.variable_amt   = (currVariable + etfAmount)
            investor.fixed_amt      = (currFixed + cetesAmount)
            updateInvestor(investor)
            print(f"Informacion guardada en la base de datos con el ID: {newRec}")

        goAhead = WantToRepeat(goAhead)
        log(f"Repeat: {goAhead}",scriptName)

except ImportError as e:
    os.system("cls")
    print()
    print("Algo anda mal con la importación...")
    print(log(f"{e}",scriptName))

except noSuchRecord as e:
    os.system("cls")
    print()
    print(log(f"{e}: {defaultId}",scriptName))

except greaterThanZeroError as e:
    os.system("cls")
    print()
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
    