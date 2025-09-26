@echo off
REM Cambia al directorio donde está este .bat
cd /d "%~dp0"

REM Ejecuta el script con el Python correcto
"C:\Users\jovan\AppData\Local\Programs\Python\Python312\python.exe" "%~dp0toInvest.py"

REM Mantiene la ventana abierta al final
pause
