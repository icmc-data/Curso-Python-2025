import mss
import pyautogui

sct = mss.mss()

def tirar_screenshot():
    monitor = {"top": 290, "left": 175, "width": 50, "height": 1}
    screenshot = sct.grab(monitor)
    return screenshot

def deve_agachar():
    screenshot = tirar_screenshot()
    #verificar se os pixels de cima são pretos
    return tem_pixels_pretos

def deve_pular():
    screenshot = tirar_screenshot()
    linha = screenshot.pixels[0]
    soma_vermelhos = sum([p[0] for p in linha])
    print(soma_vermelhos)
    if soma_vermelhos != 12050:
        return True
    else:
        return False

def pular():
    pyautogui.press('up')

while True:
    if deve_pular():
        pular()
