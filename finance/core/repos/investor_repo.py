from finance.models.classes import Investor, User
from finance.core.db import get_connection

def rowToUser(user_row) -> User:
    """Instancia un objeto de User a partir de un select"""
    user = User(id=user_row[0], name=user_row[1], last_name=user_row[2], birthday=user_row[3], gender=user_row[4], email=user_row[5])
    return user

def getUserById(user_id:int) -> User:
    """Hace select a users"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""SELECT id, name, last_name, birthday, gender, email, active FROM users WHERE id = ?""",(user_id,),)
    user_row = cursor.fetchone()
    conn.close()
    if user_row is None:
        return None
    else:
        return rowToUser(user_row)

def rowToInvestor(investor_row) -> Investor:
    """Instancia un objeto de Investor a partir de un select"""
    user_id = investor_row[0]
    user    = getUserById(user_id)
    investor = Investor(user, nickname=investor_row[1], investment_rule=investor_row[2], monthly_expenses=investor_row[3], emergency_fund=investor_row[4], variable_amt=investor_row[5], fixed_amt=investor_row[6])
    return investor

def getInvestorById(investor_id: int) -> Investor | None:
    """Hace select a Investors """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""SELECT user_id, nickname, investment_rule, monthly_expenses, emergency_fund, variable_amt, fixed_amt FROM investors WHERE id = ?""",(investor_id,),)
    investor_row = cursor.fetchone()
    conn.close()

    if investor_row is None:
        return None
    else:
        return rowToInvestor(investor_row)
    