#!/usr/bin/env python
import time, pyautogui, threading
import PySimpleGUI as sg
import platform
from enum import Enum

class WakeUpEvent(Enum):
    DISABLED = 0
    MOUSE = 1
    VOLUME = 2

wakeupEvent = WakeUpEvent.DISABLED
wakeupThread = None
runningThread = False

def useVolume(keyPress):
    if keyPress:
        pyautogui.press(keyPress)
    if keyPress and keyPress == 'volumedown':
        return 'volumeup'
    else: 
        return 'volumedown'

def useMouse(mv):
    if mv:
        pyautogui.move(mv,0)
    if mv and mv > 0:
        return -25
    else:
        return 25

def dontsleep(evt, timeout):
    global runningThread
    state = None
    prevState = None
    runningThread = True
    t = time.time()
    while runningThread:
        nt = time.time()
        if nt-t > timeout or not prevState:
            prevState = state
            if evt == WakeUpEvent.MOUSE:
                state = useMouse(state)
            elif evt == WakeUpEvent.VOLUME:
                state = useVolume(state)
            t = nt
        time.sleep(0.5)

def stopThread(wakeupThread):
    global runningThread
    if wakeupThread:
        while(wakeupThread.is_alive()):
            if runningThread: runningThread = False

def restartWakeUpThread(evt):
    global wakeupThread
    global wakeupEvent
    wakeupEvent = evt
    stopThread(wakeupThread)
    wakeupThread = threading.Thread(target=dontsleep, args=(wakeupEvent,20), daemon=True)
    wakeupThread.start()
        
def main():
    global wakeupThread

    osPlatform = platform.system()
    if 'Windows' in osPlatform:
        restartWakeUpThread(WakeUpEvent.VOLUME)
        cbDefaultValue = 'Volume Up/Down'
    else:
        restartWakeUpThread(WakeUpEvent.MOUSE)
        cbDefaultValue = 'Move Mouse'

    sg.theme('Dark')
    layout = [
        [sg.Text('Your computer will stay on as long as this program is running.\nClose it to disable it.')],
        [sg.Text('Event Type:'), sg.Combo(['Move Mouse', 'Volume Up/Down'], default_value=cbDefaultValue, key='cmbEventTypes', enable_events=True)]
    ]
    window = sg.Window('KeepMeAwake', layout, icon='icn.ico')
    
    while True:
        event, values = window.read(timeout=100)
        if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
            stopThread(wakeupThread)
            break
        if event == 'cmbEventTypes':
            if values['cmbEventTypes'] == 'Move Mouse':
                restartWakeUpThread(WakeUpEvent.MOUSE)
            elif values['cmbEventTypes'] == 'Volume Up/Down':
                restartWakeUpThread(WakeUpEvent.VOLUME)
    window.close()

if __name__ == '__main__':
    pyautogui.FAILSAFE = False
    main()
