import os
import time


location = os.getcwd()
#locationS = location + "/"

#standard: \033[0m\033[1;32;48m
#blåbakrund: \033[32;44m
#gulbakrund: \033[0;37;43m
#vit text: \033[0;37;40m

login = 0
try:
  open1 = location + "home/root/saved_passwd.txt"
  l = open(open1, "r")
  t = l.read()
  exec(t)
except:
  location = location + "/"
  open1 = location + "home/root/saved_passwd.txt"
  l = open(open1, "r")
  t = l.read()
  exec(t)

open77 = location + "home/root/login.py"
f = open(open77, "r")
l = f.read()
exec(l)

if login == 1:
  os.system('clear')
  open2 = location + "saves/cach/location"
  f = open(open2, "w")
  if location != '':
    try:
      f.write(location + "home/" + usr)
    except:
      f.write(location + "home/")
  elif location == '':
    f.write("home/")
  open3 = location + "saves/configurations.py"
  f = open(open3, "r")
  ff = f.read()
  tf = "t"
  hej = location.split("/")
  print(hej)
  i = 0
  importl = ""
  hawekfj = 1
  while hawekfj == 1:
    try:
      if hej[i] != "":
        importl = importl + "." + hej[i]
      i = i + 1
    except:
      hawekfj = 0
      exec("from " + importl + ".home.root.program.commands import f")
  
  print("\033[1;32;48m")
  print("   00000000000000000000000   ")
  print(" 000000000000000000000000000 ")
  print("0000000000\033[32;44m´       `\033[0m\033[1;32;48m0000000000")
  print("0000000000\033[32;44m  *      \033[0m\033[1;32;48m0000000000")
  print("000000\033[32;44m´            \033[0;33;43m#####\033[0m\033[1;32;48m00000")
  print("000000\033[32;44m            \033[0;33;43m/#####\033[0m\033[1;32;48m00000")
  print("000000\033[32;44m     \033[0;33;43m/############\033[0m\033[1;32;48m00000")
  print("000000\033[32;44m.    \033[0;33;43m#############\033[0m\033[1;32;48m00000")
  print("00000000000\033[0;33;43m#####\033[0;37;43m*\033[0;33;43m##\033[0m\033[1;32;48m0000000000")
  print("00000000000\033[0;33;43m\######/\033[0m\033[1;32;48m0000000000")
  print(" 000000000000000000000000000 ")
  print("   00000000000000000000000   ")
  print("")
try:
  l = os.listdir(location + "home/User/" + usr)
  if usr == "":
    fssdif
except:
  for i in range(999999999999999999999999999 ** 99):
    slleep = 0.005
    print("\033[0m\033[0;31;48mHacker Alarm!")
    time.sleep(slleep)
    print("\033[0m\033[1;33;48mHacker Alarm!")
    time.sleep(slleep)
    print("\033[0m\033[1;93;48mHacker Alarm!")
    time.sleep(slleep)
    print("\033[0m\033[1;32;48mHacker Alarm!")
    time.sleep(slleep)
    print("\033[0m\033[1;96;48mHacker Alarm!")
    time.sleep(slleep)
    print("\033[0m\033[1;34;48mHacker Alarm!")
    time.sleep(slleep)
    print("\033[0m\033[1;35;48mHacker Alarm!")
    time.sleep(slleep)



























#print("                             ")
#print("   00000000000000000000000   ")
#print(" 000000000000000000000000000 ")
#print("0000000000´       `0000000000")
#print("0000000000  *      0000000000")
#print("000000´            #####00000")
#print("000000            /#####00000")
#print("000000     ############000000")
#print("000000.    #############00000")
#print("00000000000#####*##0000000000")
#print("00000000000\######/0000000000")
#print(" 000000000000000000000000000 ")
#print("   00000000000000000000000   ")
#print("                             ")

power = 1
while power == 1:
  exec(ff)
  y = input(con1 + " ")
  tf = "t"
  print("\033[0m\033[1;32;48m")
  i = y.split()
  try:
    open12356 = location + "home/root/program/funktioner.py"
    f = open(open12356, "r")
    iii = f.read()
    exec(iii)
  except:
    try:
      exec("f." + i[0])
    except:
      tf = "f"