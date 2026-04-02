
from finance.core.balancers import portfolio_balancer

print("\n ----- Balanceador de Renta Variable ----- \n")

my_portfolio = {}

type = input("Fija/Variable (0,1): ")

if type == "0":
    my_portfolio['CETES'] = float(input("Total en CETES: "))
    my_portfolio['BONOS'] = float(input("Total en Bonos: "))
    my_portfolio['UDIBONOS'] = float(input("Total UDIBonos: "))
    type = "fixed"
    
elif type == "1":
    my_portfolio['S&P500'] = float(input("Total en S&P500: "))
    my_portfolio['Emergentes'] = float(input("Total en Mercados Emergentes: "))
    my_portfolio['Oro'] = float(input("Total en Oro: "))
    type = "variable"

to_add = float(input("Nueva Inversion: "))

distribution = portfolio_balancer(type,my_portfolio,to_add)

for asset, amount in distribution.items():
    print(f"Destinar a {asset}: ${amount:,.2f}")

