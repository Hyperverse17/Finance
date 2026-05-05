import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter
from datetime import datetime
from finance.core.db import get_connection

def generar_graficas():
    try:
        # 1. Conexión y carga de datos
        conn  = get_connection()
        query = "SELECT * FROM vw_otelo_progress"
        df = pd.read_sql_query(query, conn)
        conn.close()

        # 2. Preparación de datos
        fecha_actual = datetime.now().strftime("%B %Y")
        df['Fecha'] = pd.to_datetime(df['Fecha'])
        df = df.sort_values('Fecha')

        # --- ESTILO ---
        plt.style.use('seaborn-v0_8-darkgrid')
        # Definimos colores específicos
        color_fija = 'tab:cyan'
        color_variable = '#ffca3a'
        color_total = '#8ac926'
        color_emergencias = '#ff595e'

        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 11), sharex=True)
        fig.canvas.manager.set_window_title(f"Progreso del Portafolios de Otelo {fecha_actual}")

        # --- GRÁFICA 1: Inversiones y Total ---
        
        # A. Sombreado estilo "integración matemática" para el Total
        # Usamos un alfa muy bajo (0.1) para que sea un tinte sutil
        ax1.fill_between(df['Fecha'], df['Portafolio_Total'], color=color_total, alpha=0.1, label='Total (Área)')
        
        # B. Línea del Portafolio Total (Púrpura)
        ax1.plot(df['Fecha'], df['Portafolio_Total'], label='Portafolio Total (Línea)', color=color_total, linewidth=3)
        
        # C. Líneas de los componentes
        # Renta Variable (Anaranjado)
        ax1.plot(df['Fecha'], df['Renta_Variable'], label='Renta Variable', marker='s', linewidth=2.5, color=color_variable)
        # Renta Fija (Verde)
        ax1.plot(df['Fecha'], df['Renta_Fija'], label='Renta Fija', marker='^', linewidth=2.5, color=color_fija)

        # Configuración eje superior
        ax1.set_title('Evolución de Inversiones vs Valor Total', fontsize=16, fontweight='bold', color='#333333')
        ax1.set_ylabel('Monto ($)', fontsize=12)
        ax1.legend(loc='upper left', frameon=True, shadow=True)
        # Formatear eje Y con separador de miles
        ax1.yaxis.set_major_formatter(StrMethodFormatter('{x:,.0f}'))

        # --- GRÁFICA 2: Fondo de Emergencias ---
        ax2.plot(df['Fecha'], df['Emergencias'], label='Fondo de Emergencias', marker='o', linewidth=2.5, color=color_emergencias)
        
        # Configuración eje inferior
        ax2.set_title('Detalle: Fondo de Emergencias', fontsize=16, fontweight='bold', color='#333333')
        ax2.set_xlabel('Fecha de Registro', fontsize=12)
        ax2.set_ylabel('Monto ($)', fontsize=12)
        ax2.legend(loc='upper left', frameon=True, shadow=True)
        # Formatear eje Y con separador de miles
        ax2.yaxis.set_major_formatter(StrMethodFormatter('{x:,.0f}'))

        # Ajustes finales de formato y diseño
        plt.xticks(rotation=35, ha='right')
        plt.tight_layout()
        
        print("Graficando el progreso financiero...")
        plt.show()

    except Exception as e:
        print(f"Error al generar la gráfica: {e}")

if __name__ == "__main__":
    generar_graficas()