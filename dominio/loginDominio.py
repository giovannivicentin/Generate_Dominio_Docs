import pyautogui
import time


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
        self.click_image('dominio\\pyautogui-images\\user.png')
        pyautogui.moveTo(x=952, y=498, duration=0.5)
        pyautogui.doubleClick()
        pyautogui.typewrite(user)

    def password_login(self, password):
        self.click_image('dominio\\pyautogui-images\\password.png')
        pyautogui.moveTo(x=984, y=534, duration=0.5)
        pyautogui.doubleClick()
        pyautogui.typewrite(password)
        pyautogui.press('enter')
