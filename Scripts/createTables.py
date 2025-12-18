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

# Guardar cambios y cerrar
conn.commit()
conn.close()
