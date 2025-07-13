try:
    import os
    import time
    from Settings.properties import monthly, myBirthDay, sStars
    from Settings.functions import toInvest, emergencies, WantToRepeat, getAge

    goAhead = True

    while goAhead:
        os.system("cls")
        print()
        print(sStars + " Emergencias e Inersiones " + sStars)
        print()
        emerFunds = float(input("Fondo de Emergencias: "))
        toAdd     = float(input("Cuanto deseas añadir: "))
        mdg       = round(emerFunds/monthly,2)
        os.system("cls")
        print()
        print(sStars + " Resumen " + sStars)
        print(f"Gastos Mensuales     : $ {monthly:,.2f}")
        print(f"Fondo de Emergencias : $ {emerFunds:,.2f} ({mdg} MDG)")
        print(f"Edad                 : {getAge(myBirthDay)} años")
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

        str1 = f"Destina los $ {toAdd:,.2f} de la siguiente manera: "
        str2 = f"{emergencies(emerFunds)}% a Emergencias y {(100-emergencies(emerFunds))}% a Inversiones"
        print(str1 + str2)
        print()
        
        print(f"Emergencias    > $ {emerAmount:,.2f}")
        print(f"Renta Variable > $ {etfAmount:,.2f}")
        print(f"Renta Fija     > $ {cetesAmount:,.2f}")
        print()
        goAhead = WantToRepeat(goAhead)

except ImportError as e:
    os.system("cls")
    print()
    print("Algo anda mal con la importación...")
    print(f"{e}")

except ValueError as e:
    os.system("cls")
    print()
    print("Tipo de dato no permitido!")
    print(f"{e}")

finally:
    print()
    print("Fin del programa")
    print()
    time.sleep(3)