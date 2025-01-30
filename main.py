import webbrowser
import time
import pyautogui

print("Starting...")


url = 'https://www.tiktok.com/messages?lang=en&u=ID'    #<---------------this paste ID
webbrowser.open(url)

time.sleep(20)

pyautogui.moveTo(x, y) # <------------------ enter your x and y 

pyautogui.click()

time.sleep(2)

pyautogui.typewrite("Get up samurai!", interval=0.1)    #<-------- massage for your friends
time.sleep(1)
pyautogui.press('enter')

time.sleep(2)

pyautogui.typewrite("An eternal interesting path awaits us... ", interval=0.1)
time.sleep(1)
pyautogui.press('enter')

print("Completed!")
