import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import os
from datetime import datetime

# Configurar rutas relativas
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, '..', 'data', 'databases', 'MyFinances.db')
# Crear carpeta de reportes si no existe
REPORTS_DIR = os.path.join(BASE_DIR, '..', 'reports')
os.makedirs(REPORTS_DIR, exist_ok=True)

def graficar_distribucion():
    try:
        conn = sqlite3.connect(DB_PATH)
        query = "SELECT Renta_Variable, Renta_Fija, Fecha FROM vw_otelo_progress ORDER BY Fecha DESC LIMIT 1"
        df = pd.read_sql_query(query, conn)
        conn.close()

        if df.empty: return

        # Datos
        var_amt = df['Renta_Variable'].iloc[0]
        fija_amt = df['Renta_Fija'].iloc[0]
        total_inv = var_amt + fija_amt
        fecha_actual = datetime.now().strftime("%B %Y")
        
        valores = [var_amt, fija_amt]
        etiquetas = ['Renta Variable', 'Renta Fija']
        # Inversión de colores solicitada: Variable (tab:orange), Fija (tab:cyan)
        colores = ['tab:orange', 'tab:cyan'] 

        # --- ESTILO ---
        plt.style.use('seaborn-v0_8-whitegrid')
        fig, ax = plt.subplots(figsize=(9, 9))
        fig.canvas.manager.set_window_title(f"Portafolios de Otelo {fecha_actual}")

        # Dona
        wedges, texts, autotexts = ax.pie(
            valores, labels=etiquetas, autopct='%1.2f%%', 
            startangle=140, colors=colores, pctdistance=0.85,
            explode=(0.05, 0), textprops={'fontsize': 12, 'fontweight': 'bold'}
        )

        # Círculo central (Dona)
        centre_circle = plt.Circle((0,0), 0.70, fc='white')
        fig.gca().add_artist(centre_circle)

        # Texto Central: Total y Desglose
        texto_central = (
            f"Total Invertido\n"
            f"${total_inv:,.2f}\n\n"
            f"Variable: ${var_amt:,.2f}\n"
            f"Fija: ${fija_amt:,.2f}"
        )
        ax.text(0, 0, texto_central, ha='center', va='center', 
                fontsize=11, fontweight='bold', color='#2c3e50')

        # Título y Pie de página
        ax.set_title('Distribución Actual del Portafolio', fontsize=18, fontweight='bold', pad=25)
        
        
        plt.annotate(f'{fecha_actual}', xy=(0.5, 0.02), 
                     xycoords='figure fraction', ha='center', fontsize=10, color='gray')

        ax.axis('equal')
        
        # --- GUARDAR IMAGEN ---
        nombre_archivo = f"distribucion_{datetime.now().strftime('%Y_%m')}.png"
        ruta_guardado = os.path.join(REPORTS_DIR, nombre_archivo)
        plt.savefig(ruta_guardado, dpi=300, bbox_inches='tight')
        
        print(f"Reporte guardado en: {ruta_guardado}")
        plt.show()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    graficar_distribucion()