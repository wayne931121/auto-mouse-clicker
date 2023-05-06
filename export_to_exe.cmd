chcp 65001 > NUL
call conda create --name ttt python=3.9
call conda activate ttt
pip install pyautogui
pip install pyinstaller
pip install pynput
pyinstaller -w -i 73af0910-0854-4082-b143-cb7a2a595eb2-1.ico -F 連點器.py
call conda deactivate
call conda remove -n ttt --all
pause