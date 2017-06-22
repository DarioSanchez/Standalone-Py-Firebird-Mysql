@echo off

echo Esperamos unos 10 seg para agregar al inicio de Windows picaso_crm.exe !
timeout /t 10 /nobreak
Copy "C:\user\build\exe.win32-2.7\connect-crm.lnk" "C:\Users\%USERNAME%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\connect-crm.lnk"