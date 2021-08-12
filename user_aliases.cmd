;= @echo off
;= rem Call DOSKEY and use this file as the macrofile
;= %SystemRoot%\system32\doskey /listsize=1000 /macrofile=%0%
;= rem In batch mode, jump to the end of the file
;= goto:eof
;= Add aliases below here
e.=explorer .
gl=git log --oneline --all --graph --decorate  $*
;= ls=ls --show-control-chars -F --color $*
;= ll=ls -lat --show-control-chars -F --color $*
ll=ls -lat
pwd=cd
clear=cls
unalias=alias /d $1
vi=vim $*
cmderr=cd /d "%CMDER_ROOT%"
unalias=alias /d $1
w=where $1
note="C:\Program Files\Notepad++\notepad++.exe" $*
note++="C:\Program Files\Notepad++\notepad++.exe" $*
npp="C:\Program Files\Notepad++\notepad++.exe" $*
run_marc_2020.1="C:\MSC.Software\Marc\2020.1.0\marc2020.1\tools\run_marc" $*
;= run_marc_2018="C:\MSC.Software\Marc\2018.0.0\marc2018\tools\run_marc" $*
;= run_marc_2017.1="C:\MSC.Software\Marc\2017.1.0\marc2017\tools\run_marc" $*
;= run_marc_2016="C:\MSC.Software\Marc\2016.0.0\marc2016\tools\run_marc" $*
;= run_nastran_20161="D:\MSC.Software\MSC_Nastran\20161\bin\nast20161" $*
;= mentat_2016=start "" "C:\MSC.Software\Marc\2016.0.0\mentat2016\bin\mentat.bat"
;= mentat_2017.1=start "" "C:\MSC.Software\Marc\2017.1.0\mentat2017\bin\mentat.bat"
;= mentat_2018=start "" "C:\MSC.Software\Marc\2018.0.0\mentat2018\bin\mentat.bat"
mentat_2021.2=start "" "C:\MSC.Software\Marc\2021.2.0\mentat2021.2\bin\mentat.bat"
eclipse="C:\PROGRAMMI\SVILUPPO\eclipse\eclipse.exe"
visual_studio="D:\Program Files (x86)\Microsoft Visual Studio 12.0\Common7\IDE\devenv.exe"
fortran_config2017="C:\Program Files (x86)\IntelSWTools\compilers_and_libraries_2019.4.245\windows\bin\ipsxe-comp-vars.bat" intel64 vs2017
fortran_local="D:\PROGRAMMI\cmder\vendor\fortran_local.bat"
fortran_server="D:\PROGRAMMI\cmder\vendor\fortran_server.bat"
;= vim="c:\Program Files (x86)\Vim\vim82\vim.exe"
vifm="D:\PROGRAMMI\cmder\vendor\vifm\vifm.exe"
far=D:\PROGRAMMI\cmder\vendor\farmanager\far

goto_cmder=cd /d "%CMDER_ROOT%"
goto_vimmain=cd /d C:\Users\e3018\vim_main
goto_projects=cd /d C:\Projects
goto_work=cd /d D:\WORK
goto_scoop=cd /d D:\PROGRAMMI\scoop\apps

top="D:\PROGRAMMI\cmder\vendor\top.bat"

