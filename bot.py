import pyautogui
import time

pyautogui.alert('vai comecar')
time.sleep(2)
pyautogui.press('winleft')
time.sleep(0.2)
pyautogui.write('edge')
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(0.8)
def click(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.write("https://www.facebook.com/")
    pyautogui.press("enter")
    time.sleep(10)
    pyautogui.moveTo(1220, 142)
    time.sleep(0.3)
    pyautogui.click()
    time.sleep(0.3)
    pyautogui.moveTo(1127, 241)
    time.sleep(0.5)
    pyautogui.click()
    time.sleep(0.3)
    pyautogui.write("nome") #nomedapessoapraquemvcquermandarbomdia
    time.sleep(2)
    pyautogui.press('tab')
    time.sleep(0.3)
    pyautogui.press("enter")
    pyautogui.write("BOM DIA")
    pyautogui.press("enter")
    pyautogui.hotkey('alt', 'space')
    time.sleep(0.5)
    pyautogui.press("x")
    pyautogui.hotkey('alt', 'F4')
    pyautogui.alert('pode usar já')


def check_screen():
    button = pyautogui.locateOnScreen("image.png", confidence=0.6)

    if button != None:
        click(button.left, button.top)
        return True

    return False


def main():
    check_screen()


main()
