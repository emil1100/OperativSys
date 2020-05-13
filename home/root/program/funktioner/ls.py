import os
f = open("saves/cach/location", "r")
l = f.read()
try:
  p = os.listdir(i[1])
except:
  p = os.listdir(l + i[1])
print(p)