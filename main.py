import keyboard
import mouse
import time 

print('!!! клики выполтоняются там, где стоит курсор !!!')
print(' ')
print('включить/выключить - "ALT + V"')
print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
isClicking = False




def set_clicker():
    global isClicking
    if isClicking:
        isClicking = False
        print('Кликер отключен')
    else:
        isClicking = True
        print('Кликер включен')


keyboard.add_hotkey('Alt + V', set_clicker)





while True:
    if isClicking:
        mouse.double_click(button = 'left')
        time.sleep(0.1)