from cube.cubeClass import Cube
from cube.colorPos import ColorPos

class Step4:

    def applyMix(self, mix, cubeCurrent, solveMoveList):
        switcher = {
            "F":cubeCurrent.moveF, "B":cubeCurrent.moveB, "R":cubeCurrent.moveR, "L":cubeCurrent.moveL, "U":cubeCurrent.moveU, "D":cubeCurrent.moveD,
            "F\'":cubeCurrent.moveBackF, "B\'":cubeCurrent.moveBackB, "R\'":cubeCurrent.moveBackR, "L\'":cubeCurrent.moveBackL, "U\'":cubeCurrent.moveBackU, "D\'":cubeCurrent.moveBackD,
            "F2":cubeCurrent.moveDoubleF, "B2":cubeCurrent.moveDoubleB, "R2":cubeCurrent.moveDoubleR, "L2":cubeCurrent.moveDoubleL, "U2":cubeCurrent.moveDoubleU, "D2":cubeCurrent.moveDoubleD
        }
        for instruction in mix.split():
            switcher[instruction]()
            solveMoveList.append(instruction)

    def run(self, cubeCurrent, solveMoveList):
        one,two = self.checkBackState(cubeCurrent.down, "yellow")
        if (one == 4):
            return True
        if (one == 1):
            self.applyMix(self, "F L D L' D' F'", cubeCurrent, solveMoveList)

        one,two = self.checkBackState(cubeCurrent.down, "yellow")
        if (one == 2 and two == 0):
            self.applyMix("F L D L' D' F'", cubeCurrent, solveMoveList)
        elif (one == 2 and two == 1):
            self.applyMix("D' F L D L' D' F'", cubeCurrent, solveMoveList)
        elif (one == 2 and two == 2):
            self.applyMix("D' D' F L D L' D' F'", cubeCurrent, solveMoveList)
        elif (one == 2 and two == 3):
            self.applyMix("D F L D L' D' F'", cubeCurrent, solveMoveList)

        one,two = self.checkBackState(cubeCurrent.down, "yellow")
        if (one == 3 and two == 0):
            self.applyMix("F L D L' D' F'", cubeCurrent, solveMoveList)
        elif (one == 3 and two == 1):
            self.applyMix("D F L D L' D' F'", cubeCurrent, solveMoveList)

        one,two = self.checkBackState(cubeCurrent.down, "yellow")
        if (one == 4):
            return True

    def checkBackState(self, cubFace, color):
        if cubFace[0][1] == color and cubFace[1][1] == color and cubFace[1][2] == color and cubFace[1][0] == color and cubFace[2][1] == color:
            return (4, 0)
        elif cubFace[1][0] == color and cubFace[1][1] == color and cubFace[1][2] == color:
            return (3, 0)
        elif cubFace[0][1] == color and cubFace[1][1] == color and cubFace[2][1] == color:
            return (3, 1)
        elif cubFace[2][1] == color and cubFace[1][1] == color and cubFace[1][2] == color:
            return (2, 0)
        elif cubFace[1][0] == color and cubFace[1][1] == color and cubFace[2][1] == color:
            return (2, 1)
        elif cubFace[0][1] == color and cubFace[1][1] == color and cubFace[1][0] == color:
            return (2, 2)
        elif cubFace[0][1] == color and cubFace[1][1] == color and cubFace[1][2] == color:
            return (2, 3)
        elif cubFace[1][1] == color:
            return (1, 0)
        return False, False
