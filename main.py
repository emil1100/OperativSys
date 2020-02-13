import os

print("00000000000000000000000000000")
print("00000000000000000000000000000")
print("0000000000´       `0000000000")
print("0000000000  *      0000000000")
print("000000´            #####00000")
print("000000            /#####00000")
print("000000     /############00000")
print("000000.    #############00000")
print("00000000000#####*##0000000000")
print("00000000000\######/0000000000")
print("00000000000000000000000000000")
print("00000000000000000000000000000")

p = os.listdir('program')
print("Alla program:")
print(p)

i = input("vilket programm: ")
i = "program/" + i + ".py"
p = open(i, "r")
k = p.read()
exec(k)
  

if i == "tilläg":
  n = input("Namn på programmet: ")
  a = open("ProgramSamling4t5tfadföjl.py", "a")
  print('Skriv programmet(skriv "klar" på raden efter programmet):')
  i = "1"
  while i != tilläg:
    i = input()
    if i == "klar":
      i = "0"
    else:
      f = f + "\n  " + i


  print("")
  print("")
  print("")
  print("")
  print("")
  print("")
  print("")
  print("")
  print(f)
  print("")
  i = input("'ja' eller 'nej', blev det rätt?: ")
  if i == "ja":
    a.write(f)
  else:
    print("ok, om du vill göra om så starta om programmet och gör inga fel annar tar det längre tid :)")
elif i == "radera":
  i = input()
  i = i + ".py"
  f = open(i, "w")
  f.write(".. .")
  print(i)