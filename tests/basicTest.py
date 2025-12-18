from finance.core.functions import getInvestorById, getUserById

print("\n--- Test de clases y funciones ---\n")

id = int(input("\nIngresa un id: "))

user = getUserById(id)
print(user.name)
print(user.last_name)
print(user.age)

investor = getInvestorById(id)
if investor != None:
    print(investor.name)
    print(investor.last_name)
    print(investor.birthday)
    print(investor.email)
    print(investor.age)
    print(investor.gender)

    print(investor.nickname)
    print(investor.investment_rule)
    print(investor.getTotalPortfolio())
    print(investor.last_update)