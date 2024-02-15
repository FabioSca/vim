
echo Running Nastran 
echo %0 
echo %1 
echo %2 


@echo off

REM Identify and run latest installed Nastran Version
for /f skip^=2^ tokens^=3^  %%a in ('reg query "HKLM\SOFTWARE\WOW6432Node\Hexagon Manufacturing Intelligence, Inc.\MSC Nastran\Latest"') do set MSC_VER=%%a
echo MSC_VER: %MSC_VER%

for /f skip^=2^ tokens^=3^  %%a in ('reg query "HKLM\SOFTWARE\WOW6432Node\Hexagon Manufacturing Intelligence, Inc.\MSC Nastran\%MSC_VER%" /v "path"') do set MSC_BASE=%%a
echo MSC_BASE: %MSC_BASE%
echo.



cd /d %2
call %MSC_BASE%\bin\nastran.exe %1 
rem PWD=%2

rem pause



@echo off
setlocal

echo.
echo OUTPUT FILES :
echo.
dir %~n1.*

pause


rem :PROMPT
rem echo.
rem echo.
rem SET /P AREYOUSURE=DO YOU WANT TO RUN F06 Reader (y/[n])?
rem IF /I "%AREYOUSURE%" NEQ "y" GOTO END
rem 
rem echo.
rem echo ... Reading file %~n1.f06
rem D:\MSC.Software\MSC_Nastran\2019fp1\msc20191\win64i8\F06Reader.exe -b -F06File %~n1.f06
rem 
rem :END
rem endlocal
rem 

exit
