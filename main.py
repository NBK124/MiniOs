try:
	from setup import *
	from tid import *
except:
	ask()
if platform.system() == "Windows":
    def clear():
    	os.system('cls')
elif platform.system() == "Linux":
    def clear():
    	os.system('clear')
else:
	def clear():
		pass
spl = shutil.get_terminal_size().columns + 6
Version = "1.1"
Name = "MiniOs"
clear()

def main(ch):
	sys.stdout.write(f"\x1b]2;{Name, Version}\x07")
	print((colorama.Fore.BLUE + colorama.Style.BRIGHT+ APPS + colorama.Style.RESET_ALL).center(spl + 5))
	print((colorama.Back.GREEN + "123+*" + colorama.Style.RESET_ALL).center(spl))
	print((colorama.Back.GREEN + "456-/" + colorama.Style.RESET_ALL).center(spl))
	print((colorama.Back.GREEN + "7890=" + colorama.Style.RESET_ALL).center(spl))
	print((colorama.Fore.WHITE + CALC + colorama.Style.RESET_ALL).center(spl))
	print("\n")
	print((colorama.Back.BLUE + "• 12•" + colorama.Style.RESET_ALL).center(spl))
	print((colorama.Back.BLUE + "9-| 3" + colorama.Style.RESET_ALL).center(spl))
	print((colorama.Back.BLUE + "• 6 •" + colorama.Style.RESET_ALL).center(spl))
	print((colorama.Fore.WHITE + CLOCK + colorama.Style.RESET_ALL).center(spl))
	print("\n")
	print((colorama.Back.YELLOW + " 4K  " + colorama.Style.RESET_ALL).center(spl))
	print((colorama.Back.YELLOW + "Ultra" + colorama.Style.RESET_ALL).center(spl))
	print((colorama.Back.YELLOW + "  HD " + colorama.Style.RESET_ALL).center(spl))
	print((colorama.Fore.WHITE + JACKALER + colorama.Style.RESET_ALL).center(spl))
	print("\n")
	print((colorama.Back.RED + "  |  " + colorama.Style.RESET_ALL).center(spl))
	print((colorama.Back.RED + "┌–|–┐" + colorama.Style.RESET_ALL).center(spl))
	print((colorama.Back.RED + "└–––┘" + colorama.Style.RESET_ALL).center(spl))
	print((colorama.Fore.WHITE + SHUTDOWN + colorama.Style.RESET_ALL).center(spl))
	print("\n")
	
	ch = input(colorama.Fore.YELLOW + colorama.Style.BRIGHT+ CHOICE + colorama.Style.RESET_ALL)
	if ch == "1":
		clear()
		math(cch)
	elif ch == "2":
		clock()
	elif ch == "exit":
		shutdown()
	elif ch == "glitch":
		glitch()
	elif ch == Version:
		Easter()
	elif ch == "ecit":
		pecit()
	elif ch == '3':
		jackal()
	else:
		clear()
		main(ch)

