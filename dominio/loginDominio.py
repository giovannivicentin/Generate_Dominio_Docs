import pyautogui
import time
from variables import user_dominio_folha, password_dominio_folha

class LoginDominio:
    def __init__(self):
        pass

    def click_image(self, image_path, timeout=15):
        start_time = time.time()
        while time.time() - start_time < timeout:
            location = pyautogui.locateCenterOnScreen(image_path)
            if location is not None:
                pyautogui.click(location)
                return True
            time.sleep(1)
        return False

    def user_login(self, user):
        self.click_image('pyautogui-images/user.png')
        pyautogui.moveTo(x=952, y=498, duration=0.5)
        pyautogui.doubleClick()
        pyautogui.typewrite(user)

    def password_login(self, password):
        self.click_image('pyautogui-images/password.png')
        pyautogui.moveTo(x=984, y=534, duration=0.5)
        pyautogui.doubleClick()
        pyautogui.typewrite(password)

    def ok_login(self):
        self.click_image('pyautogui-images/ok.png')

login = LoginDominio()
UserROTINASDP = login.user_login(user='ROTINASDP')
PasswordROTINASDPDP = login.password_login(password='74157')
OkLogin = login.ok_login()
