import pyautogui
import time
from datetime import datetime


routines = {
        'folha_cm': [(img_path + 'gerar_docs_cm_blue.png'), (img_path + 'gerar_docs_cm_white.png')],
    }


def Select_Automatic_Routines( rotina):

        if routine not in self.routines:
            raise ValueError("Invalid routine name")

        pyautogui.sleep(45)

        pyautogui.moveTo(x=960, y=491, duration=0.2)
        pyautogui.click()

        pyautogui.hotkey('esc')
        pyautogui.sleep(0.25)

        pyautogui.press('esc')
        pyautogui.sleep(0.5)

        pyautogui.hotkey('alt', 'p')
        pyautogui.sleep(1)

        pyautogui.hotkey('u')
        pyautogui.sleep(2)

        # find the routine
        image1_path = self.routines[routine.Param][0]
        image2_path = self.routines[routine.param][1]

        max_wait_time = 30
        start_timer = time.time()

        # This script searches for two images on the screen and performs a set of actions when one of them is found.
        while time.time() - start_timer < max_wait_time:
            image1_location = pyautogui.locateOnScreen(image1_path, region=(576, 357, 398, 341))
            image2_location = pyautogui.locateOnScreen(image2_path, region=(576, 357, 398, 341))

            if image1_location or image2_location:

                # discover which image is
                if image1_location is not None:
                    image_location = image1_location
                else:
                    image_location = image2_location

                # find the coords
                image_center = pyautogui.center(image_location)
                # click in coords
                pyautogui.doubleClick(image_center)

                # go to edit
                pyautogui.hotkey('alt', 'd')
                time.sleep(1.5)
        else:
            raise ValueError("Could not find automatic routine in Domínio")
