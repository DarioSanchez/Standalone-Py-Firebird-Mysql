@echo off

echo Esperamos unos 10 seg para iniciar picaso_crm.exe en segundo plano
timeout /t 10 /nobreak
FOR %%X IN ("C:\user\build\exe.win32-2.7\connect-crm.exe") DO rundll32 shell32.dll,ShellExec_RunDLL %%X