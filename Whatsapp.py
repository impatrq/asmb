import pyautogui, webbrowser
from time import sleep

# include your country code and no spaces
phone = '5491161862342'

# open whatsapp web
webbrowser.open(f'https://web.whatsapp.com/send?phone={phone}')
print(111)
sleep(10)
print(2222)
# write the lines on page opened
pyautogui.typewrite('eyyy')

# press enter (send message)
pyautogui.press("enter")