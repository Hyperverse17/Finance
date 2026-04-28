try:
    from finance.core.properties import * #<carpetaorigen>.<nombreArchivoPy>
    from finance.core.functions import *
    from finance.core.balancers import *
    from finance.models.classes import noSuchRecord, dateError, updateDateError, greaterThanZeroError, zeroValueError

    investor = getInvestorById(defaultId)

    curr_portfolio = {'S&P500':42021.08,
                      'Emergentes':0.0,
                      'Oro':0.0}

    to_add = float(input("\nCuanto deseas agregar: "))

    print(portfolio_balancer(defaultId,"variable",curr_portfolio,to_add))

    curr_portfolio = {'UDIBONOS':0.0,
                      'BONOS':0.0,
                      'CETES':0.0}

    to_add = float(input("\nCuanto deseas agregar: "))
    print(portfolio_balancer(defaultId,"fixed",curr_portfolio,to_add))


except:
    pass
finally:
    pass