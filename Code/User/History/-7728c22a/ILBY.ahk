#Requires AutoHotkey v2.0

;testo := WinGetTitle("ahk_exe msedge.exe")
;MsgBox "ciao", testo

; Controlla il titolo della finestra per confermare che siamo su YouTube


; Cerca la parola 2 volte
WinActivate("ahk_exe msedge.exe")

; Send("{Ctrl down}f{Ctrl up}")
; Sleep(200)
; Send("Iscrizioni")
; Sleep(200)
; Send("{Enter}")
; Sleep(200)
; Send("{Enter}")
;Send("{Esc}")

KeyWait "LButton", "D"

Sleep(300)

; Calcola le coordinate
    CoordMode("Mouse", "Screen")
    ; MouseMove GetCaretPos()[1], GetCaretPos()[2]
    ; Usa l'API per ottenere la posizione del cursore
    MouseGetPos(&X, &Y)

; Posiziona il mouse 25 pixel sotto per 5 cicli
Loop 7 {
    MouseMove(0, 45, 1, "R")
    Click()
    Sleep(300)
}