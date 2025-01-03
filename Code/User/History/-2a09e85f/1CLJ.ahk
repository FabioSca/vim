

; Cerca la parola 2 volte
WinActivate, ahk_exe msedge.exe
Send, {Ctrl down}f{Ctrl up}
Send, Iscrizioni
Send {Enter}
Send, {Ctrl down}f{Ctrl up}
Send, Iscrizioni
Send {Enter}

; Posiziona il mouse 25 pixel sotto per 5 cicli
Loop, 5 {
    MouseMove, 0, 25, 0, R
    Sleep, 500
}
