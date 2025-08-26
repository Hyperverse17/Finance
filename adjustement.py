
try:
    import os
    import time
    from Settings.properties import investRule
    from Settings.functions import log, WantToRepeat, toInvest, investAdjust
    scriptName = os.path.basename(__file__)
    
    print()
    goAhead = True
    while goAhead:

        variablePer = toInvest()
        fixedPer    = 100-variablePer

        currVariable = float(input("Ingresa el monto de Renta Variable : "))
        currFixed    = float(input("Ingresa el monto de Renta Fija     : "))
        toAdd        = float(input("Ingresa cuanto deseas agregar      : "))
        investTotal  = currVariable + currFixed

        os.system("cls")

        print(f"Se usa regla del {investRule}")
        print(f"Total de tus inversiones: ${investTotal:,.2f}")
        print(f"Ajustando {variablePer}% en Renta Variable y {fixedPer}% en Renta Fija ...")
        print()
        
        time.sleep(1)

        toInvestVar, toInvestFixed = investAdjust(currVariable, currFixed, toAdd)    
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
