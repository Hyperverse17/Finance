from finance.core.db import get_connection
# Conexión a la base de datos (se crea si no existe)
conn   = get_connection()
cursor = conn.cursor()

# Crear tabla si no existe
cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    last_name TEXT,
    birthday DATE,
    gender TEXT CHECK(gender IN ('Female', 'Male')),
    email TEXT UNIQUE,
    active BOOL,
    last_update TIMESTAMP DEFAULT (datetime('now','localtime'))
    )""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS investors(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER UNIQUE,
    nickname TEXT UNIQUE,
    investment_rule INTEGER DEFAULT 100,
    monthly_expenses REAL DEFAULT 10000,
    emergency_fund REAL,
    variable_amt REAL,
    fixed_amt REAL,
    total_portfolio REAL,
    last_update TIMESTAMP DEFAULT (datetime('now','localtime')),
    FOREIGN KEY (user_id) REFERENCES users(id)
)""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS investments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    investor INTEGER NOT NULL,
    age INTEGER,
    rule INTEGER,
    monthly_expenses REAL,
    current_emergency REAL,
    moe_equivalence REAL,
    current_variable REAL,
    current_fixed REAL,
    total_add REAL,
    emergency_add REAL,
    investments_add REAL,           
    variable_add REAL,
    fixed_add REAL,
    emergency_percentage REAL,
    investments_percentage REAL,
    variable_percentage REAL,
    fixed_perentage REAL,
    comments TEXT,
    date DATE DEFAULT (date('now','localtime')),
    last_update TIMESTAMP DEFAULT (datetime('now','localtime')),
    FOREIGN KEY (investor) REFERENCES users(id)
)""")

cursor.execute("""CREATE TABLE IF NOT EXISTS portfolios(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    investment_id integer,
    date DATE DEFAULT (date('now','localtime')),
    emergency_fund REAL,
    variable_amt REAL,
    fixed_amt REAL,
    total_portfolio REAL,
    plot BOOLEAN DEFAULT 1,
    last_update TIMESTAMP DEFAULT (datetime('now','localtime')),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (investment_id) REFERENCES investments(id)
)""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS parameters(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id integer,
    payment_day DATE,
    next_payment_day DATE,
    free_spending REAL,
    last_update TIMESTAMP DEFAULT (datetime('now','localtime')),
    FOREIGN KEY (user_id) REFERENCES investors(id)
)
""")

cursor.execute("""CREATE VIEW IF NOT EXISTS vw_otelo_portfolio AS
        SELECT 
        id,
        investment_id AS Referencia,
        printf('$%,.2f', emergency_fund) AS Emergencias, 
        printf('$%,.2f', variable_amt) AS Renta_Variable, 
        printf('$%,.2f', fixed_amt) AS Renta_Fija, 
        printf('$%,.2f', total_portfolio) AS Portafolio_Total, 
        date 
        FROM portfolios
        WHERE user_id = 1
        ORDER BY date""")
        
cursor.execute("""CREATE VIEW IF NOT EXISTS vw_otelo_progress AS
        SELECT 
        id,
        investment_id AS Referencia,
        emergency_fund AS Emergencias, 
        variable_amt AS Renta_Variable, 
        fixed_amt AS Renta_Fija, 
        total_portfolio AS Portafolio_Total, 
        date 
        FROM portfolios
        WHERE (user_id = 1 AND plot = 1)
        ORDER BY date""")

# Guardar cambios y cerrar
conn.commit()
conn.close()
