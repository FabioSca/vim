#Requires AutoHotkey v2.0

testo = WinGetTitle("ahk_exe msedge.exe")
MsgBox &testo]

; Controlla il titolo della finestra per confermare che siamo su YouTube
If (InStr(WinGetTitle("ahk_exe msedge.exe"), "YouTube"))
{

    ; Cerca la parola 2 volte
    WinActivate("ahk_exe msedge.exe")
    Send("{Ctrl down}f{Ctrl up}")
    Send("Iscrizioni")
    Send("{Enter}")
    Send("{Ctrl down}f{Ctrl up}")
    Send("Iscrizioni")
    Send("{Enter}")

    Sleep(2000)

    ; Calcola le coordinate
        CoordMode("Mouse", "Screen")
        ; Usa l'API per ottenere la posizione del cursore
        MouseGetPos(&X, &Y)

    ; Posiziona il mouse 25 pixel sotto per 5 cicli
    Loop 5 {
        MouseMove(0, 30, 1, "R")
        Click()
        Sleep(500)
    }
}
Else 
{
    MsgBox "non sei su youtube"
}