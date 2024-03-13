import pyautogui as start
import sys,time
import pyfiglet
import colorama
from colorama import Fore

def autoketik(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.008)
        
result = pyfiglet.figlet_format("Spam Whatsapp", font = "3x5")
print(53*"=")
autoketik(Fore.RED + result)

print(53*"=")
autoketik("            Program ini dibuat oleh Fadil           ")
print(53*"="+ "\n")

total = input("Jumlah pesan yang dikirim  : ")
msg = input("Masukan pesan yang dikirim : ")

counter=0

time.sleep(5)

while counter<int(total):
    start.typewrite(msg)
    start.press("Enter")
    counter+=1
else:
    print("Spam telah berhasil dikirim"+ "\n")
print(53*"=")
print("             Terimakasih telah menggunakan    ") 
print("                     program ini              ")
print(53*"="+ "\n")