
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
        os.system("cls")
        grandTotal   = currVariable + currFixed
        
        shldVariable = grandTotal*(variablePer/100)
        shldFixed    = grandTotal*(fixedPer/100)
        
        fixedDiff    = shldFixed-currFixed
        variableDiff = shldVariable-currVariable

        print(f"Se usa regla del {investRule}")
        print(f"Total de tus inversiones: ${grandTotal:,.2f}")
        print(f"Ajustando {variablePer}% en Renta Variable y {fixedPer}% en Renta Fija ...")
        print()
        
        time.sleep(1)

        if fixedDiff < 0 and variableDiff > 0:
            print(f"Retira {fixedDiff:,.2f} de renta fija y pasalos a renta variable")

        elif fixedDiff > 0 and variableDiff < 0:
            print(f"Retira {variableDiff:,.2f} de renta variable y pasalos a renta fija")

        else:
            print("Tu portafolios esta perfectamente balanceado")


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
