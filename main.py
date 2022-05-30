import pyautogui
import time


def click(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.write("link do chat da pessoa")
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.hotkey('alt', 'space')
    time.sleep(0.3)
    pyautogui.press('x')


def check_screen():
    button = pyautogui.locateOnScreen("imagem1.png", confidence=0.9)

    if button is not None:
        click(button.left, button.top)
        return True

    return False


def main():
    pyautogui.hotkey('ctrl', 'alt', 'e')#atalhodonavegador
    while True:
        if check_screen():
            break


main()


def click1(x, y):
    time.sleep(0.3)
    pyautogui.moveTo(x, y)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.write("Bom dia")#textodamenssagem
    time.sleep(0.3)
    pyautogui.press('enter')
    pyautogui.hotkey()


def check_screen1():
    button1 = pyautogui.locateOnScreen("imagem2.png", confidence=0.8)

    if button1 is not None:
        click1(button1.left, button1.top)
        return True

    return False


def check():
    while True:
        if check_screen1():
            break


check()