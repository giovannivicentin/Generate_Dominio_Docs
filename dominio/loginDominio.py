import pyautogui
import time


class LoginDominio:

    def __init__(self):
        pass

    def click_image(self, image_path, timeout=15, return_position=False):
        start_time = time.time()
        while time.time() - start_time < timeout:
            location = pyautogui.locateCenterOnScreen(image_path)
            if location is not None:
                if return_position:
                    return location
                pyautogui.click(location)
                return True
            time.sleep(1)
        return None

    def user_login(self, user):
        center = self.click_image('dominio\\pyautogui-images\\user.png', return_position=True)
        if center is None:
            raise Exception("User image not found")
        x, y = center
        x += 150
        pyautogui.doubleClick(x=x, y=y)
        pyautogui.sleep(0.25)
        pyautogui.press('backspace')
        pyautogui.typewrite(user)

    def password_login(self, password):
        x = 975
        y = 534
        pyautogui.doubleClick(x=x, y=y)
        pyautogui.sleep(0.25)
        pyautogui.press('backspace')
        pyautogui.typewrite(password)
        pyautogui.sleep(0.25)
        pyautogui.press('enter')
