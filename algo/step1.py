from cube.cubeClass import Cube
from cube.colorPos import ColorPos

class Step1:

    def __init__(self):
        self.cubeOrigin = Cube()
        self.colorCubeCurrent = list()
        self.colorCubeOrigin = list()
        self.colorPos = ColorPos()

    def run(self, cubeCurrent, solveMoveList):
        if ((self.colorPos.checkPositionColor(self.cubeOrigin, cubeCurrent, "white", "red")) == False):
            self.edgeMoveTwoColor(cubeCurrent, solveMoveList, "white", "red", "front")
        if ((self.colorPos.checkPositionColor(self.cubeOrigin, cubeCurrent, "white", "magenta")) == False):
            self.edgeMoveTwoColor(cubeCurrent, solveMoveList, "white", "magenta", "back")
        if ((self.colorPos.checkPositionColor(self.cubeOrigin, cubeCurrent, "white", "blue")) == False):
            self.edgeMoveTwoColor(cubeCurrent, solveMoveList,  "white", "blue", "right")
        if ((self.colorPos.checkPositionColor(self.cubeOrigin, cubeCurrent, "white", "green")) == False):
            self.edgeMoveTwoColor(cubeCurrent, solveMoveList, "white", "green", "left")

    def edgeMoveTwoColor(self, cubeCurrent, solveMoveList, colorOne, colorTwo, face):
        self.colorCubeCurrent = self.colorPos.edge(cubeCurrent, colorOne, colorTwo)
        self.colorCubeOrigin = self.colorPos.edge(self.cubeOrigin, colorOne, colorTwo)

        if (face != self.colorCubeCurrent[0][0] and face != self.colorCubeCurrent[1][0]):
            self.moveDownTwoColor(cubeCurrent, solveMoveList, colorOne, colorTwo, face)
        if (face == self.colorCubeCurrent[0][0] or face == self.colorCubeCurrent[1][0]):
            if (self.colorCubeCurrent[0][1] == colorOne and self.colorCubeCurrent[0][0] == face and self.colorCubeCurrent[1][0] == "down") or (self.colorCubeCurrent[1][1] == colorOne and self.colorCubeCurrent[1][0] == face and self.colorCubeCurrent[0][0] == "down"):
                self.changeSideDown(cubeCurrent, solveMoveList, face)
            elif (self.colorCubeCurrent[0][1] == colorOne and self.colorCubeCurrent[0][0] == face and self.colorCubeCurrent[1][0] == "upper") or (self.colorCubeCurrent[1][1] == colorOne and self.colorCubeCurrent[1][0] == face and self.colorCubeCurrent[0][0] == "upper"):
                self.changeSideUpper(cubeCurrent, solveMoveList, face)
            else :
                self.moveCenter(cubeCurrent, solveMoveList, face, colorOne, colorTwo)
                if (self.colorCubeCurrent[0][1] == colorOne and self.colorCubeCurrent[0][0] == face and self.colorCubeCurrent[1][0] == "upper") or (self.colorCubeCurrent[1][1] == colorOne and self.colorCubeCurrent[1][0] == face and self.colorCubeCurrent[0][0] == "upper"):
                    self.changeSideUpper(cubeCurrent, solveMoveList, face)

    def moveCenter(self, cubeCurrent, solveMoveList, face, colorOne, colorTwo):
        while (self.colorCubeCurrent[1][2] != self.colorCubeOrigin[1][2]):
            if (face == "front"):
                cubeCurrent.moveBackF()
                solveMoveList.append("F'")
            if (face == "right"):
                cubeCurrent.moveBackR()
                solveMoveList.append("R'")
            if (face == "left"):
                cubeCurrent.moveBackL()
                solveMoveList.append("L'")
            if (face == "back"):
                cubeCurrent.moveBackB()
                solveMoveList.append("B'")
            self.colorCubeCurrent = self.colorPos.edge(cubeCurrent, colorOne, colorTwo)

    def updateFaceColor(self, cubeCurrent, colorOne, colorTwo):
        self.colorCubeCurrent = self.colorPos.edge(cubeCurrent, colorOne, colorTwo)
        return self.colorCubeCurrent[0][0], self.colorCubeCurrent[1][0]

    def moveDownTwoColor(self, cubeCurrent, solveMoveList, colorOne, colorTwo, face):
        faceOne,faceTwo = self.updateFaceColor(cubeCurrent, colorOne, colorTwo)

        def moveDownCenter(cubeCurrent, solveMoveList, colorOne, colorTwo, face):
            faceOne,faceTwo = self.updateFaceColor(cubeCurrent, colorOne, colorTwo)
            while (1):
                if (faceOne == face or faceTwo == face):
                    break
                cubeCurrent.moveD()
                solveMoveList.append("D")
                faceOne,faceTwo = self.updateFaceColor(cubeCurrent, colorOne, colorTwo)

        def optimizationStep(count, solveMoveList, move):
            if (count == 3):
                count = 1
                solveMoveList.append(move + "'")
                return count, 1
            else:
                x = 0
                while (x != count):
                    x += 1
                    solveMoveList.append(move)
            return count, 0

        count = 0
        if (faceOne == "front" or faceTwo == "front"):
            while (1):
                if (faceOne == "down" or faceTwo == "down"):
                    break
                count += 1
                cubeCurrent.moveF()
                faceOne,faceTwo = self.updateFaceColor(cubeCurrent, colorOne, colorTwo)
            count, flag = optimizationStep(count, solveMoveList, "F")
            moveDownCenter(cubeCurrent, solveMoveList, colorOne, colorTwo, face)
            while (count != 0):
                count -= 1
                if (flag == 0):
                    cubeCurrent.moveBackF()
                    solveMoveList.append("F'")
                else:
                    cubeCurrent.moveF()
                    solveMoveList.append("F")
        elif (faceOne == "left" or faceTwo == "left"):
            while (1):
                if (faceOne == "down" or faceTwo == "down"):
                    break
                count += 1
                cubeCurrent.moveL()
                faceOne,faceTwo = self.updateFaceColor(cubeCurrent, colorOne, colorTwo)
            count,flag = optimizationStep(count, solveMoveList, "L")
            moveDownCenter(cubeCurrent, solveMoveList, colorOne, colorTwo, face)
            while (count != 0):
                count -= 1
                if (flag == 0):
                    cubeCurrent.moveBackL()
                    solveMoveList.append("L'")
                else:
                    cubeCurrent.moveL()
                    solveMoveList.append("L")

        elif (faceOne == "right" or faceTwo == "right"):
            while (1):
                if (faceOne == "down" or faceTwo == "down"):
                    break
                count += 1
                cubeCurrent.moveR()
                faceOne,faceTwo = self.updateFaceColor(cubeCurrent, colorOne, colorTwo)
            count,flag = optimizationStep(count, solveMoveList, "R")
            moveDownCenter(cubeCurrent, solveMoveList, colorOne, colorTwo, face)
            while (count != 0):
                count -= 1
                if (flag == 0):
                    cubeCurrent.moveBackR()
                    solveMoveList.append("R'")
                else:
                    cubeCurrent.moveR()
                    solveMoveList.append("R")

        elif (faceOne == "back" or faceTwo == "back"):
            while (1):
                if (faceOne == "down" or faceTwo == "down"):
                    break
                count += 1
                cubeCurrent.moveB()
                faceOne,faceTwo = self.updateFaceColor(cubeCurrent, colorOne, colorTwo)
            count,flag = optimizationStep(count, solveMoveList, "B")
            moveDownCenter(cubeCurrent, solveMoveList, colorOne, colorTwo, face)
            while (count != 0):
                count -= 1
                if (flag == 0):
                    cubeCurrent.moveBackB()
                    solveMoveList.append("B'")
                else:
                    cubeCurrent.moveB()
                    solveMoveList.append("B")

    def changeSideDown(self, cubeCurrent, solveMoveList, face):
        switcher = {
            "F":cubeCurrent.moveF, "B":cubeCurrent.moveB, "R":cubeCurrent.moveR, "L":cubeCurrent.moveL, "U":cubeCurrent.moveU, "D":cubeCurrent.moveD,
            "F\'":cubeCurrent.moveBackF, "B\'":cubeCurrent.moveBackB, "R\'":cubeCurrent.moveBackR, "L\'":cubeCurrent.moveBackL, "U\'":cubeCurrent.moveBackU, "D\'":cubeCurrent.moveBackD,
            "F2":cubeCurrent.moveDoubleF, "B2":cubeCurrent.moveDoubleB, "R2":cubeCurrent.moveDoubleR, "L2":cubeCurrent.moveDoubleL, "U2":cubeCurrent.moveDoubleU, "D2":cubeCurrent.moveDoubleD
         }
        if (face == "front"):
            mix = "F' U' R U"
        elif (face == "right"):
            mix = "R' U' B U"
        elif (face == "left"):
            mix = "L' U' F U"
        elif (face == "back"):
            mix = "B' U' L U"
        for instruction in mix.split():
            switcher[instruction]()
            solveMoveList.append(instruction)

    def changeSideUpper(self, cubeCurrent, solveMoveList, face):
        switcher = {
            "F":cubeCurrent.moveF, "B":cubeCurrent.moveB, "R":cubeCurrent.moveR, "L":cubeCurrent.moveL, "U":cubeCurrent.moveU, "D":cubeCurrent.moveD,
            "F\'":cubeCurrent.moveBackF, "B\'":cubeCurrent.moveBackB, "R\'":cubeCurrent.moveBackR, "L\'":cubeCurrent.moveBackL, "U\'":cubeCurrent.moveBackU, "D\'":cubeCurrent.moveBackD,
            "F2":cubeCurrent.moveDoubleF, "B2":cubeCurrent.moveDoubleB, "R2":cubeCurrent.moveDoubleR, "L2":cubeCurrent.moveDoubleL, "U2":cubeCurrent.moveDoubleU, "D2":cubeCurrent.moveDoubleD
        }
        if (face == "front"):
            mix = "F U' R U"
        elif (face == "right"):
            mix = "R U' B U"
        elif (face == "left"):
            mix = "L U' F U"
        elif (face == "back"):
            mix = "B U' L U"
        for instruction in mix.split():
            switcher[instruction]()
            solveMoveList.append(instruction)