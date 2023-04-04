import pyautogui
import time

class LoginDominio:
    def __init__(self):
        image_path = None
        click_on_screen = None

    def click_image(self, image_path, timeout=15):
        start_time = time.time()
        while time.time() - start_time < timeout:
            try:
                x, y = pyautogui.locateCenterOnScreen(image_path)
                pyautogui.click(x, y)
                return True
            except TypeError:
                time.sleep(1)
                continue
        return False

    def user_login(self):
        click_image(self, pyautogui-images/user.png, timeout=15)
        pyautogui.moveTo(952, 498, duration=0.5)
        pyautogui.doubleClick()
        user = "ROTINASDP"
        pyautogui.typewrite(user)
