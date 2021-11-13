
echo Running Nastran 2021.3
echo %0 
echo %1 
echo %2 

cd /d %2
call D:\MSC.Software\MSC_Nastran\2021.3\bin\nastran %1 
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
