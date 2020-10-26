from cube.cubeClass import Cube
from cube.colorPos import ColorPos

class Step6:

    def __init__(self):
        self.cubeOrigin = Cube()
        self.colorCubeCurrent = list()
        self.colorCubeOrigin = list()
        self.colorPos = ColorPos()

    def run(self, cubeCurrent, solveMoveList):
        res = self.checkCorner(cubeCurrent)
        if (res == 4):
            return True
        else:
            res = self.checkTryPosition(cubeCurrent)
            if (res[0] == 4):
                return True
            else:
                while res[0] == 0:
                    self.applyMix("D L D' R' D L' D' R", cubeCurrent, solveMoveList)
                    res = self.checkTryPosition(cubeCurrent)
                    if (res[0] == 4):
                        return True
                patternList = self.getPattern(cubeCurrent, res[1])
                self.moveDownFace(cubeCurrent, solveMoveList, patternList)

    def checkCorner(self, cubeCurrent):
        count = 0
        if ((self.colorPos.checkPositionColor(self.cubeOrigin, cubeCurrent, "yellow", "green", "red")) == True):
            count += 1
        if ((self.colorPos.checkPositionColor(self.cubeOrigin, cubeCurrent, "yellow", "blue", "magenta")) == True):
            count += 1
        if ((self.colorPos.checkPositionColor(self.cubeOrigin, cubeCurrent, "yellow", "red", "blue")) == True):
            count += 1
        if ((self.colorPos.checkPositionColor(self.cubeOrigin, cubeCurrent, "yellow", "magenta", "green")) == True):
            count += 1
        return (count)

    def checkTryPosition(self, cubeCurrent):
        count = 0
        correctCorner = list()
        self.colorCubeCurrent = self.colorPos.corner(cubeCurrent, "yellow", "red", "blue")
        if ((self.checkDoubleSide("front", "right"))) == True:
            count += 1
            correctCorner = ["yellow", "red", "blue"]
        self.colorCubeCurrent = self.colorPos.corner(cubeCurrent, "yellow", "blue", "magenta")
        if ((self.checkDoubleSide("right", "back"))) == True:
            count += 1
            correctCorner = ["yellow", "blue", "magenta"]
        self.colorCubeCurrent = self.colorPos.corner(cubeCurrent, "yellow", "magenta", "green")
        if ((self.checkDoubleSide("back", "left"))) == True:
            count += 1
            correctCorner = ["yellow", "magenta", "green"]
        self.colorCubeCurrent = self.colorPos.corner(cubeCurrent, "yellow", "green", "red")
        if ((self.checkDoubleSide("left", "front"))) == True:
            count += 1
            correctCorner = ["yellow", "green", "red"]
        return (count, correctCorner)

    def checkDoubleSide(self, face, subFace):
        count = 0
        i = 0
        while (i < len(self.colorCubeCurrent)):
            if (((self.colorCubeCurrent[i][0]) == face) or ((self.colorCubeCurrent[i][0]) == subFace)):
                count += 1
            i += 1
        return (count == 2)


    def getPattern(self, cubeCurrent, colorsList):
        patternList = list()
        if (["yellow", "red", "blue"] == colorsList):
            patternList.append(self.getDirection(cubeCurrent))
            if (patternList[0] == "left"):
                patternList.append("frontFace")
            else:
                patternList.append("rightFace")
        elif (["yellow", "magenta", "green"] == colorsList):
            patternList.append(self.getDirection(cubeCurrent))
            if (patternList[0] == "left"):
                patternList.append("backFace")
            else:
                patternList.append("leftFace")
        elif (["yellow", "blue", "magenta"] == colorsList):
            patternList.append(self.getDirection(cubeCurrent))
            if (patternList[0] == "left"):
                patternList.append("rightFace")
            else:
                patternList.append("backFace")
        elif (["yellow", "green", "red"] == colorsList):
            patternList.append(self.getDirection(cubeCurrent))
            if (patternList[0] == "left"):
                patternList.append("leftFace")
            else:
                patternList.append("frontFace")
        return patternList

    def getDirection(self, cubeCurrent):
        cubeCurrent.moveD()
        res = self.checkTryPosition(cubeCurrent)
        direction = "left"
        if (res[0] == 0):
            direction = "right"
        cubeCurrent.moveBackD()
        return (direction)

    def moveDownFace(self, cubeCurrent, solveMoveList, patternList):
        face = patternList[1]
        if (face == "frontFace"):
            if (patternList[0] == "right"):
                self.applyMix("D L D' R' D L' D' R", cubeCurrent, solveMoveList)
            else:
                self.applyMix("D' R' D L D' R D L'", cubeCurrent, solveMoveList)
        elif (face == "backFace"):
            if (patternList[0] == "right"):
                self.applyMix("D R D' L' D R' D' L", cubeCurrent, solveMoveList)
            else:
                self.applyMix("D' L' D R D' L D R'", cubeCurrent, solveMoveList)
        elif (face == "rightFace"):
            if (patternList[0] == "right"):
                self.applyMix("D F D' B' D F' D' B", cubeCurrent, solveMoveList)
            else:
                self.applyMix("D' B' D F D' B D F'", cubeCurrent, solveMoveList)
        elif (face == "leftFace"):
            if (patternList[0] == "right"):
                self.applyMix("D B D' F' D B' D' F", cubeCurrent, solveMoveList)
            else:
                self.applyMix("D' F' D B D' F D B'", cubeCurrent, solveMoveList)

#     def updatePositionList(self, cub, colors):
#       return (self.checkerManager.three(cub, colors[0], colors[1], colors[2]))


#       def finishedThreeColorPosition(self, cubeCurrent, colorsList):
#               return checkPositionColor(self.cubOrigin, cubeCurrent, colorsList[0], colorsList[1], colorsList[2])

    def applyMix(self, mix, cubeCurrent, solveMoveList):
        switcher = {
            "F":cubeCurrent.moveF, "B":cubeCurrent.moveB, "R":cubeCurrent.moveR, "L":cubeCurrent.moveL, "U":cubeCurrent.moveU, "D":cubeCurrent.moveD,
            "F\'":cubeCurrent.moveBackF, "B\'":cubeCurrent.moveBackB, "R\'":cubeCurrent.moveBackR, "L\'":cubeCurrent.moveBackL, "U\'":cubeCurrent.moveBackU, "D\'":cubeCurrent.moveBackD,
            "F2":cubeCurrent.moveDoubleF, "B2":cubeCurrent.moveDoubleB, "R2":cubeCurrent.moveDoubleR, "L2":cubeCurrent.moveDoubleL, "U2":cubeCurrent.moveDoubleU, "D2":cubeCurrent.moveDoubleD
        }
        for instruction in mix.split():
            switcher[instruction]()
            solveMoveList.append(instruction)