import sqlite3
from Settings.properties import mainDbName

# Conexión a la base de datos (se crea si no existe)
conn = sqlite3.connect(mainDbName)
cursor = conn.cursor()

# Crear tabla si no existe
cursor.execute("""
CREATE TABLE IF NOT EXISTS investors(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    last_name TEXT,
    birthday DATE,
    investment_rule INTEGER,
    monthly_expenses REAL,
    emergency_fund REAL,
    variable_amt REAL,
    fixed_amt REAL,
    total_portfolio REAL,
    last_update TIMESTAMP DEFAULT (datetime('now','localtime'))
)
""")

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
)
""")

# Guardar cambios y cerrar
conn.commit()
conn.close()

