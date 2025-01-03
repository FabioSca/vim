@echo off
set pyUICCommand="pyuic5"
set fname=%1

SET SUBDIR=%~dp0
ECHO %SUBDIR%

set NUMEXPR_MAX_THREADS=8
set pythonpath=C:\DE-Python\envs\LEO4\Scripts\python.exe

rem set PYTHONHOME=C:\Anaconda3


rem set PATH=%PYTHONHOME%;%PYTHONHOME%\DLLs;%PYTHONHOME%\Library\bin;%PYTHONHOME%\Scripts;%PYTHONHOME%\Lib\site-packages

echo Convert txt to py
echo %pythonpath% %SUBDIR%\fromuitopy2.py %fname%
call %pythonpath% "%SUBDIR%\fromuitopy2.py" %fname%

dir

pause