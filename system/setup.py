try:
	import os
	import sys
	import time
	import shutil
	import random
	import platform
	from PIL import Image
	from threading import Timer
	from datetime import datetime
except:
	pass
def Setup():
	print("Идёт процесс установки необходимых модулей...")
	os.system("pip install colorama")
	os.system("pip install pillow")
	print("Установка завершена")
	exit()

def ask():
	askinp = input("Установить необходимые модули? (y/n) ")
	if askinp == 'y':
		Setup()
	elif askinp == 'n':
		print("Установка отменена")
		exit()
	else:
		ask()
