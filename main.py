import os

location = input("where is this program? ")
#standard: \033[0m\033[1;32;48m
#blåbakrund: \033[32;44m
#gulbakrund: \033[0;37;43m
#vit text: \033[0;37;40m

login = 0

l = open("home/root/saved_passwd.txt", "r")
t = l.read()
exec(t)

print("\033[0m\033[1;32;48m")
f = 0
while login != 1:
  if f >= 10:
    for f in range(100000000000000000):
      input("User : ")
      input("password: \033[0;30;40m")
      print("\033[0m\033[1;32;48m")
    f = 0
  i = input("User: ")
  usr = i
  p = input("password: \033[0;30;40m")
  f = f + 1
  print("\033[0m\033[1;32;48m")
  try:
    exec("i = " + i)
  except:
    p = p
  try:
    if i == p:
      l = os.listdir("home/User/" + usr)
      login = 1
  except:
    p = p
  try:
    exec(usr)
  except:
    i = i

if login == 1:
  os.system('clear')
  f = open("saves/cach/location", "w")
  if location != '':
    f.write(location + "home/")
  elif location == '':
    f.write("home/")
  f = open("saves/configurations.py", "r")
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
  l = os.listdir("home/User/" + usr)
except:
  for i in range(99999999999999999999999999999999999999999999):
    print("Hacker Alarm!")


























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
    p = open(ii, "r")
    k = p.read()
    exec(k)
  except:
    try:
      ii = "home/root/program/funktioner/" + i[0] + ".py"
      p = open(ii, "r")
      k = p.read()
      exec(k)
    except:
      try:
        exec(y)
      except:
        print("\033[0m\033[1;32;48mSyntaxError: ", y, " ")
        tf = "f"