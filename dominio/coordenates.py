import pyautogui
import win32api
# Just a code that print coordenates per second acording your mouse on screen.

while True:
    x, y = pyautogui.position()
    width = win32api.GetSystemMetrics(0)
    height = win32api.GetSystemMetrics(1)
    prop_x = x/width
    prop_y = y/height
    print(f"Coordinates: ({x}, {y}) Screen proportion: ({prop_x}, {prop_y})")
    pyautogui.sleep(1)
