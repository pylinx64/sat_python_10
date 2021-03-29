import pyautogui

pyautogui.moveTo(233,655)   # перемещает мышку в x. y
pyautogui.click(button='left')

pyautogui.typewrite('print()')  # имитирует тест
pyautogui.keyDown('Enter')      # имитирует клавишу
pyautogui.PAUSE = 5             # пауза
pyautogui.typewrite('print()')

