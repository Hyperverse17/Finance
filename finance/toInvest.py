try:
    import os
    import time
    from Settings.properties import monthly, myBirthDay, sStars, investRule
    from Settings.functions import toInvest, emergencies, WantToRepeat, getAge, log
    scriptName = os.path.basename(__file__)
    
    goAhead = True
    log(sStars*3,scriptName)
    
    while goAhead:
        
        os.system("cls")
        print()
        print(sStars + f" Emergencias e Inersiones - {investRule} " + sStars)
        print()
        emerFunds = float(input("Fondo de Emergencias: "))
        toAdd     = float(input("Cuanto deseas añadir: "))
        mdg       = round(emerFunds/monthly,2)
        os.system("cls")
        print()
        print(sStars + " Resumen " + sStars)
        print(log(f"Gastos Mensuales     : ${monthly:,.2f}",scriptName))
        print(log(f"Fondo de Emergencias : ${emerFunds:,.2f}",scriptName) + f" ({mdg} MDG)")
        log(f"MDG                  : {mdg}",scriptName)
        log(f"Se agrega            : ${toAdd:,.2f}",scriptName)
        print(log(f"Edad                 : {getAge(myBirthDay)}",scriptName) + " Años")
        time.sleep(1)
        print()
        
#       Cálculos
        emerPerc    = emergencies(emerFunds)
        emergencias = toAdd*(emergencies(emerFunds)/100)
        inversion   = toAdd*((1-(emergencies(emerFunds)/100)))
         
        etfPerc   = toInvest()/100
        cetesPerc = 1-(toInvest()/100)
        
        emerAmount = round(emergencias,2)
        etfAmount = round(inversion*etfPerc,2)
        cetesAmount = round(inversion*cetesPerc,2)

        str1 = f"Destina los ${toAdd:,.2f} de la siguiente manera: "
        str2 = f"{emergencies(emerFunds)}% a Emergencias y {(100-emergencies(emerFunds))}% a Inversiones"
        print(str1 + str2)
        log(f"Emergencias          : {round(emergencies(emerFunds),2)}%",scriptName)
        log(f"Inversiones          : {round(100-(emergencies(emerFunds)),2)}%",scriptName)
        log(f"  - Renta variable   : {round(toInvest(),2)}%",scriptName)
        log(f"  - Renta fija       : {round((100-toInvest()),2)}%",scriptName)
        print(log("",scriptName))
        print(log(f"Emergencias          : ${emerAmount:,.2f}",scriptName))
        print("Inversiones")
        log(f"Total inversiones    : ${inversion:,.2f}",scriptName)
        print(log(f" - Renta Variable    : ${etfAmount:,.2f}",scriptName))
        print(log(f" - Renta Fija        : ${cetesAmount:,.2f}",scriptName))
        print()
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

finally:
    print()
    print(log("Fin del programa",scriptName))
    print()
    time.sleep(2)