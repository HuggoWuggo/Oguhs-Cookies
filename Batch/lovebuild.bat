@echo off

mkdir build

tar -a -c -f game.zip *

copy game.zip build

del game.zip

cd build

copy /b "C:\Program Files\LOVE\love.exe"+game.zip game.exe

del game.zip

copy "C:\Program Files\LOVE\*.dll" 