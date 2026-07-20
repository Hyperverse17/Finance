from datetime import datetime
from data.databases.distributions import *
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
    
    def __str__(self) -> str:
        """Retorna un string con información de cada instancia de User"""
        if self.active:
            status = "Active"
        else:
            status = "Inctive"

        return f"User {self.id} ({status}): {self.name} {self.last_name}."

class Investor(User):
    """Inversores"""
    def __init__(self, user: User, nickname: str, investment_rule: int, monthly_expenses: float, emergency_fund: float, variable_amt: float, fixed_amt: float):
        super().__init__(user.id, user.name, user.last_name, user.birthday, user.gender, user.email)
        self.nickname = nickname
        self.investment_rule = investment_rule
        self.monthly_expenses = round(monthly_expenses,2)
        self.emergency_fund = round(emergency_fund,2)
        self.variable_amt = round(variable_amt,2)
        self.fixed_amt = round(fixed_amt,2)
        self.inv_last_update = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self) -> str:
        """Retorna un string con información de cada instancia de Investor"""
        if self.active:
            status = "Active"
        else:
            status = "Inctive"
        return f"Investor {self.id} ({status}): {self.name} {self.last_name} [{self.nickname}]."

    def getTotalPortfolio(self) -> float:
        """Devuelve la suma de variable amount y fixed amount"""
        totalPortfolio = round(self.variable_amt + self.fixed_amt,2)
        return totalPortfolio
    
    def variable_objectives(self):
        try:
            self.variable_objectives = get_variable_objectives(self.id)
            return self.variable_objectives
        except ValueError as error:
            print(error)

    def fixed_objectives(self):
        try:
            self.fixed_objectives = get_fixed_objectives(self.id)
            return self.fixed_objectives
        except ValueError as error:
            print(error)

    def other_objectives(self):
        try:
            self.other_objectives = get_other_objectives(self.id)
            return self.other_objectives
        except ValueError as error:
            print(error)

class Investment():
    def __init__(self, investor_age:int, investment_rule:int, curr_variable:float, curr_fixed:float, to_add:float) -> None:
        self.investment_rule = investment_rule
        self.investor_age = investor_age 
        self.curr_variable = curr_variable
        self.curr_fixed = curr_fixed
        self.to_add = to_add
        self.curr_total = self.curr_variable + self.curr_fixed 
      
    def fixed_variable(self, justVariable: bool):
        """Determina la distribución de nuevo capital para alcanzar el balance objetivo."""
        # 1. Calcular el nuevo total teórico y los montos objetivos

        if justVariable == True:
            self.target_var_per = 1
        else:
            self.target_var_per = (self.investment_rule - self.investor_age) / 100
        
        total_after = self.curr_variable + self.curr_fixed + self.to_add
    
        obj_var = total_after * self.target_var_per
        obj_fix = total_after * (1 - self.target_var_per)

        # 2. Determinar cuánto falta para llegar al objetivo (Shortfall)
        # Si el resultado es negativo, significa sobreponderación
        need_var = max(0, obj_var - self.curr_variable)
        need_fix = max(0, obj_fix - self.curr_fixed)

        # 3. Ajuste proporcional si el capital no alcanza para cubrir ambos déficits
        # O si el rebalanceo requiere más de lo que vamos a inyectar (sin vender activos)
        total_needed = need_var + need_fix
    
        if total_needed > 0:
            # Escala los montos para que la suma sea exactamente to_add
            to_invest_var = (need_var / total_needed) * self.to_add
            to_invest_fix = (need_fix / total_needed) * self.to_add
        else:
            # Caso borde: El portafolio está perfecto o to_add es 0
            to_invest_var = self.to_add * self.target_var_per
            to_invest_fix = self.to_add * (1 - self.target_var_per)

        return to_invest_var, to_invest_fix

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
        self.message = "No se encontro el Id"
        super().__init__(self.message)

dateError = updateDateError()
zeroValueError = greaterThanZeroError()

