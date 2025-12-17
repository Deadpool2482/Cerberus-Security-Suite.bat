@echo off
title Cerberus Security Suite v2.0 Launcher
color 0A
echo.
echo    [ AVVIO DI CERBERUS v2.0 ]
echo    Verifica installazione Python...
echo.

:: Controlla se Python è installato
python --version >nul 2>&1
if %errorlevel% neq 0 (
    color 0C
    echo [ERRORE] Python non e' stato trovato!
    echo Per favore installa Python da python.org per usare la v2.0.
    pause
    exit
)

:: Avvia lo script Python
python main.py

pause