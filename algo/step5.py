from cube.cubeClass import Cube
from cube.colorPos import ColorPos

class Step5:

    def __init__(self):
        self.cubeOrigin = Cube()
        self.colorCubeCurrent = list()
        self.colorCubeOrigin = list()
        self.colorPos = ColorPos()

    def run(self, cubeCurrent, solveMoveList):
        res = self.moveDown(cubeCurrent, solveMoveList)
        if (res == 4):
            return True
        elif (res == 2):
            self.moveFace(cubeCurrent, solveMoveList)

    def moveDown(self, cubeCurrent, solveMoveList):
        count = 0
        while (count < 2):
            if ((self.colorPos.checkPositionColor(self.cubeOrigin, cubeCurrent, "yellow", "green")) == True):
                count += 1
            if ((self.colorPos.checkPositionColor(self.cubeOrigin, cubeCurrent, "yellow", "blue")) == True):
                count += 1
            if ((self.colorPos.checkPositionColor(self.cubeOrigin, cubeCurrent, "yellow", "red")) == True):
                count += 1
            if ((self.colorPos.checkPositionColor(self.cubeOrigin, cubeCurrent, "yellow", "magenta")) == True):
                count += 1
            if (count == 4):
                return 4
            if (count < 2):
                count = 0
                cubeCurrent.moveD()
                solveMoveList.append("D")
        return 2

    def moveFace(self, cubeCurrent, solveMoveList):
        res = 2
        if ((self.colorPos.checkPositionColor(self.cubeOrigin, cubeCurrent, "yellow", "green")) == True):
            if ((self.colorPos.checkPositionColor(self.cubeOrigin, cubeCurrent, "yellow", "blue")) == True):
                res = self.moveOppositeRibs(cubeCurrent, solveMoveList, "right")
        if ((self.colorPos.checkPositionColor(self.cubeOrigin, cubeCurrent, "yellow", "red")) == True):
            if ((self.colorPos.checkPositionColor(self.cubeOrigin, cubeCurrent, "yellow", "magenta")) == True):
                res = self.moveOppositeRibs(cubeCurrent, solveMoveList, "front")
        if (res == 2):
            self.cornerChange(cubeCurrent, solveMoveList, self.getIncorectCorner(cubeCurrent))

    def moveOppositeRibs(self, cubeCurrent, solveMoveList, face):
        switcher = {
            "F":cubeCurrent.moveF, "B":cubeCurrent.moveB, "R":cubeCurrent.moveR, "L":cubeCurrent.moveL, "U":cubeCurrent.moveU, "D":cubeCurrent.moveD,
            "F\'":cubeCurrent.moveBackF, "B\'":cubeCurrent.moveBackB, "R\'":cubeCurrent.moveBackR, "L\'":cubeCurrent.moveBackL, "U\'":cubeCurrent.moveBackU, "D\'":cubeCurrent.moveBackD,
            "F2":cubeCurrent.moveDoubleF, "B2":cubeCurrent.moveDoubleB, "R2":cubeCurrent.moveDoubleR, "L2":cubeCurrent.moveDoubleL, "U2":cubeCurrent.moveDoubleU, "D2":cubeCurrent.moveDoubleD
        }
        if (face == "front"):
            mix = "L D L' D L D2 L'"
        if (face == "right"):
            mix = "F D F' D F D2 F'"
        for instruction in mix.split():
            switcher[instruction]()
            solveMoveList.append(instruction)
        return self.moveDown(cubeCurrent, solveMoveList)

    def getIncorectCorner(self, cubeCurrent):
        isFalseBlue = self.colorPos.checkPositionColor(self.cubeOrigin, cubeCurrent, "yellow", "blue")
        isFalseGreen = self.colorPos.checkPositionColor(self.cubeOrigin, cubeCurrent, "yellow", "green")
        isFalseRed = self.colorPos.checkPositionColor(self.cubeOrigin, cubeCurrent, "yellow", "red")
        isFalseMagenta = self.colorPos.checkPositionColor(self.cubeOrigin, cubeCurrent, "yellow", "magenta")
        if (isFalseGreen == True and isFalseMagenta == True):
            return ("front")
        elif (isFalseGreen == True and isFalseRed == True):
            return ("right")
        elif (isFalseBlue == True and isFalseRed == True):
            return ("back")
        elif (isFalseMagenta  == True and isFalseBlue == True):
            return ("left")

    def cornerChange(self, cubeCurrent, solveMoveList, face):
        switcher = {
            "F":cubeCurrent.moveF, "B":cubeCurrent.moveB, "R":cubeCurrent.moveR, "L":cubeCurrent.moveL, "U":cubeCurrent.moveU, "D":cubeCurrent.moveD,
            "F\'":cubeCurrent.moveBackF, "B\'":cubeCurrent.moveBackB, "R\'":cubeCurrent.moveBackR, "L\'":cubeCurrent.moveBackL, "U\'":cubeCurrent.moveBackU, "D\'":cubeCurrent.moveBackD,
            "F2":cubeCurrent.moveDoubleF, "B2":cubeCurrent.moveDoubleB, "R2":cubeCurrent.moveDoubleR, "L2":cubeCurrent.moveDoubleL, "U2":cubeCurrent.moveDoubleU, "D2":cubeCurrent.moveDoubleD
        }
        if (face == "front"):
            mix = "L D L' D L D2 L' D"
        elif (face == "back"):
            mix = "R D R' D R D2 R' D"
        elif (face == "right"):
            mix = "F D F' D F D2 F' D"
        elif (face == "left"):
            mix = "B D B' D B D2 B' D"
        for instruction in mix.split():
            switcher[instruction]()
            solveMoveList.append(instruction)