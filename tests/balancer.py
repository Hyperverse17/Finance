try:
    from finance.core.properties import * #<carpetaorigen>.<nombreArchivoPy>
    from finance.core.functions import *
    from finance.core.balancers import *
    from finance.models.classes import noSuchRecord, dateError, updateDateError, greaterThanZeroError, zeroValueError

    investor = getInvestorById(defaultId)

    my_portfolio = {'S&P500':38630.47,  #VOO / VUAA
                      'EMERGENTES':7697.26, # VWO / VFEA (1491.23)
                      'FIBRAS':0, # VNQ (1680) / VREA
                      'ORO':0} # GLD

    
    to_add = 14583.16 - 7697.26

    objectives = portfolio_balancer(defaultId, "variable", my_portfolio, to_add)

    print(f"Destina los {to_add} de la siguiente manera:\n{objectives}")
    objectives_sum = sum(objectives.values())
    print(objectives_sum)

finally:
    print("\nFin del programa...\n")