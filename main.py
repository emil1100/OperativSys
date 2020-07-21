import os
import time

location = os.getcwd()
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
  for i in range(99999999999999999999999999999999 * 99999999999999999999999999999999999999999999999999999999999):
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
  ii = y.split()
  i = ii
  try:
    ii = "home/root/program/" + i[0] + ".py"
    open4 = location + ii
    p = open(open4, "r")
    k = p.read()
    exec(k)
  except:
    try:
      ii = "home/root/program/" + i[0]
      open4 = location + ii
      p = open(open4, "r")
      k = p.read()
    except:
      try:
        ii = "home/root/program/funktioner/" + i[0] + ".py"
        open5 = location + ii
        p = open(open5, "r")
        k = p.read()
        exec(k)
      except:
        try:
          exec(y)
        except:
          try:
            hesdfsfdjlkasjdhfjal = i[1]
            print("\033[0m\033[1;32;48mSyntaxError: ", y, " ")
            tf = "f"
          except:
            try:
              exec("print(" + i + ")")
            except:
              print("\033[0m\033[1;32;48mSyntaxError: ", y, " ")
              tf = "f"