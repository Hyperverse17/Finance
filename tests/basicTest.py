
from finance.models.classes import *

print("\n ----- Pruebas con clases ----- \n")

user1 = User(1,"otelo jovani", "galicia garcia", "1991-07-17", "male", "jovanigalicia17@gmail.com")
investor1 = Investor(user1,"Hyperverse", 110, 33000.5689, 45000.0236, 31000.7878, 10000.99)


print(user1)
print(investor1)

print(investor1.emergency_fund)
print(investor1.fixed_amt)
print(investor1.variable_amt)
print(investor1.getTotalPortfolio())
