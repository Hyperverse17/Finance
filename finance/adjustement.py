
try:
    import os
    import time
    from Settings.properties import investRule
    from Settings.functions import log, WantToRepeat, toInvest, addition
    scriptName = os.path.basename(__file__)
    
    print()
    goAhead = True
    while goAhead:
        variablePer = toInvest()
        fixedPer    = 100-variablePer

        currVariable = float(input("Ingresa el monto de Renta Variable : "))
        currFixed    = float(input("Ingresa el monto de Renta Fija     : "))
        toAdd        = float(input("Ingresa cuanto deseas agregar      : "))
        
        os.system("cls")
        investTotal  = currVariable + currFixed
        #grandTotal   = investTotal + toAdd
        
        shldVariable = investTotal*(variablePer/100)
        shldFixed    = investTotal*(fixedPer/100)
        
        variableDiff = shldVariable-currVariable
        fixedDiff    = shldFixed-currFixed
            
        toAddVariable = toAdd*(variablePer/100)
        toAddFixed    = toAdd*(fixedPer/100)

        toInvestVar   = toAddVariable + variableDiff
        toInvestFixed = toAddFixed + fixedDiff 

        #grandVariable = grandTotal*(variablePer/100)
        #grandFixed    = grandTotal*(fixedPer/100)

        print(f"Se usa regla del {investRule}")
        print(f"Total de tus inversiones: ${investTotal:,.2f}")
        print(f"Ajustando {variablePer}% en Renta Variable y {fixedPer}% en Renta Fija ...")
        print()
        
        time.sleep(1)

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
            
        print(f"A invertir (v/f)  : {toInvestVar:,.2f}, {toInvestFixed:,.2f}")

        goAhead = WantToRepeat(goAhead)

except ImportError as e:
    os.system("cls")
    print()
    print("Algo anda mal con la importación...")
    #print(log(f"{e}",scriptName))

except ValueError as e:
    os.system("cls")
    print()
    print("Tipo de dato no permitido!")
    #print(log(f"{e}",scriptName))

finally:
    print()
    print("Fin del programa")
    print()
    time.sleep(2)
