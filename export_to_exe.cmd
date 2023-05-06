chcp 65001 > NUL
call conda create --name ttt python=3.9
call conda activate ttt
pip install pyautogui
pip install pyinstaller
pip install pynput
rem pyinstaller -w -i your.ico -F 連點器.py
pyinstaller -w -F 連點器.py
call conda deactivate
call conda remove -n ttt --all
pause
