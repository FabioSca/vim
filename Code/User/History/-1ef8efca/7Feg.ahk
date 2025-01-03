#Requires AutoHotkey v2.0
#SingleInstance force

; Make it hit Ctrl 
; +#f23::Ctrl
; RCtrl::Ctrl
<+<#f23::Send "{Blind}{LShift Up}{LWin Up}{RControl Down}"
<+<#f23 Up::Send "{RControl Up}"