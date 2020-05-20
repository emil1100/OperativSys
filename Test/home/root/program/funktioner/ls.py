import os
f = open("saves/cach/location", "r")
l = f.read()
try:
  open7 = location + i[1]
  p = os.listdir(open7)
except:
  open8 = location + l + i[1]
  p = os.listdir(open8)
print(p)