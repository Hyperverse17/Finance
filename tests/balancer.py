try:
    from finance.core.properties import * #<carpetaorigen>.<nombreArchivoPy>
    from finance.core.functions import *
    from finance.core.balancers import *
    from finance.models.classes import noSuchRecord, dateError, updateDateError, greaterThanZeroError, zeroValueError

    investor = getInvestorById(defaultId)

    general_A = {'VARIABLE':0,
               'FIXED':10000}
    
    to_add = 1000
    variable_per = 110 - investor.age

    for counter in range (1, 21):
        print(f"-------- Iteración: {counter} --------")

        variable_A = round(general_A['VARIABLE'],2)
        fixed_A = round(general_A['FIXED'],2)
        total_A = variable_A + fixed_A
        per_var_A = round((variable_A/total_A)*100,2)
        per_fix_A = round((fixed_A/total_A)*100,2)
        print(f"Portafolios actual A: ({round(variable_A,2)}, {round(fixed_A,2)}) - ({per_var_A}% , {per_fix_A}%) de {total_A}")

        toInvestVar, toInvestFixed = investAdjust(general_A['VARIABLE'], general_A['FIXED'], to_add, variable_per)

        toInvestVar = round(toInvestVar,2)
        toInvestFixed = round(toInvestFixed,2)

        general_A['VARIABLE'] += toInvestVar
        general_A['FIXED'] += toInvestFixed

        print(f"Adición Nuevo Método : ({toInvestVar}, {toInvestFixed})\n")
        
finally:
    print("\nFin del programa...\n")