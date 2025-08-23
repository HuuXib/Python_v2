import pyautogui

while True:
    if pyautogui.pixel(900,429) == (75, 219, 106):
        pyautogui.click()
        break