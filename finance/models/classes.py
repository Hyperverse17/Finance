from datetime import datetime
class User:
    """Usuarios del sistema"""
    def __init__(self, id: int | None, name: str, last_name: str, birthday:str, gender:str, email:str):
        today = datetime.today()
        self.id = id
        self.name = name.title()
        self.last_name = last_name.title()
        self.birthday = birthday
        birthday_date = datetime.strptime(self.birthday, "%Y-%m-%d")   
        self.age = int(today.year - birthday_date.year - ((today.month, today.day) < (birthday_date.month, birthday_date.day))) # Se hace un comparativo entre mes y día (del día) y de mes y dia del cumpleaños, si el resultado es true, al evaluarse se considera como 1, si es false, 0
        self.gender = gender.title()
        self.email = email
        self.active = True
        self.usr_last_update = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class Investor(User):
    """Inversores"""
    def __init__(self, user: User, nickname: str, investment_rule: int, monthly_expenses: float, emergency_fund: float, variable_amt: float, fixed_amt: float):
        super().__init__(user.id, user.name, user.last_name, user.birthday, user.gender, user.email)
        self.nickname = nickname
        self.investment_rule = investment_rule
        self.monthly_expenses = monthly_expenses
        self.emergency_fund = emergency_fund
        self.variable_amt = variable_amt
        self.fixed_amt = fixed_amt
        self.inv_last_update = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def getTotalPortfolio(self) -> float:
        """Devuelve la suma de variable amount y fixed amount"""
        totalPortfolio = round(self.variable_amt + self.fixed_amt,2)
        return totalPortfolio
        
class Investment():
    pass

# Errors
class updateDateError(Exception):
    def __init__(self) -> None:
        self.message = "Actualizar fecha de pago y fecha de proximo pago"
        super().__init__(self.message)

class greaterThanZeroError(Exception):
    def __init__(self) -> None:
        self.message = "El monto debe ser mayor que cero"
        super().__init__(self.message)

class noSuchRecord(Exception):
    def __init__(self) -> None:
        self.message = "No existe el id"
        super().__init__(self.message)

dateError = updateDateError()
zeroValueError = greaterThanZeroError()

