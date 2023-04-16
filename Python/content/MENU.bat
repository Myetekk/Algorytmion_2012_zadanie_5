@echo off
@chcp 1250
:menu
cls

echo MENU
echo 1 - Uruchom program
echo  2 - Backup
echo 3 - Informacje o projekcie
echo  4 - Wyjscie
echo:
set /p choice="Twój wybór: "


if %choice%==1 (
 goto 1
)
if %choice%==2 (
 goto 2
)
if %choice%==3 (
 goto 3
)
if %choice%==4 (
 goto 4
)


:1
cls
"D:\Python\python.exe" "D:\Projekt_JS\content\main.py"
"D:\Python\python.exe" "D:\Projekt_JS\content\raport.py"
pause
goto menu


:2
cls
for /f %%a in ('powershell -Command "Get-Date -format yyyy_MM_dd__HH_mm_ss"') do set datetime=%%a
cd backups
mkdir "%datetime%"
cd %datetime%
mkdir output
cd ../
cd ../
xcopy /s output backups\"%datetime%"\output
xcopy raport.html backups\"%datetime%"
echo Backup wykonany pomyœlnie
pause
goto menu


:3
cls
informacje.bat
pause
goto menu


:4
cls
