
#!/usr/bin/env python3
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def clear_screen():
    os.system("clear" if os.name != "nt" else "cls")

def main():
    clear_screen()
    print("\n" + "=" * 50)
    print("      Finanzas Personales - Menu Principal")
    print("=" * 50)
    print("\n  Opciones disponibles:\n")
    print("  1. Balance del dia (todaysBalance)")
    print("  2. Inversiones (toInvest)")
    print("  3. Graficar Progreso")
    print("  4. Graicar Distribucion")
    print("  0. Salir")
    print("\n" + "=" * 50)
    
    try:
        choice = input("\n  Selecciona una opcion: ").strip()
        
        if choice == "1":
            print("\n  Ejecutando Balance del dia...")
            time.sleep(1)
            clear_screen()
            exec(open("scripts/todaysBalance.py").read())

        elif choice == "2":
            print("\n  Ejecutando Inversiones...")
            time.sleep(1)
            clear_screen()
            exec(open("scripts/toInvest.py").read())

        elif choice == "3":
            print("\n  Graficando Progreso...")
            exec(open("scripts/plot_progress.py", encoding="utf-8").read())
            input("\n  Presiona Enter para continuar...")
            main()

        elif choice == "4":
            print("\n  Graficando Distribucion...")
            exec(open("scripts/plot_distribution.py", encoding="utf-8").read())
            input("\n  Presiona Enter para continuar...")
            main()

        elif choice == "0":
            print("\n  Hasta luego!\n")
            time.sleep(2)
            sys.exit(0)
        else:
            print("\n  Opcion no valida")
            input("\n  Presiona Enter para continuar...")
            main()
    except KeyboardInterrupt:
        print("\n\n  Programa interrumpido")
        sys.exit(0)
    except Exception as e:
        print(f"\n  Error: {e}")
        input("\n  Presiona Enter para continuar...")
        main()

if __name__ == "__main__":
    main()
