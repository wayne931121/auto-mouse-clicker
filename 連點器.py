import time
#https://stackoverflow.com/questions/1181464/controlling-mouse-with-python
#https://stackoverflow.com/questions/11918999/key-listeners-in-python
#https://stackoverflow.com/questions/61295239/how-to-listen-letter-keys-with-combination-of-modifier-keys-using-pynput
import pyautogui, threading, sys
from pynput import keyboard

def on_press(key):
    if key == keyboard.Key.esc:
        return False  # stop listener
    # try:
        # k = key.char  # single-char keys
    # except:
        # k = key.name  # other keys
    k = str(listener.canonical(key))
    #print(k)
    return keys.store(k)

class keyStore():
    def __init__(self):
        self.keys = ["NAN" for i in range(3)]
        self.isDetect = False
    def store(self, key):
        if key==self.keys[-1]:
            return True
        #print(self.keys)
        self.keys.pop(0)
        self.keys.append(key)
        return self.detects()
    def detects(self):
        funs = [(["Key.ctrl", "'k'"], self.stopProcess),
                (["Key.ctrl", "'c'"], self.stopClick),
                (["Key.ctrl", "'j'"], self.startClick),
                (["Key.ctrl", "'d'"], self.startDetect),]
        result = True
        for i in funs:
            #print(i)
            result *= self.detect(*i)
        result = True if result==1 else False #決定是否繼續執行監聽
        return result
    def detect(self, confirm, function): #detect HotKey
        #keys = self.keys
        #for i in confirm:
        #    if not i in self.keys: #若所指定的按鍵全在裡面則繼續執行function，否則忽略並返回True。
        #        return True
        if not confirm==self.keys[1:]:
            return True
        return function()
    def stopProcess(self):
        global loop
        loop = 0
        root.destroy()
        return False #最終返回False則停止鍵盤監聽，否則繼續監聽。
    def stopClick(self):
        global loop
        loop = 0
        return True
    def startClick(self):
        try:
            x, y = [int(i) for i in position.get().split(",")]
        except:
            tk.messagebox.showerror("錯誤", "位置格式為: x,y")
            return True
        try:
            max_thread = int(layout_maxThread.text.get())
        except:
            tk.messagebox.showerror("錯誤", "併發進程數格式為數字")
            return True
        try:
            rest_time = float(layout_restTime.text.get())
        except:
            tk.messagebox.showerror("錯誤", "休息時間格式為數字")
            return True
        global ClickPosition
        ClickPosition = (x,y)
        pyautogui.PAUSE = rest_time
        for e in range(max_thread):
            process = threading.Thread(target=click)
            process.start()
        return True
    def startDetect(self):
        detect_mouse_position()
        return True

class DetectMousePosition():
    def __init__(self):
        self.isDetect = False
    def __call__(self):
        if self.isDetect:
            self.isDetect = False
        else:
            self.isDetect = True
            process = threading.Thread(target=self.run)
            process.start()
    def run(self):
        while self.isDetect:
            time.sleep(0.01)
            ClickPosition = pyautogui.position()
            position.set(str(ClickPosition[0])+","+str(ClickPosition[1]))

keys = keyStore()
detect_mouse_position = DetectMousePosition()
def startListener():
    listener = keyboard.Listener(on_press=on_press)
    listener.start()  # start to listen on a separate thread
    try:
        listener.join()  # remove if main thread is polling self.keys
    except KeyboardInterrupt:
        pass
listener = keyboard.Listener(on_press=on_press)
listener.start()  # start to listen on a separate thread
loop = 1
#https://stackoverflow.com/questions/35805649/how-to-increase-number-of-clicks-per-second-with-pyautogui
#pyautogui.PAUSE = 0.01

def click():
    global loop
    loop = 1
    while loop:
        try:
            pyautogui.click(*ClickPosition)
        except:
            break
        time.sleep(0.01)
# try:
    # listener.join()
# except KeyboardInterrupt:
    # pass
import tkinter as tk
from tkinter import messagebox

class layout_style1(tk.Frame):
    def __init__(self, master, label_text, input_text):
        super().__init__(master)
        self.text = tk.StringVar()
        self.text.set(input_text)
        self.inputext = tk.Label(self, text=label_text)
        self.inputBox = tk.Entry(self, textvariable=self.text)
        self.pack()
        self.inputext.pack(side="left")
        self.inputBox.pack(side="left")
        return None

root = tk.Tk()
root.title("連續點擊器")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width, height = 300, 270
root.geometry('%dx%d+%d+%d'%(width, height, (screen_width-width)/2,(screen_height-height)/2))


ClickPosition = (screen_width/2, screen_height/2)
layout_position = layout_style1(root, "位置:", "%d,%d"%(screen_width/2,screen_height/2))
layout_maxThread = layout_style1(root, "併發進程數:", "1")
layout_restTime = layout_style1(root, "休息時間:", "0.1")
position = layout_position.text
intro = ""+ \
"按下Ctrl+J開始，\nCtrl+C取消，\nCtrl+K結束程序。\n\n"+ \
"""
按下Ctrl+D開始偵測滑鼠位置，並且再按一次停止偵測。注意，您不能按住Ctrl按J並繼續按C，
這不會使您開始並結束連點器，您必須按完Ctrl+J後重新按一次Ctrl+C。若按Ctrl+J會觸發其他
功能，您可以不必壓住Ctrl再按J，可以按Ctrl放開後再按J。休息時間是指連點器程式點擊休
息時間，實際最短時間取決於電腦CPU配置。最大併發進程數建議最多32以內，實際效能取決於CPU。""".replace("\n","")
introduce = tk.Label(root, text=intro,wraplength=270)
introduce.pack()

root.mainloop()