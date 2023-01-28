
echo Running Nastran 2014.1
echo %0 %1 %2 %3
rem E:
cd /d %3
call D:\MSC.Software\MSC_Nastran\20141\bin\nast20141.exe %1 PWD=%3

dir
pause