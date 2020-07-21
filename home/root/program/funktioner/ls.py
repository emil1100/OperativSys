
elif i[1] != "":
  open7 = location + i[1]
  p = os.listdir(open7)
else:
  open8 = location
  p = os.listdir(open8)
print(p)