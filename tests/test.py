try:
    from finance.core.properties import defaultId
    from finance.models.classes import Investment
    from finance.core.functions import getInvestorById

    print("\nInversiones")
    investor = getInvestorById(defaultId)

    curr_variable = float(input("Actual variable: "))
    curr_fixed = float(input("Actual Fija: "))
    to_add = float(input("Agregar: "))

    investment = Investment(investor.age, investor.investment_rule, curr_variable, curr_fixed, to_add, False)
    print("\n" + investment.__str__())
    print(f"\nTotal Actual: ${investment.curr_portfolio_value:,.2f}")
    print(f"    Actual Variable: ${investment.curr_variable:,.2f} ({investment.curr_variable_perc*100}%)")
    print(f"    Actual Fija: ${investment.curr_fixed:,.2f} ({investment.curr_fixed_perc*100}%)")

    print(f"\nAdición Total: ${investment.total_add:,.2f}")
    print(f"    Adición Variable: ${investment.variable_add:,.2f}")
    print(f"    Adición Fija: ${investment.fixed_add:,.2f}")
    
    print(f"\nNuevo Total: ${investment.new_portfolio_value:,.2f}")
    print(f"    Nuevo Variable: ${investment.new_variable:,.2f} ({investment.new_variable_perc*100}%)")
    print(f"    Nuevo Fija: ${investment.new_fixed:,.2f} ({investment.new_fixed_perc*100}%)")

finally:
    print("\nFin\n")





