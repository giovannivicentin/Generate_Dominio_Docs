import pyautogui
import time
from datetime import datetime
import psutil

img_path = 'dominio\\pyautogui-images\\'


class RoutineParameters:

    def __init__(self):
        pass

    rotinas = {
        'folha_cm': [img_path + 'gerar_docs_cm_blue.png', img_path + 'gerar_docs_cm_white.png'],
    }

    def Select_Automatic_Routines(self, rotina):

        if rotina not in self.rotinas:
            raise ValueError("Invalid routine name")

        # wait up to 60 seconds to verify if dominio is open
        app_name = "mstsc.exe"
        max_wait_time = 60
        start_time = time.time()
        app_running = False
        while time.time() - start_time < max_wait_time:
            for process in psutil.process_iter():
                process_info = process.as_dict(attrs=['name'])
                if process_info['name'] and app_name.lower() in process_info['name'].lower():
                    app_running = True
                    break
            if app_running:
                break
            time.sleep(1)

            pyautogui.sleep(40)

            pyautogui.moveTo(x=960, y=491, duration=0.2)
            pyautogui.click()

            pyautogui.press('esc')
            pyautogui.press('esc')

            pyautogui.hotkey('alt', 'p')
            pyautogui.hotkey('alt', 'u')
            pyautogui.sleep(2)

            # find the routine

            image1_path = self.rotinas[0]
            image2_path = self.rotinas[1]

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

                    # click in "Na data"
                    pyautogui.moveTo(x=558, y=404, duration=0.2)
                    pyautogui.doubleClick()
                    time.sleep(0.2)

                    # select competence in calculus
                    pyautogui.moveTo(x=1349, y=404, duration=0.2)
                    pyautogui.click()

                    # declarate img pathings
                    comp_white = (img_path + 'comp_da_exec_white.png')
                    comp_blue = (img_path + 'comp_da_exec_blue.png')

                    # choose "competencia da execução" white or blue
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
                    # click in "Na data"
                    pyautogui.moveTo(x=558, y=404, duration=0.2)
                    pyautogui.doubleClick()

                    # get now date
                    today = datetime.now()

                    # verify the date in computer, if the day is >= 20, select "competencia da execução"
                    if today.day >= 20:
                        # select competence in calculus
                        pyautogui.moveTo(x=1349, y=404, duration=0.2)
                        pyautogui.click()

                        # declarate img pathings
                        comp_white = (img_path + 'comp_da_exec_white.png')
                        comp_blue = (img_path + 'comp_da_exec_blue.png')

                        # choose "competencia da execução" white or blue
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
                                pyautogui.doubleClick()

                                # go to "Empresas" table to start other class
                                pyautogui.moveTo(x=613, y=302, duration=0.3)
                                pyautogui.doubleClick()

                    # else is < 20, "competencia anterior a execução"
                    else:
                        # select competence in calculus
                        pyautogui.moveTo(x=1349, y=404, duration=0.2)
                        pyautogui.click()

                        # declarate img pathings
                        prior_comp_white = (img_path + 'prior_comp_da_exec_white.png')
                        prior_comp_blue = (img_path + 'prior_comp_da_exec_blue.png')

                        # choose "competencia anterior à execução" white or blue
                        max_wait_time = 15
                        start_time = time.time()
                        while time.time() - start_time < max_wait_time:
                            prior_white_location = pyautogui.locateOnScreen(prior_comp_white)
                            prior_blue_location = pyautogui.locateOnScreen(prior_comp_blue)

                            if prior_white_location or prior_blue_location:

                                # discover which image is
                                if prior_white_location is not None:
                                    prior_location_comp = prior_white_location
                                else:
                                    prior_location_comp = prior_blue_location

                                # find the coords
                                prior_location_center = pyautogui.center(prior_location_comp)

                                # click in coords
                                pyautogui.click(prior_location_center)

                                # go back and click in "não agendar" and pass the code
                                pyautogui.moveTo(x=559, y=433, duration=0.2)
                                pyautogui.doubleClick()

                                # go to "Empresas" table to start other class
                                pyautogui.moveTo(x=613, y=302, duration=0.3)
                                pyautogui.doubleClick()

            else:
                raise ValueError("Could not find automatic routine in Dominio")
        else:
            raise ValueError("Could not load Dominio after login")
