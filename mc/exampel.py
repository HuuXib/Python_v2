import pyautogui
import time

while True:
    # 1. Zniszcz blok (przytrzymaj LPM)
    pyautogui.mouseDown(button='left')
    time.sleep(1.8)  # Czas na zniszczenie bloku
    pyautogui.mouseUp(button='left')
    # currentx,currenty = pyautogui.position()
    # pyautogui.moveTo(currentx, currenty+ 500, duration=0.5)
    
    # 2. Przesuń się w prawo
    pyautogui.keyDown('w')  # Wciśnij 'D'
    time.sleep(0.5)         # Idź przez 0.5s
    pyautogui.keyUp('w')     # Zwolnij 'D'