# auto-mouse-clicker
auto mouse clicker (python3.9)
連點器，自動滑鼠點擊器。

```
按下Ctrl+D開始偵測滑鼠位置，並且再按一次停止偵測。注意，您不能按住Ctrl按J並繼續按C，這不會使您開始並結束連點器，您必須按完Ctrl+J後重新按一次Ctrl+C。若按Ctrl+J會觸發其他功能，您可以不必壓住Ctrl再按J，可以按Ctrl放開後再按J。休息時間是指連點器程式點擊休息時間，實際最短時間取決於電腦CPU配置。最大併發進程數建議最多32以內，實際效能取決於CPU。
```

```
[Translate]
Press Ctrl+D to start detecting the mouse position, and press again to stop detecting. Note that you cannot hold Ctrl and press J and continue to press C, this will not start and end the clicker, you have to press Ctrl+C again after pressing Ctrl+J. If pressing Ctrl+J will trigger other functions, you don’t need to hold Ctrl and then press J, you can press Ctrl and release it and then press J. The rest time refers to the rest time of the clicker program per click, and the actual shortest time depends on the computer CPU configuration. The maximum number of concurrent threading processes is recommended to be within 32, and the actual performance depends on the CPU.
```

```
預設介面:位置-滑鼠點擊位置(x,y)、併發進程數-開幾個子進程增加點擊次數(1)、休息時間-每次點擊後程式延遲時間(0.1)
Default GUI: Position-Mouse Position(x,y), Max Threading(1), Rest Time-Rest Time after per clicking(0.1)
```
