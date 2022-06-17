from time import sleep
import pyautogui
op = 1
pyautogui.alert('[1]abrir bloco de notas \n[2]abrir chrome')
op = int(pyautogui.prompt('escolha uma opcao'))
if op == 1:
    sleep(1)
    pyautogui.press('win')
    sleep(1)
    pyautogui.write('bloco de notas')
    sleep(2)
    pyautogui.press('enter')
elif op == 2:
    sleep(1)
    pyautogui.press('win')
    sleep(1)
    pyautogui.write('chrome')
    sleep(1)
    pyautogui.press('enter')
while op != 1 or op != 2:
    op = int(pyautogui.prompt('escolha uma opcao'))
    if op == 1:
        sleep(1)
        pyautogui.press('win')
        sleep(1)
        pyautogui.write('bloco de notas')
        sleep(2)
        pyautogui.press('enter')
    elif op == 2:
        sleep(1)
        pyautogui.press('win')
        sleep(1)
        pyautogui.write('chrome')
        sleep(1)
        pyautogui.press('enter')
    elif op != 1 or op !=2:
        pyautogui.alert('opcao invalida')



