#this how the "input text" will look like
f = open("saves/cach/location", "r")
location = f.read()
computername = "Cherman"
#textfärger:
white = "\033[0;37;40m"
green = "\033[0m\033[0;32;48m"
orange = "\033[0;33;40m"
red = "\033[0;31;40"
defult = "\033[0;0;0m"

if tf == "t":
  smiley = green + ":)"
elif tf == "f":
  smiley = red + ":("

con1 = white + "<" + green + computername + white + ":" + orange + usr + white + ":" + green + location + white + "> " + smiley + defult