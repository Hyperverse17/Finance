import sqlite3
import sys
import time
from pathlib import Path
import git

# ---------- RUTAS BASE ----------
BASE_DIR = Path(__file__).resolve().parents[2]   # FinancePro/
DB_DIR   = BASE_DIR / "data" / "databases"

# ---------- DETECTAR RAMA GIT ----------
def get_current_branch():
    try:
        repo = git.Repo(BASE_DIR, search_parent_directories=True)
        return repo.active_branch.name
    except Exception:
        return "unknown"

# ---------- SELECCIONAR DB ----------
def get_db_path():
    branch = get_current_branch()
    if branch == "main":
        return DB_DIR / "MyFinances.db"

    db_path = DB_DIR / "Tests.db"
    print(f"\n⚠️ Estás en branch '{branch}', se usará la base de datos: {db_path.name}")
    answer = input("¿Deseas continuar? (y/n): ").strip().upper()
    if answer not in ("Y", "YES"):
        print("Ejecución detenida por el usuario...\n")
        time.sleep(1)
        sys.exit(0)

    return db_path

# ---------- CONEXIÓN CENTRAL ----------
def get_connection():
    db_path = get_db_path()
    return sqlite3.connect(db_path)
