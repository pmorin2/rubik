from cube.cubeClass import Cube
from cube.colorPos import ColorPos

class Step7:

    def __init__(self):
        self.cubeOrigin = Cube()
        self.colorCubeCurrent = list()
        self.colorCubeOrigin = list()
        self.colorPos = ColorPos()

    def run(self, cubeCurrent, solveMoveList):
        cubeCurrent.mathHash()
        if (self.cubeOrigin.hash == cubeCurrent.hash):
            return True
        self.moveSide(cubeCurrent, solveMoveList, ["yellow", "red", "green"])
        self.moveDown(cubeCurrent, solveMoveList)
        self.moveSide(cubeCurrent, solveMoveList, ["yellow", "green", "magenta"])
        self.moveDown(cubeCurrent, solveMoveList)
        self.moveSide(cubeCurrent, solveMoveList, ["yellow", "blue", "magenta"])
        self.moveDown(cubeCurrent, solveMoveList)
        self.moveSide(cubeCurrent, solveMoveList, ["yellow", "blue", "red"])
        self.moveDown(cubeCurrent, solveMoveList)

    def moveDown(self, cubeCurrent, solveMoveList):
        cubeCurrent.moveD()
        solveMoveList.append("D")

    def moveSide(self, cubeCurrent, solveMoveList, colorsList):
        switcher = {
            "F":cubeCurrent.moveF, "B":cubeCurrent.moveB, "R":cubeCurrent.moveR, "L":cubeCurrent.moveL, "U":cubeCurrent.moveU, "D":cubeCurrent.moveD,
            "F\'":cubeCurrent.moveBackF, "B\'":cubeCurrent.moveBackB, "R\'":cubeCurrent.moveBackR, "L\'":cubeCurrent.moveBackL, "U\'":cubeCurrent.moveBackU, "D\'":cubeCurrent.moveBackD,
            "F2":cubeCurrent.moveDoubleF, "B2":cubeCurrent.moveDoubleB, "R2":cubeCurrent.moveDoubleR, "L2":cubeCurrent.moveDoubleL, "U2":cubeCurrent.moveDoubleU, "D2":cubeCurrent.moveDoubleD
        }
        while (self.finishedThreeColorPosition(cubeCurrent, colorsList)) == False:
            for instruction in ["L'", "U'", "L", "U"]:
                        switcher[instruction]()
                        solveMoveList.append(instruction)

    def finishedThreeColorPosition(self, cubeCurrent, colorsList):
        listPos = self.colorPos.corner(cubeCurrent, colorsList[0], colorsList[1], colorsList[2])
        listPosOrigin = self.colorPos.corner(self.cubeOrigin, colorsList[0], colorsList[1], colorsList[2])
        if (listPos[0][0] == "down" and listPos[0][1] == "yellow"):
            return True
        return False