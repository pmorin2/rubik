from algo.generalAlgorithm import GeneralAlgorithm
from random import randint
from cube.cubeClass import Cube
import argparse
import sys

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('mix', nargs='?', default="generator", help="mixing sequence")
  parser.add_argument("-g", "--generator", type=int, help="number of mixing movement to generate")
  parser.add_argument('-c', "--color", help="colored printing", action="store_true")
  parser.add_argument('-t', "--text", help="text printing", action="store_true")
  parser.add_argument('-f', "--french", help="french human undertandable moves", action="store_true")
  args = parser.parse_args()
  mix = args.mix
  if mix == "generator":
    movement = args.generator if args.generator else 8
    if movement < 1 :
        movement = 1
        print("number of random generated movements was set to 1")
    if movement > 1000:
        movement = 1000
        print("number of random generated movements was set to 100")
    face = ["F", "B", "R", "L", "U", "D"]
    modifier = ["", "\'", "2"]
    mix = ""

    for _ in range(0, movement):
        value_f = randint(0, 5)
        value_m = randint(0, 2)
        mix = mix + face[value_f] + modifier[value_m] + " "
  else:
    allowed = "FBRLUD2\' "
    if not all(c in allowed for c in mix):
        print("argument error, unauthorized character in mixing sequence !")
        sys.exit()

  cube = Cube()
  cubeTry = Cube()

  switcher = {
    "F":cube.moveF, "B":cube.moveB, "R":cube.moveR, "L":cube.moveL, "U":cube.moveU, "D":cube.moveD,
    "F\'":cube.moveBackF, "B\'":cube.moveBackB, "R\'":cube.moveBackR, "L\'":cube.moveBackL, "U\'":cube.moveBackU, "D\'":cube.moveBackD,
    "F2":cube.moveDoubleF, "B2":cube.moveDoubleB, "R2":cube.moveDoubleR, "L2":cube.moveDoubleL, "U2":cube.moveDoubleU, "D2":cube.moveDoubleD
  }
  switcherTry = {
      "F":cubeTry.moveF, "B":cubeTry.moveB, "R":cubeTry.moveR, "L":cubeTry.moveL, "U":cubeTry.moveU, "D":cubeTry.moveD,
      "F\'":cubeTry.moveBackF, "B\'":cubeTry.moveBackB, "R\'":cubeTry.moveBackR, "L\'":cubeTry.moveBackL, "U\'":cubeTry.moveBackU, "D\'":cubeTry.moveBackD,
      "F2":cubeTry.moveDoubleF, "B2":cubeTry.moveDoubleB, "R2":cubeTry.moveDoubleR, "L2":cubeTry.moveDoubleL, "U2":cubeTry.moveDoubleU, "D2":cubeTry.moveDoubleD
    }
  for instruction in mix.split():
    switcher[instruction]()
    switcherTry[instruction]()

  algo = GeneralAlgorithm(cube)
  result = algo.run()
  loopCheck = True
  while (loopCheck):
    loopCheck = False
    i = 0
    while (i < len(result) - 1):
        if (not "2" in result[i]) and (result[i] == result[i + 1]):
            result[i] = result[i][0] + "2"
            result.pop(i + 1)
            loopCheck = True
        elif ("2" in result[i]) and (result[i] == result[i + 1]):
            result.pop(i + 1)
            result.pop(i)
            loopCheck = True
        elif (not "2" in result[i]) and (not "2" in result[i + 1]) and (result[i] != result[i + 1]) and (result[i][0] == result[i + 1][0]):
            result.pop(i + 1)
            result.pop(i)
            loopCheck = True
        elif ("2" in result[i] or "2" in result[i + 1]) and (result[i] != result[i + 1]) and (result[i][0] == result[i + 1][0]):
            if ("'" in result[i] or "'" in result[i + 1]):
                result[i] = result[i][0]
                result.pop(i + 1)
                loopCheck = True
            else:
                result[i] = result[i][0] + "'"
                result.pop(i + 1)
                loopCheck = True
        i += 1

  toPrint = ""
  for instruction in mix.split():
    toPrint = toPrint + instruction + " "
  print ("mixing moves: " + toPrint)
  print("\n================================================================================")
  print("                                 PROCESSING                                     ")
  print("================================================================================\n")
  toPrint = ""
  switcherHuman = {
    "F":"Face avant, sens horaire", "B":"Face arrière, sens horaire", "R":"Face droite, sens horaire", "L":"Face gauche, sens horaire", "U":"Face dessus, sens horaire", "D":"Face dessous, sens horaire",
    "F\'":"Face avant, sens anti-horaire", "B\'":"Face arrière, sens anti-horaire", "R\'":"Face droite, sens anti-horaire", "L\'":"Face gauche, sens anti-horaire", "U\'":"Face dessus, sens anti-horaire", "D\'":"Face dessous, sens anti-horaire",
    "F2":"Face avant, demi-tour", "B2":"Face arrière, demi-tour", "R2":"Face droite, demi-tour", "L2":"Face gauche, demi-tour", "U2":"Face dessus, demi-tour", "D2":"Face dessous, demi-tour"
  }
  for instruction in result:
      toPrint = toPrint + instruction + " "
  print ("solution moves: " + toPrint)
  if (args.french or args.text or args.color):
    if (args.text):
      cubeTry.printCubeText()
    if (args.color):
      cubeTry.printCubeColor()
    for instruction in result:
      switcherTry[instruction]()
      print("")
      if (args.french):
        print(switcherHuman[instruction])
      else:
        print(instruction)
      if (args.text):
        cubeTry.printCubeText()
      if (args.color):
        cubeTry.printCubeColor()
