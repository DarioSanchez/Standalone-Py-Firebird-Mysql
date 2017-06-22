@echo off

echo En 10 segundos el proceso picaso_crm.exe de cerrara!
timeout /t 10 /nobreak
TASKKILL /F /IM connect_crm.exe
