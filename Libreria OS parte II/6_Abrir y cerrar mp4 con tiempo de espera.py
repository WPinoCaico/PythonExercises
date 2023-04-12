import os
import time

os.startfile("AHORA_Y_AQUI.mp4")

time.sleep(5)

os.system("TASKKILL /F /IM wmplayer.exe")
