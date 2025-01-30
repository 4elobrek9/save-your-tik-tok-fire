import pyautogui
import time

print("go to tik tok in your tik tok account and\ngo to your friend’s account after click on “send messages” and copy the link\n((user ID is indicated there)) after perform the action what happens next\n")
time.sleep(2)
print("move the cursor to the message input field in tiktok for 20 seconds")

time.sleep(20) 

x, y = pyautogui.position()
print(f"mouse coordinates: x={x}, y={y}")
