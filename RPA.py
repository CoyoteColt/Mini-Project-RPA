'''
Lembrando que fiz essa automação em um PC com 2 monitores UltraWide.
Remembering that I did this automation on a PC with 2 UltraWide monitors.

'''


import pyautogui
import time
import pandas as pd
import pyperclip

pyautogui.alert('Do not touch the computer until automation is complete')

pyautogui.PAUSE = 0.5
pyautogui.press('win')
pyautogui.write('Chrome')
pyautogui.press('enter')
pyautogui.write('google.com')
pyautogui.press('enter')
pyautogui.write('gmail.com')
pyautogui.press('enter')

x, y, largura, altura = pyautogui.locateOnScreen('Search_Google.png')
pyautogui.click(x + largura/2, y + altura/2)

while not pyautogui.locateOnScreen('Site_Loading.png'):
    time.sleep(1)

x, y, largura, altura = pyautogui.locateOnScreen('Google_apps.png')
pyautogui.click(x + largura/2, y + altura/2)
x, y, largura, altura = pyautogui.locateOnScreen('Google_apps.png')
pyautogui.click(x + largura/2, y + altura/2)

while not pyautogui.locateOnScreen('Contacts_Loading.png'):
    time.sleep(1)
    

x, y, largura, altura = pyautogui.locateOnScreen('Export.png')
pyautogui.click(x + largura/2, y + altura/2)
x, y, largura, altura = pyautogui.locateOnScreen('Export_Download.png')
pyautogui.click(x + largura/2, y + altura/2)
time.sleep(3)

df = pd.read_csv(r'C://Users/PythonRPA/Downloads/Contacts.csv')
#display(df)
df = df.dropna(axis=1)
#display(df)

pyautogui.hotkey('ctrl', 'pgup')
for email in df['E-mail - value']:
    x, y, largura, altura = pyautogui.locateOnScreen('Compose.png')
    pyautogui.click(x + largura/2, y + altura/2)
    pyautogui.write(email)
    pyautogui.press('enter')
    
pyautogui.press('tab')
pyautogui.write('customer list')
pyautogui.press('tab')

# obs: O RPA escreve somente texto no padrão Norte Americado, para escrever txt com caracteres especiais vamos usar o "Pyperclip".
# obs: RPA only writes text in the North American standard, to write txt with special characters we will use "Pyperclip"

txt = '''é, á, À, õ, jão. Lía. TáTa, Vó Vô Rô'''
pyperclip.copy(txt)
pyautogui.hotkey('ctrl', 'v')

x, y, largura, altura = pyautogui.locateOnScreen('Send.png')
pyautogui.click(x + largura/2, y + altura/2)

pyautogui.alert('Automation is complete')