import pyautogui as pag
from time import sleep

pag.PAUSE = 0.3

pag.press('win')
pag.write('chrome')
pag.press('enter')

sleep(2)
# clicando no meu perfil do chrome
pag.click(x=1288, y=457)

sleep(1)
pag.click(x=402, y=76)

# escrevendo no navegador o comando para ir pro canal do Krikor
sleep(2)
pag.write('https://www.youtube.com/@GMKrikor/videos')
pag.press('enter')

# clicando no vídeo mais recente
sleep(6)
pag.click(x=600, y=880)
