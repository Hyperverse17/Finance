from datetime import datetime, date
from data.databases.distributions import *
from finance.core.properties import today
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
    def _get_fixed_variable(self):
        """Determina la distribución de nuevo capital para alcanzar el balance objetivo."""
        self.curr_portfolio_value = self.curr_variable + self.curr_fixed
        # 1. Calcular el nuevo total teórico y los montos objetivos
        if self.just_variable == True:
            self.target_var_per = 1
            self.target_fix_per = 0
        else:
            self.target_var_per = (self.investment_rule - self.investor_age) / 100
            self.target_fix_per = (1 - self.target_var_per)
        
        self.new_portfolio_value = self.curr_variable + self.curr_fixed + self.total_add
    
        var_target = self.new_portfolio_value * self.target_var_per
        fix_target = self.new_portfolio_value * self.target_fix_per

        # 2. Determinar cuánto falta para llegar al objetivo (Shortfall)
        # Si el resultado es negativo, significa sobreponderación
        need_var = max(0, var_target - self.curr_variable)
        need_fix = max(0, fix_target - self.curr_fixed)

        # 3. Ajuste proporcional si el capital no alcanza para cubrir ambos déficits
        # O si el rebalanceo requiere más de lo que vamos a inyectar (sin vender activos)
        total_needed = need_var + need_fix
    
        if total_needed > 0:
            # Escala los montos para que la suma sea exactamente to_add
            self.variable_add = (need_var / total_needed) * self.total_add
            self.fixed_add = (need_fix / total_needed) * self.total_add
        else:
            # Caso borde: El portafolio está perfecto o to_add es 0
            self.variable_add = self.total_add * self.target_var_per
            self.fixed_add = self.total_add * self.target_fix_per

        self.new_variable = self.curr_variable + self.variable_add
        self.new_fixed = self.curr_fixed + self.fixed_add
    
    def __init__(self, investor_age:int, investment_rule:int, curr_variable:float, curr_fixed:float, to_add:float, justvariable: bool) -> None:
        self.investment_rule = investment_rule
        self.investor_age = investor_age 
        self.curr_variable = curr_variable
        self.curr_fixed = curr_fixed
        self.total_add = to_add
        self.just_variable = justvariable
        self._get_fixed_variable()
        self.curr_variable_perc = round(self.curr_variable/self.curr_portfolio_value,2) if self.curr_portfolio_value > 0 else 0    
        self.curr_fixed_perc = round(self.curr_fixed/self.curr_portfolio_value,2) if self.curr_portfolio_value > 0 else 0
        self.new_variable_perc = round(self.new_variable/self.new_portfolio_value,2)
        self.new_fixed_perc = round(self.new_fixed/self.new_portfolio_value,2)
        
    def __str__(self) -> str:
        return f"Inversion en renta fija y renta variable para una persona de {self.investor_age} años usando la regla del {self.investment_rule} %."
    
class Budget():
    def _calculate_days(self):
        self.elapsed = self.today - self.payment_day
        self.all = self.next_payment_day - self.payment_day
        self.remaining = self.all - self.elapsed
        current = self.today - self.payment_day
        self.current_day = current.days + 1

        if self.all.days == 0:
            raise ValueError("Ajustar Fechas de Pago y Proximo Pago")

        if self.elapsed.days > self.all.days:
            raise ValueError("Actualizar Fechas de Pago y Proximo Pago")

    def _calculate_budget(self):
        self.daily_budget = round(self.total_budget/self.all.days,2)
        self.should_amount = round((self.daily_budget*(self.all.days - self.elapsed.days)),2)

    def __init__(self, total_budget:float, payment_day:date, next_payment_day:date):
        if total_budget > 0:
            self.total_budget = total_budget
        else:
            raise ValueError("El presupuesto debe ser positivo")
        
        self.today = today
        self.payment_day = payment_day
        self.next_payment_day = next_payment_day
        self._calculate_days()
        self._calculate_budget()

    def status(self, current:float) -> str:
        """Indica el estatus del dia"""
        if self.remaining.days == 1:
            message = f"Dia final, hoy puedes gastar todo."

        else:
            self.difference = current - self.should_amount
            self.total_for_today = self.daily_budget + self.difference
        
            if self.difference >= 0:
                if self.difference > 0:
                    message = f"Hoy puedes gastar tus ${self.daily_budget:,.2f} mas ${self.difference:,.2f} (${self.total_for_today:,.2f} en total)."

                if self.difference == 0:
                    message = f"Hoy solo puedes gastar tus ${self.daily_budget:,.2f} diarios."

            else:
                if self.total_for_today > 0 and self.total_for_today < self.daily_budget:
                    message = f"Hoy solo tienes ${self.total_for_today:,.2f}."

                elif self.total_for_today <= 0:
                    message = "Mejor no gastes hoy."

            return message

    def __str__(self) -> str:
        return f"Distribucion de ${self.total_budget:,.2f} durante {self.all.days} dias."

    
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

