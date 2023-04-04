import pyautogui
import time
from variables import user_dominio_folha, password_dominio_folha

class LoginDominio:
    def __init__(self):
        image_path = None

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
        image_path = pyautogui-images/user.png
        click_image(self, image_path, timeout=15)
        pyautogui.moveTo(952, 498, duration=0.5)
        pyautogui.doubleClick()
        pyautogui.typewrite(user_dominio_folha)

    def password_login(self):
        image_path = pyautogui-images/password.png
        click_image(self, image_path, timeout=15)
        pyautogui.moveTo(984, 534, duration=0.5)
        pyautogui.doubleClick()
        pyautogui.typewrite(password_dominio_folha)

    def ok_login(self):
        image_path = pyautogui-images/ok.png
        click_image(self, image_path, timeout=15)