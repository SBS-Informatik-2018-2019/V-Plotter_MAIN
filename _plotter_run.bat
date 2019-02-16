@echo off
title V-Plotter
cls
echo -V-Plotter------------------------
echo -Mit dem Raspberry verbinden...
title V-Plotter -Verbindung testen
ping 192.168.178.210
timeout /T 3
cls
echo -Datei "file.svg" wird uebertragen
psftp.exe -b plotter_trans_cmd.txt -pw raspberry pi@192.168.178.210
title V-Plotter -gestarted
START putty.exe -ssh pi@192.168.178.210 -pw raspberry
timeout /T 20
cls
title V-Plotter -cleanup
timeout /T 3
exit
