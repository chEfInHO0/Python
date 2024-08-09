import requests as req
import bs4
import keyboard as kb
from time import sleep

while True:
    a = req.get('https://dragon.mu/character/4e6472616e6768657461/X9999')
    mu = bs4.BeautifulSoup(a.text, features="html.parser")
    tds = mu.find_all('td')
    level = tds[7].get_text()
    print(level)
    if level == '328':
        kb.write('/reset')
        sleep(.5)
        kb.press('enter')
        kb.write('FAZ O PIX 79999508809')
    sleep(300)