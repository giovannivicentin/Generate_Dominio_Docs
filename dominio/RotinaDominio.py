import pyautogui
import time

img_path = 'dominio\\pyautogui-images\\'

class RotinaDominio:
    

    def __init__(self):
        pass


    rotinas = {
        'folha_cm': [img_path+'gerar_docs_cm_blue.png', img_path+'gerar_docs_cm_white.png'],
    }


    def Select_Rotinas_Automaticas(self, rotina):

        logo_path = (img_path+'logo.png')

        if rotina not in self.rotinas:
            raise ValueError("Invalid rotina name")

        # wait up to 15 seconds to find the image
        max_wait_time = 15
        start_time = time.time()
        while time.time() - start_time < max_wait_time:
            image_location = pyautogui.locateOnScreen(logo_path)
            if image_location is not None:
                break

        # if the image was found, continue the code
        if image_location is not None:

            pyautogui.sleep(3)

            pyautogui.press('esc')
            pyautogui.press('esc')

            pyautogui.hotkey('alt', 'p')
            pyautogui.hotkey('alt', 'u')
            pyautogui.sleep(2)

            # find the routine

            image1_path = self.rotinas.rotina[0]
            image2_path = self.rotinas.rotina[1]

            max_wait_time = 15
            start_time = time.time()
            while time.time() - start_time < max_wait_time:
                image1_location = pyautogui.locateOnScreen(image1_path)
                image2_location = pyautogui.locateOnScreen(image2_path)

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
                    break

                # verify if is adto
                if rotina[:2] == "ad":
                    pyautogui.moveTo(x=558, y=404, duration=0.2)
                    pyautogui.doubleClick()
                    time.sleep(0.2)
                    
                    # select "competencia da execução"
                    pyautogui.moveTo(x=1349, y=404, duration=0.2)
                    pyautogui.click()

                    # choose "competencia da execução" white or blue
                    comp_white = (img_path+'comp_da_exec_white.png')
                    comp_blue = (img_path+'comp_da_exec_blue.png')

                    max_wait_time = 15
                    start_time = time.time()
                    while time.time() - start_time < max_wait_time:
                        white_location = pyautogui.locateOnScreen(comp_white)
                        blue_location = pyautogui.locateOnScreen(comp_blue)

                        if white_location or blue_location:

                            # discover which image is
                            if white_location is not None:
                                location_comp = white_location
                            else:
                                location_comp = blue_location

                            # find the coords
                            location_center = pyautogui.center(location_comp)

                            # click in coords
                            pyautogui.click(location_center)

                            # go back and click in "não agendar" and pass the code
                            pyautogui.moveTo(x=559, y=433, duration=0.2)
                            pyautogui.click()

                            # go to "Empresas" table to start other class
                            pyautogui.moveTo(x=613, y=302, duration=0.3)
                            pyautogui.click()
                        else:
                            raise ValueError('Could not find "competência da execução" image.')
                else:
                    pyautogui.moveTo(x=558, y=404, duration=0.2)
                    pyautogui.doubleClick()
                    # verify the date in my computer, if the day is > 20, "competencia da execução" if is < 20, "competencia anteriro a execução"

            else:
                raise ValueError("Could not find automatic routine in Dominio")
        else:
            raise ValueError("Could not load Domínio after login")