def calc(d, x, y):
	print((colorama.Fore.YELLOW+ calc_D + colorama.Style.RESET_ALL).center(spl))
	d = input()
	try:
	    x = float(input(calc_X))
	    y = float(input(calc_Y))
	except:
		clear()
		calc(d, x, y)
		main(ch)
	if d == "1":
		print("\n")
		print(calc_RESULT, x + y)
	elif d == "2":
		print("\n")
		print(calc_RESULT, x - y)
	elif d == "3":
		print("\n")
		print(calc_RESULT, x * y)
	elif d == "4":
		if y != 0:
			print("\n")
			print(calc_RESULT, x / y)
		else:
			print("\n")
			print(calc_RESULT, "∞")
	elif d == "5":
		print("\n")
		print(calc_RESULT, x % y)
	elif d == "6":
		print("\n")
		print(calc_RESULT, x // y)
	elif d == "7":
		print("\n")
		print(calc_RESULT, x ** y)
	else:
		clear()
		calc(d, x, y)
		main(ch)
	input(colorama.Fore.GREEN + READY + colorama.Style.RESET_ALL)
	clear()
	main(ch)

def clock():
	print(datetime.now().strftime("%H:%M:%S"))
	print("\n")
	input(colorama.Fore.GREEN + READY + colorama.Style.RESET_ALL)
	clear()
	main(ch)

def glitch():
	gg = Timer(1, glitch)
	gg.start()
	clear()
	print(glich)
	main(ch)

def Easter():
	for num in range(1):
		egg = random.randint(1, 8)
		if egg == 1:
			input(colorama.Fore.RED + easter_1 + colorama.Style.RESET_ALL)
		elif egg == 2:
			input(colorama.Fore.RED + easter_2 + colorama.Style.RESET_ALL)
		elif egg == 3:
			input(colorama.Fore.RED + easter_3 + colorama.Style.RESET_ALL)
		elif egg == 4:
			input(colorama.Fore.RED + easter_4 + colorama.Style.RESET_ALL)
		elif egg == 5:
			input(colorama.Fore.RED + easter_5 + colorama.Style.RESET_ALL)
		elif egg == 6:
			input(colorama.Fore.RED + easter_6 + colorama.Style.RESET_ALL)
		elif egg == 7:
			input(colorama.Fore.RED + easter_7 + colorama.Style.RESET_ALL)
		else:
			input(colorama.Fore.RED + easter_8 + colorama.Style.RESET_ALL)
		clear()
		main(ch)

def ecit(ip):
	try:
	    for num in range(1):
		    exnum = str(random.randint(1, 12))
	    ip = input(colorama.Back.YELLOW + ecit_1 + colorama.Style.RESET_ALL)
	    if exnum == ip:
		    input(colorama.Fore.GREEN + READY + colorama.Style.RESET_ALL)
		    shutdown()
	    else:
		    clear()
		    ecit(ip)
	except:
		shutdown()

def pecit():
	clear()
	print(colorama.Fore.RED + ecit_0 + colorama.Style.RESET_ALL)
	time.sleep(0.6)
	ecit(ip)

def jackal():
	Version = 1.4
	Name = "Jackaler"
	sys.stdout.write(f"\x1b]2;{Name, Version}\x07")
	clear()
	print(colorama.Fore.YELLOW + jackal_INFO + colorama.Style.RESET_ALL)
	input(READY)
	clear()
	try:
		im = Image.open("system/before.png")
	except: 
		input(colorama.Fore.RED + jackal_ERROR + colorama.Style.RESET_ALL)
		clear()
		main(ch)
	try:
		cach = int(input(jackal_CACH))
	except:
		clear()
		jackal()
		main(ch)
	if cach < 2 or cach > 10:
		clear()
		jackal()
		main(ch)
	width, height = im.size
	width //= cach
	height //= cach
	new = im.resize((width, height))
	new.save("system/after.png")
	input(colorama.Fore.GREEN + READY + colorama.Style.RESET_ALL)
	clear()
	main(ch)

def math(cch):
	Version = 2.5
	Name = "Calculator Pack"
	sys.stdout.write(f"\x1b]2;{Name, Version}\x07")
	clear()
	print(colorama.Fore.YELLOW + calc_1 + colorama.Style.RESET_ALL)
	print(colorama.Fore.YELLOW + calc_2 + colorama.Style.RESET_ALL)
	print(colorama.Fore.YELLOW + calc_3 + colorama.Style.RESET_ALL)
	cch = input(calc_MODE)
	if cch == "1":
		clear()
		calc(d, x, y)
	elif cch == "2":
		clear()
		quad(a, b, c)
	elif cch == "3":
		clear()
		mass()
	else:
		clear()
		math(cch)

def quad(a, b, c):
	try:
		a = float(input(calc_A))
		b = float(input(calc_B))
		c = float(input(calc_C))
	except:
		clear()
		quad(a, b, c)
		main(ch)
	if a == 0:
		clear()
		quad(a, b, c)
		main(ch)
	dis = b ** 2 - 4 * a * c
	if dis > 0:
		x1 = (-b + dis ** 0.5) / (2 * a)
		x2 = (-b - dis ** 0.5) / (2 * a)
		print(calc_X1, x1)
		print(calc_X2, x2)
		input(colorama.Fore.GREEN + READY + colorama.Style.RESET_ALL)
		clear()
		main(ch)
	elif dis == 0:
		x1 = -b / (2 * a)
		print(calc_X1, x1)
		input(colorama.Fore.GREEN + READY + colorama.Style.RESET_ALL)
		clear()
		main(ch)
	else:
		print("Нет решения")
		input(colorama.Fore.GREEN + READY + colorama.Style.RESET_ALL)
		clear()
		main(ch)

def mass():
	sum = 0
	try:
		k = int(input(calc_MASS))
	except:
		clear()
		mass()
		main(ch)
	for i in range(k):
		try:
			mip = float(input(calc_SL))
		except:
			clear()
			mass()
			main(ch)
		sum += mip
	print(calc_RESULT, sum)
	input(colorama.Fore.GREEN + READY + colorama.Style.RESET_ALL)
	clear()
	main(ch)

def shutdown():
	sys.stdout.write(f"\x1b]2;{''}\x07")
	clear()
	exit()

main(ch)
