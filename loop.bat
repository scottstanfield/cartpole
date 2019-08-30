
echo %1 
:loop
python sim.py --brain %1
goto loop