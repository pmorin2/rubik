from cube.cubeClass import Cube
from cube.colorPos import ColorPos

class Step2:

    def __init__(self):
        self.cubeOrigin = Cube()
        self.colorCubeCurrent = list()
        self.colorCubeOrigin = list()
        self.colorPos = ColorPos()

    def run(self, cubeCurrent, solveMoveList):
        if ((self.colorPos.checkPositionColor(self.cubeOrigin, cubeCurrent, "white", "red", "blue")) == False):
            self.moving(cubeCurrent, solveMoveList, "white", "red", "blue", "front")
        if ((self.colorPos.checkPositionColor(self.cubeOrigin, cubeCurrent, "white", "blue", "magenta")) == False):
            self.moving(cubeCurrent, solveMoveList, "white", "blue", "magenta", "right")
        if ((self.colorPos.checkPositionColor(self.cubeOrigin, cubeCurrent, "white", "magenta", "green")) == False):
            self.moving(cubeCurrent, solveMoveList, "white", "magenta", "green", "back")
        if ((self.colorPos.checkPositionColor(self.cubeOrigin, cubeCurrent, "white", "green", "red")) == False):
            self.moving(cubeCurrent, solveMoveList, "white", "green", "red", "left")

#     def updatePositionList(self, cub, colorOne, colorTwo, colorThree):
#         return (self.colorPos.corner(cub, colorOne, colorTwo, colorThree))

    def moving(self, cubeCurrent, solveMoveList, colorOne, colorTwo, colorThree, face):
        self.listPositionCubOrigin = self.colorPos.corner(self.cubeOrigin, colorOne, colorTwo, colorThree)
        self.listPositionCubCurrent = self.colorPos.corner(cubeCurrent, colorOne, colorTwo, colorThree)

        if (self.checkSide(cubeCurrent, face)) == False:
            if (self.listPositionCubCurrent[0][0] == "upper"):
                self.moveEdgeDown(cubeCurrent, solveMoveList, colorOne, colorTwo, colorThree)
            if (self.listPositionCubCurrent[0][0] == "down"):
                self.moveEdgeDownToPosition(cubeCurrent, solveMoveList, colorOne, colorTwo, colorThree, face)
        self.listPositionCubCurrent = self.colorPos.corner(cubeCurrent, colorOne, colorTwo, colorThree)
        if (self.checkSide(cubeCurrent, face)) == True:
            self.moveSide(cubeCurrent, solveMoveList, colorOne, colorTwo, colorThree, face)

    def checkSide(self, cubeCurrent, face):
        if (face == "front"):
            return (self.checkDoubleSide(face, "right"))
        elif (face == "right"):
            return (self.checkDoubleSide(face, "back"))
        elif (face == "back"):
            return (self.checkDoubleSide(face, "left"))
        elif (face == "left"):
            return (self.checkDoubleSide(face, "front"))
        return False

    def checkDoubleSide(self, face, subFace):
        count = 0
        for i in range(0, len(self.listPositionCubCurrent)):
            if (((self.listPositionCubCurrent[i][0]) == face) or ((self.listPositionCubCurrent[i][0]) == subFace)):
                count += 1
        return (count == 2)

    def moveEdgeDown(self, cubeCurrent, solveMoveList, colorOne, colorTwo, colorThree):
        self.listPositionCubCurrent = self.colorPos.corner(cubeCurrent, colorOne, colorTwo, colorThree)
        switcher = {
            "F":cubeCurrent.moveF, "B":cubeCurrent.moveB, "R":cubeCurrent.moveR, "L":cubeCurrent.moveL, "U":cubeCurrent.moveU, "D":cubeCurrent.moveD,
            "F\'":cubeCurrent.moveBackF, "B\'":cubeCurrent.moveBackB, "R\'":cubeCurrent.moveBackR, "L\'":cubeCurrent.moveBackL, "U\'":cubeCurrent.moveBackU, "D\'":cubeCurrent.moveBackD,
            "F2":cubeCurrent.moveDoubleF, "B2":cubeCurrent.moveDoubleB, "R2":cubeCurrent.moveDoubleR, "L2":cubeCurrent.moveDoubleL, "U2":cubeCurrent.moveDoubleU, "D2":cubeCurrent.moveDoubleD
        }
        if ((self.listPositionCubCurrent[1][0] == "right" and self.listPositionCubCurrent[2][0] == "front")):
            mix = "F D' F'"
        elif ((self.listPositionCubCurrent[1][0] == "left" and self.listPositionCubCurrent[2][0] == "front")):
            mix = "F' D F"
        elif ((self.listPositionCubCurrent[1][0] == "right" and self.listPositionCubCurrent[2][0] == "back")):
            mix = "B' D B"
        elif ((self.listPositionCubCurrent[1][0] == "left" and self.listPositionCubCurrent[2][0] == "back")):
            mix = "B D' B'"
        for instruction in mix.split():
            switcher[instruction]()
            solveMoveList.append(instruction)
        self.listPositionCubCurrent = self.colorPos.corner(cubeCurrent, colorOne, colorTwo, colorThree)

    def moveEdgeDownToPosition(self, cubeCurrent, solveMoveList, colorOne, colorTwo, colorThree, face):
        while (self.checkSide(cubeCurrent, face)) == False:
            cubeCurrent.moveD()
            solveMoveList.append("D")
            self.listPositionCubCurrent = self.colorPos.corner(cubeCurrent, colorOne, colorTwo, colorThree)

    def moveSide(self, cubeCurrent, solveMoveList, colorOne, colorTwo, colorThree, face):
        self.listPositionCubCurrent = self.colorPos.corner(cubeCurrent, colorOne, colorTwo, colorThree)
        switcher = {
            "F":cubeCurrent.moveF, "B":cubeCurrent.moveB, "R":cubeCurrent.moveR, "L":cubeCurrent.moveL, "U":cubeCurrent.moveU, "D":cubeCurrent.moveD,
            "F\'":cubeCurrent.moveBackF, "B\'":cubeCurrent.moveBackB, "R\'":cubeCurrent.moveBackR, "L\'":cubeCurrent.moveBackL, "U\'":cubeCurrent.moveBackU, "D\'":cubeCurrent.moveBackD,
            "F2":cubeCurrent.moveDoubleF, "B2":cubeCurrent.moveDoubleB, "R2":cubeCurrent.moveDoubleR, "L2":cubeCurrent.moveDoubleL, "U2":cubeCurrent.moveDoubleU, "D2":cubeCurrent.moveDoubleD
        }
        for i in range(0, 3):
            if (self.listPositionCubCurrent[i][1] == colorOne and self.listPositionCubCurrent[i][0] == face):
                if (face == "front"):
                    mix = "D' R' D R"
                elif (face == "right"):
                    mix = "D' B' D B"
                elif (face == "back"):
                    mix = "D' L' D L"
                elif (face == "left"):
                    mix = "D' F' D F"
                for instruction in mix.split():
                    switcher[instruction]()
                    solveMoveList.append(instruction)
                return(self)
        while ((self.colorPos.checkPositionColor(self.cubeOrigin, cubeCurrent, colorOne, colorTwo, colorThree)) == False):
            if (face == "front"):
                mix = "R' D' R D"
            elif (face == "right"):
                mix = "B' D' B D"
            elif (face == "back"):
                mix = "L' D' L D"
            elif (face == "left"):
                mix = "F' D' F D"
            for instruction in mix.split():
                switcher[instruction]()
                solveMoveList.append(instruction)