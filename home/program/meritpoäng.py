w = 1
gf = 0
y = 0
while w == 1:
  x = input("Betyg: ")
  if x == "A":
    y = y + 20
  elif x == "B":
    y = y + 17.5
  elif x == "C":
    y = y + 15
  elif x == "D":
    y = y + 12.5
  elif x == "E":
    y = y + 10
  elif x == "F":
    y = y
  elif x == "Klart!":
    w = 0
  else:
    y = y
print(y)