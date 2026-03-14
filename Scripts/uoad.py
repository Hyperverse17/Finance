import time
try:
    from finance.core.db import get_connection

    conn   = get_connection()
    cursor = conn.cursor()

    command = """DELETE FROM portfolios"""
    print(command)
    cursor.execute(command)
    conn.commit()

    command = """UPDATE sqlite_sequence SET seq = 0 WHERE name = 'portfolios'"""
    print(command)
    cursor.execute(command)
    conn.commit()

    command = """SELECT id, investor, current_emergency, emergency_add, current_variable, variable_add, current_fixed, fixed_add, last_update FROM investments ORDER BY last_update""" 
    print(command)
    cursor.execute(command)

    investments = cursor.fetchall()

    print("Actualizando portfolios...")
    for investment in investments:
        values = []

        values.append(investment[1])
        values.append(investment[0])
        
        values.append(round(investment[2] + investment[3],2))
        values.append(round(investment[4] + investment[5],2))
        values.append(round(investment[6] + investment[7],2))
        values.append(round(investment[4] + investment[5] + investment[6] + investment[7],2))
        values.append(investment[8])

        values = tuple(values)
        
        command2 = """INSERT INTO portfolios (user_id, investment_id, emergency_fund, variable_amt, fixed_amt, total_portfolio, last_update) VALUES (?,?,?,?,?,?,?)"""
        cursor.execute(command2,values)
        conn.commit()

    conn.close()

except:
    pass


finally:
    time.sleep(3)


