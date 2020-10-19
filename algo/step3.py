from cube.cubeClass import Cube
from cube.colorPos import ColorPos

class Step3:

    def __init__(self):
        self.cubeOrigin = Cube()
        self.colorCubeCurrent = list()
        self.colorCubeOrigin = list()
        self.colorPos = ColorPos()

    def run(self, cubeCurrent, solveMoveList):
        if ((self.colorPos.checkPositionColor(self.cubeOrigin, cubeCurrent, "red", "green")) == False):
            self.moving(cubeCurrent, solveMoveList, ["red", "green"], "front")
        if ((self.colorPos.checkPositionColor(self.cubeOrigin, cubeCurrent, "green", "magenta")) == False):
            self.moving(cubeCurrent, solveMoveList, ["green", "magenta"], "left")
        if ((self.colorPos.checkPositionColor(self.cubeOrigin, cubeCurrent, "magenta", "blue")) == False):
            self.moving(cubeCurrent, solveMoveList, ["magenta", "blue"], "back")
        if ((self.colorPos.checkPositionColor(self.cubeOrigin, cubeCurrent, "blue", "red")) == False):
            self.moving(cubeCurrent, solveMoveList, ["blue", "red"], "right")

    def moving(self, cubeCurrent, solveMoveList, colorsList, face):
        self.listPositionCubOrigin = self.colorPos.edge(self.cubeOrigin, colorsList[0], colorsList[1])
        self.listPositionCubCurrent = self.colorPos.edge(cubeCurrent, colorsList[0], colorsList[1])

        checkSideList = self.checkSide(cubeCurrent, colorsList)

        if (checkSideList[0] == True):
            self.moveToTryPosition(cubeCurrent, solveMoveList, colorsList)
        else:
            if (self.listPositionCubCurrent[0][0] != "down"):
                self.pushDown(cubeCurrent, solveMoveList, colorsList)
                self.listPositionCubCurrent = self.colorPos.edge(cubeCurrent, colorsList[0], colorsList[1])
            if (self.listPositionCubCurrent[0][0] != "down"):
                print ("ERROR DOWN IS NOT")
                sys.exit(-1)
            self.listPositionCubCurrent = self.colorPos.edge(cubeCurrent, colorsList[0], colorsList[1])
            if (self.listPositionCubCurrent[0][0] == "down"):
                self.moveToCente(cubeCurrent, solveMoveList, colorsList, face)
                self.listPositionCubCurrent = self.colorPos.edge(cubeCurrent, colorsList[0], colorsList[1])
                self.moveToTryPosition(cubeCurrent, solveMoveList, colorsList)

    def pushDown(self, cubeCurrent, solveMoveList, colorsList):
        faceOne, faceTwo, colorOne, colorTwo = self.getSideParams(cubeCurrent, colorsList)
        pattern = self.getPatternPushDown(faceOne, faceTwo)
        if (pattern == "rightPattern"):
            self.moveFormulaRight(cubeCurrent, solveMoveList, faceOne)
        elif (pattern == "leftPattern"):
            self.moveFormulaLeft(cubeCurrent, solveMoveList, faceOne)

    def getPatternPushDown(self, faceOne, faceTwo):
        if (faceOne == "left"):
            if (faceTwo == "front"):
                return ("rightPattern")
            elif (faceTwo == "back"):
                return ("leftPattern")
        elif (faceOne == "front" and faceTwo == "right"):
                return ("rightPattern")
        elif (faceOne == "right" and faceTwo == "back"):
            return ("rightPattern")

    def moveToCente(self, cubeCurrent, solveMoveList, colorsList, face):
        checkSideList = self.checkSide(cubeCurrent, colorsList)
        while (checkSideList[0] == False):
            cubeCurrent.moveD()
            solveMoveList.append("D")
            checkSideList = self.checkSide(cubeCurrent, colorsList)

    def checkSide(self, cubeCurrent, colorsList):
        down, face, colorDown, colorFace = self.getSideParams(cubeCurrent, colorsList)
        if (down != "down"):
            return [False, "null"]
        if (face == "front"):
            if (colorDown == "green" and colorFace == "red"):
                return [True, "leftPattern"]
            elif (colorDown == "blue" and colorFace == "red"):
                return [True, "rightPattern"]
        if (face == "back"):
            if (colorDown == "green" and colorFace == "magenta"):
                return [True, "leftPattern"]
            elif (colorDown == "blue" and colorFace == "magenta"):
                return [True, "rightPattern"]
        if (face == "right"):
            if (colorDown == "magenta" and colorFace == "blue"):
                return [True, "rightPattern"]
            elif (colorDown == "red" and colorFace == "blue"):
                return [True, "leftPattern"]
        if (face == "left"):
            if (colorDown == "red" and colorFace == "green"):
                return [True, "rightPattern"]
            elif (colorDown == "magenta" and colorFace == "green"):
                return [True, "leftPattern"]
        return [False, "null"]

    def getSideParams(self, cubeCurrent, colorsList):
        self.listPositionCubCurrent = self.colorPos.edge(cubeCurrent, colorsList[0], colorsList[1])
        down = self.listPositionCubCurrent[0][0]
        colorDown = self.listPositionCubCurrent[0][1]
        colorFace = self.listPositionCubCurrent[1][1]
        face = self.listPositionCubCurrent[1][0]
        return down, face, colorDown, colorFace

    def moveToTryPosition(self, cubeCurrent, solveMoveList, colorsList):
        down, face, colorDown, colorFace = self.getSideParams(cubeCurrent, colorsList)
        checkSideList = self.checkSide(cubeCurrent, colorsList)
        if (checkSideList[1] == "rightPattern"):
            self.moveFormulaRight(cubeCurrent, solveMoveList, face)
        elif (checkSideList[1] == "leftPattern"):
            self.moveFormulaLeft(cubeCurrent, solveMoveList, face)

    def moveFormulaLeft(self, cubeCurrent, solveMoveList, face):
        switcher = {
            "F":cubeCurrent.moveF, "B":cubeCurrent.moveB, "R":cubeCurrent.moveR, "L":cubeCurrent.moveL, "U":cubeCurrent.moveU, "D":cubeCurrent.moveD,
            "F\'":cubeCurrent.moveBackF, "B\'":cubeCurrent.moveBackB, "R\'":cubeCurrent.moveBackR, "L\'":cubeCurrent.moveBackL, "U\'":cubeCurrent.moveBackU, "D\'":cubeCurrent.moveBackD,
            "F2":cubeCurrent.moveDoubleF, "B2":cubeCurrent.moveDoubleB, "R2":cubeCurrent.moveDoubleR, "L2":cubeCurrent.moveDoubleL, "U2":cubeCurrent.moveDoubleU, "D2":cubeCurrent.moveDoubleD
        }
        if (face == "front"):
             mix = "D L D' L' D' F' D F"
        elif (face == "left"):
             mix = "D B D' B' D' L' D L"
        elif (face == "back"):
             mix = "D' L' D L D B D' B'"
        elif (face == "right"):
             mix = "D F D' F' D' R' D R"
        for instruction in mix.split():
            switcher[instruction]()
            solveMoveList.append(instruction)

    def moveFormulaRight(self, cubeCurrent, solveMoveList, face):
        switcher = {
            "F":cubeCurrent.moveF, "B":cubeCurrent.moveB, "R":cubeCurrent.moveR, "L":cubeCurrent.moveL, "U":cubeCurrent.moveU, "D":cubeCurrent.moveD,
            "F\'":cubeCurrent.moveBackF, "B\'":cubeCurrent.moveBackB, "R\'":cubeCurrent.moveBackR, "L\'":cubeCurrent.moveBackL, "U\'":cubeCurrent.moveBackU, "D\'":cubeCurrent.moveBackD,
            "F2":cubeCurrent.moveDoubleF, "B2":cubeCurrent.moveDoubleB, "R2":cubeCurrent.moveDoubleR, "L2":cubeCurrent.moveDoubleL, "U2":cubeCurrent.moveDoubleU, "D2":cubeCurrent.moveDoubleD
        }
        if (face == "front"):
             mix = "D' R' D R D F D' F'"
        elif (face == "left"):
             mix = "D' F' D F D L D' L'"
        elif (face == "right"):
             mix = "D' B' D B D R D' R'"
        elif (face == "back"):
             mix = "D R D' R' D' B' D B"
        for instruction in mix.split():
            switcher[instruction]()
            solveMoveList.append(instruction)