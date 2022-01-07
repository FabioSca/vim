Set-PSReadLineOption -PredictionSource History
oh-my-posh --init --shell pwsh --config "~/.mytheme.omp.json" | Invoke-Expression
oh-my-posh --init --shell pwsh --config ~/jandedobbeleer.omp.json | Invoke-Expression

#Set-Alias -Name ls -Value "wsl ls --color=auto -X"
function ls_alias { wsl ls --color=auto -hF $args }
Set-Alias -Name ls -Value ls_alias -Option AllScope

Set-Alias -Name np -Value C:\Windows\notepad.exe
Set-Alias -Name note++ -Value "C:\Program Files\Notepad++\notepad++.exe" 

# run_marc_2021.3="C:\MSC.Software\Marc\2021.3.1\marc2021.3.1\tools\run_marc" $*
# mentat_2021.3=start "" "C:\MSC.Software\Marc\2021.3.1\mentat2021.3.1\bin\mentat.bat"
# fortran_config2017="C:\Program Files (x86)\IntelSWTools\compilers_and_libraries_2019.4.245\windows\bin\ipsxe-comp-vars.bat" intel64 vs2017
# fortran_local="D:\PROGRAMMI\cmder\vendor\fortran_local.bat"
# fortran_server="D:\PROGRAMMI\cmder\vendor\fortran_server.bat"
