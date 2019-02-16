@echo off
cls
echo -V-Plotter------------------------
echo -Mit dem Raspberry verbinden...
echo -Verbindung testen
timeout /T 2
ping /n 1 192.168.178.210
timeout /T 2
cls
echo -Datei "file.svg" wird uebertragen
timeout /T 2
psftp.exe -b plotter_trans_cmd.txt -pw raspberry pi@192.168.178.210
timeout /T 2
cls
echo -Plotter wird gestartet
plink.exe -m plotter_run_cmd.txt -pw raspberry pi@192.168.178.210
echo -Plotter beendet
pause
exit