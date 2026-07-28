try:
    from finance.core.properties import defaultId
    from finance.models.classes import Budget
    from finance.core.functions import *
    from finance.models.classes import noSuchRecord, dateError, updateDateError, greaterThanZeroError, zeroValueError

    print("\nPresupuesto")
    investor = getInvestorById(defaultId)

    paymentDay  = datetime.strptime(getParameters(defaultId,1), "%Y-%m-%d").date()
    nextPayDay  = datetime.strptime(getParameters(defaultId,2), "%Y-%m-%d").date()
    totalBudget = float(getParameters(defaultId,3))
    current = float(input("Cuanto tienes hoy: "))
    
    user_budget = Budget(totalBudget, paymentDay, nextPayDay)
    print("\n" + user_budget.__str__())
    print(f"Dia : {user_budget.current_day} de {user_budget.all.days}")
    print(f"Han pasado {user_budget.elapsed.days} de {user_budget.all.days} Dias")
    print(f"Restan: {user_budget.remaining.days} Dias")
    print(f"Presupuesto Diario: ${user_budget.daily_budget:,.2f}")
    print(f"\nDeberias tener: ${user_budget.should_amount:,.2f}")
    print(f"Tienes: ${current:,.2f}")
    print(f"{user_budget.status(current)}")

except ValueError as e:
    print(f"\nError: {e}")

finally:
    print("\nFin\n")

