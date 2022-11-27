import random
import colorama
from colorama import *
import os
import time
import sys

colorama.init(autoreset = True)

lower_case = "abcdefghjklmnopqrstuvwxyz"
upper_case = "ABCDEFGHJKLMNOPQRSTUVWXYZ"
number = "1234567890"

Use_for = lower_case + upper_case + number
# OldCode
# length_for_pass = int(input('Password length:'))
try:
    length_for_pass = int(input("Password length(61 or more = crash):"))
    if length_for_pass >= 61:
    	os.system("cls")
    	sys.exit()
    if length_for_pass <= 60:
        os.system("cls")
except ValueError:
    print("It's not a number")
    time.sleep(2)
    sys.exit()

password = "".join(random.sample(Use_for, length_for_pass))

print(Fore.BLUE + '░█▀▀█ █▀▀█ █▀▀ █▀▀ █   █ █▀▀█ █▀▀█ █▀▀▄    █▀▀▀ █▀▀ █▀▀▄ █▀▀ █▀▀█ █▀▀█ ▀▀█▀▀ █▀▀█ █▀▀█\n░█▄▄█ █▄▄█ ▀▀█ ▀▀█ █▄█▄█ █  █ █▄▄▀ █  █    █ ▀█ █▀▀ █  █ █▀▀ █▄▄▀ █▄▄█   █   █  █ █▄▄▀\n░█    ▀  ▀ ▀▀▀ ▀▀▀  ▀ ▀  ▀▀▀▀ ▀ ▀▀ ▀▀▀     ▀▀▀▀ ▀▀▀ ▀  ▀ ▀▀▀ ▀ ▀▀ ▀  ▀   ▀   ▀▀▀▀ ▀ ▀▀')
print('\n')
print(Fore.RED + 'You password:' + Style.RESET_ALL + password)
os.system("pause")