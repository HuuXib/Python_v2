import pyautogui
import time

while True:
    # 1. Zniszcz blok (przytrzymaj LPM)
    pyautogui.mouseDown(button='left')
    time.sleep(1.8)  # Czas na zniszczenie bloku
    pyautogui.mouseUp(button='left')
    
    # 2. Przesuń się w prawo
    pyautogui.keyDown('d')  # Wciśnij 'D'
    time.sleep(0.5)         # Idź przez 0.5s
    pyautogui.keyUp('d')    # Zwolnij 'D'
    
    # 3. Wróć do pozycji (lewo)
    pyautogui.keyDown('a')
    time.sleep(0.5)
    pyautogui.keyUp('a')