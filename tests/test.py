try:
    from finance.core.properties import defaultId
    from finance.models.classes import Investment
    from finance.core.functions import getInvestorById

    print("\nInversiones")
    
    investor = getInvestorById(defaultId)

    curr_fixed = float(input("Actual Fija: "))
    curr_variable = float(input("Actual variable: "))
    to_add = float(input("Agregar: "))

    investment = Investment(investor.age, investor.investment_rule, curr_variable, curr_fixed, to_add)
    to_add_variable, to_add_fixed = investment.fixed_variable()

    print(f"\nTotal Actual: {investment.curr_total}")
    print(f"\nVariable, fija: {to_add_variable}, {to_add_fixed}")

finally:
    print("\nFin\n")





