import os
try:
  try:
    open7 = location + i[1]
    p = os.listdir(open7)
  except:
    open8 = location
    p = os.listdir(open8)
  print(p)
except:
