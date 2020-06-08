#this how the "input text" will look like


open6 = location + "saves/cach/location"
f = open(open6, "r")
LocationV = f.read()
if LocationV == location + "home/":
  LocationV = "~"

computername = "Cherman"


#textcolersd:
white = "\033[0;37;40m"
green = "\033[0m\033[0;32;48m"
dark_green = "\033[0m\033[2;32;48m"
orange = "\033[0;33;40m"
red = "\033[0;31;40m"
defult = "\033[0m\033[0;32;48m"
blue = "\033[0;34;40m"

if tf == "t":
  smiley = green + ":) "
elif tf == "f":
  smiley = red + ":( "

con1 = smiley + blue + computername + green + ":" + orange + usr + green + ":" + white + LocationV + green + " §" + defult