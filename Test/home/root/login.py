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
      l = os.listdir(location + "home/User/" + usr)
      login = 1
  except:
    p = p
  try:
    exec(usr)
  except:
    i = i
