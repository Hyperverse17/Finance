import os
try:
    from finance.core.properties import defaultId
    from finance.core.functions import getInvestorById
    from finance.core.balancers import *

    investor = getInvestorById(defaultId)
    print(f"\n ----- Bienvenido, {investor.name} ----- ")
    mode = input("\nInversión en Renta Fija o Variable (F/V) : ").upper() 
    to_add = float(input("Cuanto deseas agregar                    : "))
    
    if to_add <= 0:
        raise ValueError("Monto No Válido")
    
    os.system("cls")
    print(f"\nObteniendo objetivos de {investor.name}...")
    if mode in ('F','FIJA'):
        user_objectives = investor.fixed_objectives()
        mode = "fixed"

    elif mode in ('V','VARIABLE'):
        user_objectives = investor.variable_objectives()
        mode = "variable"

    else:
        user_objectives = investor.other_objectives()
        mode = "other"

    user_current_portfolio   = {}

    print("Obteniendo Portafolios actual...\n")
    for asset, weight in user_objectives.items():
        asset_amt = float(input(f"Ingresa total en {asset.capitalize()}: "))
        user_current_portfolio[asset] = round(asset_amt,2)
    
    user_distribution = portfolio_balancer(defaultId,mode,user_current_portfolio,to_add)

    os.system("cls")
    
    print("\n----- Distribuye de la siguiente manera -----\n")

    for asset, amount in user_distribution.items():
        print(f"{asset.capitalize()}: ${amount:,.2f}")

    print(f"--------------------\nTotal: ${to_add:,.2f}\n")
    os.system("pause")
    os.system("cls")
    print("\n--------- Porcentajes ---------- \n------ Esperado V.S. Real ------\n")

    total_portfolio = round(sum(user_current_portfolio.values()) + to_add,2)
    for asset, amount in user_distribution.items():
        expected_perc = round(user_objectives[asset]*100,2)
        actual_perc = round(((user_current_portfolio[asset] + amount)/total_portfolio*100),2)
        print(f"{asset.capitalize()}: {expected_perc}% V.S. {actual_perc}%")
    
except ValueError as e:
    print(e)

finally:
    print("\nFin del programa...\n")
