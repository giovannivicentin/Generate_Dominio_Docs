import pyautogui
import time

img_path = 'dominio\\pyautogui-images\\'

rotinas = {
    'folha_cm': [(img_path + 'gerar_docs_cm_blue.png'), (img_path + 'gerar_docs_cm_white.png')],
}

# Get the key name
key_name = list(rotinas.keys())[0]
max_wait_time = 60
start_timer = time.time()
image1_path = rotinas[key_name][0]
image2_path = rotinas[key_name][1]

while time.time() - start_timer < max_wait_time:
    while True:
        image1_location = pyautogui.locateOnScreen(image1_path, region=(576, 357, 398, 341))
        if image1_location is not None:
            break
        image2_location = pyautogui.locateOnScreen(image2_path, region=(576, 357, 398, 341))
        if image2_location is not None:
            break
        time.sleep(0.1)

    # discover which image is
    if image1_location is not None:
        image_location = image1_location
    else:
        image_location = image2_location

    # find the coords
    image_center = pyautogui.center(image_location)
    # click in coords
    pyautogui.moveTo(image_center)
    pyautogui.doubleClick(image_center)

    # go to edit
    pyautogui.hotkey('alt', 'd')
    break
else:
    raise ValueError("Could not find automatic routine in Domínio")
