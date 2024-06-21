@echo off 
cd C:\Users\%username%\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadLine
xcopy C:\Users\%username%\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt D:\Stuff\Info
pause