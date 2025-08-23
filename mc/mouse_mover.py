import ctypes
import time

# Ustawienia
move_pixels = -800  # przesunięcie w lewo
delay = 0.5         # czas ruchu

time.sleep(3)  # czas na przełączenie okna

# Symulacja ruchu myszy (działa na poziomie drivera)
ctypes.windll.user32.mouse_event(0x0001, move_pixels, 0, 0, 0)
time.sleep(delay)