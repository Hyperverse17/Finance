@echo off
cd /d "C:\Users\jovan\Documents\Coding\PythonTools\FinancePro\data\databases"
sqlite3 MyFinances.db -init init.sql
