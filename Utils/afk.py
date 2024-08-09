import pygetwindow as gw
import pyautogui
import threading
import subprocess

def cristal_clear():
    subprocess.run(['cmd', '/c', 'cls'])

def list_all_itens(titles:list):
    cristal_clear()
    counter = 0
    for title in titles:
        if title == '':
            pass
        else:
            print(f'{counter} {title}')
        counter += 1

def window_interection():
    titles = gw.getAllTitles()
    invalid = True
    while invalid:
        try:
            list_all_itens(titles)
            active = int(input('Janela a ativar: ') or -1)
            if active < 0 or active > len(titles):
                raise(ValueError)
            invalid = False
            cristal_clear()
        except ValueError:
            invalid = True
    window = gw.getWindowsWithTitle(titles[active])[0]
    window.minimize()
    window.restore()



# Executar a função em segundo plano
# thread = threading.Thread(target=window_interection)
# thread.start()

window_interection()

# O código continua a ser executado, permitindo que você use o computador normalmente
