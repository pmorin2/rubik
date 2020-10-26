from termcolor import colored
import hashlib

class Cube:
    def __init__(self):
        faces = ['front', 'back', 'right', 'left', 'upper', 'down']
        self.colors = ["red", "magenta", "blue", "green", "white", "yellow"]
        self.switcher = {"red":"  red  ", "magenta":"magenta", "blue":" blue  ", "green":" green ", "white":" white ", "yellow":"yellow "}
        self.front = self.listFill(self.colors[0])
        self.back = self.listFill(self.colors[1])
        self.right = self.listFill(self.colors[2])
        self.left = self.listFill(self.colors[3])
        self.upper = self.listFill(self.colors[4])
        self.down = self.listFill(self.colors[5])
        self.hash = ""
        self.mathHash()

    def listFill(self, color):
        list = []
        for line in range(3):
            string = []
            for column in range(3):
                string.append(color)
            list.append(string)
        return (list)

########  ALL MOVEMENTS SIDE ########
    def moveU(self):
        buff = self.right[0]
        self.right[0] = self.back[0]
        self.back[0] = self.left[0]
        self.left[0] = self.front[0]
        self.front[0] = buff
        self.moveFront(self.upper, 'u')

    def moveBackU(self):
        buff = self.right[0]
        self.right[0] = self.front[0]
        self.front[0] = self.left[0]
        self.left[0] = self.back[0]
        self.back[0] = buff
        self.moveFrontBack(self.upper, 'u')

    def moveD(self):
        buff = self.right[2]
        self.right[2] = self.front[2]
        self.front[2] = self.left[2]
        self.left[2] = self.back[2]
        self.back[2] = buff
        self.moveFront(self.down, 'd')

    def moveBackD(self):
        buff = self.right[2]
        self.right[2] = self.back[2]
        self.back[2] = self.left[2]
        self.left[2] = self.front[2]
        self.front[2] = buff
        self.moveFrontBack(self.down, 'd')

    def moveR(self):
        for i in range(3):
            buff = self.down[i][2]
            self.down[i][2] = self.back[2 - i][0]
            self.back[2 - i][0] = self.upper[i][2]
            self.upper[i][2] = self.front[i][2]
            self.front[i][2] = buff
        self.moveFront(self.right, 'r')

    def moveBackR(self):
        for i in range(3):
            buff = self.down[i][2]
            self.down[i][2] = self.front[i][2]
            self.front[i][2] = self.upper[i][2]
            self.upper[i][2] = self.back[2 - i][0]
            self.back[2 - i][0] = buff
        self.moveFrontBack(self.right, 'r')

    def moveL(self):
        for i in range(3):
            buff = self.down[i][0]
            self.down[i][0] = self.front[i][0]
            self.front[i][0] = self.upper[i][0]
            self.upper[i][0] = self.back[2 - i][2]
            self.back[2 - i][2] = buff
        self.moveFront(self.left, 'l')

    def moveBackL(self):
        for i in range(3):
            buff = self.down[i][0]
            self.down[i][0] = self.back[2 - i][2]
            self.back[2 - i][2] = self.upper[i][0]
            self.upper[i][0] = self.front[i][0]
            self.front[i][0] = buff
        self.moveFrontBack(self.left, 'l')

    def moveF(self):
        for i in range(3):
            buff = self.upper[2][2 - i]
            self.upper[2][2 - i] = self.left[i][2]
            self.left[i][2] = self.down[0][i]
            self.down[0][i] = self.right[2 - i][0]
            self.right[2 - i][0] = buff
        self.moveFront(self.front, 'f')

    def moveBackF(self):
        for i in range(3):
            buff = self.upper[2][i]
            self.upper[2][i] = self.right[i][0]
            self.right[i][0] = self.down[0][2 - i]
            self.down[0][2 - i] = self.left[2 - i][2]
            self.left[2 - i][2] = buff
        self.moveFrontBack(self.front, 'f')

    def moveB(self):
        for i in range(3):
            buff = self.upper[0][i]
            self.upper[0][i] = self.right[i][2]
            self.right[i][2] = self.down[2][2 - i]
            self.down[2][2 - i] = self.left[2 - i][0]
            self.left[2 - i][0] = buff
        self.moveFront(self.back, 'b')

    def moveBackB(self):
        for i in range(3):
            buff = self.upper[0][2 - i]
            self.upper[0][2 - i] = self.left[i][0]
            self.left[i][0] = self.down[2][i]
            self.down[2][i] = self.right[2 - i][2]
            self.right[2 - i][2] = buff
        self.moveFrontBack(self.back, 'b')

########  DOUBLE MOVEMENTS ########
    def moveDoubleF(self):
        self.moveF()
        self.moveF()

    def moveDoubleB(self):
        self.moveB()
        self.moveB()

    def moveDoubleD(self):
        self.moveD()
        self.moveD()

    def moveDoubleR(self):
        self.moveR()
        self.moveR()

    def moveDoubleL(self):
        self.moveL()
        self.moveL()

    def moveDoubleU(self):
        self.moveU()
        self.moveU()

########  MAIN FACE MOVEMENTS  ########
    def moveFront(self, front, face):
        buff = front[0][0]
        front[0][0] = front[2][0]
        front[2][0] = front[2][2]
        front[2][2] = front[0][2]
        front[0][2] = buff
        buff = front[0][1]
        front[0][1] = front[1][0]
        front[1][0] = front[2][1]
        front[2][1] = front[1][2]
        front[1][2] = buff
        if face == 'f':
            self.front = front
        elif face == 'u':
            self.upper = front
        elif face == 'd':
            self.down = front
        elif face == 'l':
            self.left = front
        elif face == 'r':
            self.rifaceht = front
        elif face == 'b':
            self.back = front

    def moveFrontBack(self, front, face):
        buff = front[0][0]
        front[0][0] = front[0][2]
        front[0][2] = front[2][2]
        front[2][2] = front[2][0]
        front[2][0] = buff
        buff = front[0][1]
        front[0][1] = front[1][2]
        front[1][2] = front[2][1]
        front[2][1] = front[1][0]
        front[1][0] = buff
        if face == 'f':
            self.front = front
        elif face == 'u':
            self.upper = front
        elif face == 'd':
            self.down = front
        elif face == 'l':
            self.left = front
        elif face == 'r':
            self.rifaceht = front
        elif face == 'b':
            self.back = front

########  PRINT METHODS  ########
    def printCubeColor(self):
        for row in range(3):
            print('\n')
            space = True
            for col in range(3):
                if space:
                    for i in range(3):
                        print('     ', end='')
                print(colored(' ███ ', self.beautifulWhite(self.upper[row][col])), end='')
                space = False
        for row in range(3):
            print('\n')
            for col in range(3):
                print(colored(' ███ ', self.beautifulWhite(self.left[row][col])), end='')
            for col in range(3):
                print(colored(' ███ ', self.beautifulWhite(self.front[row][col])), end='')
            for col in range(3):
                print(colored(' ███ ', self.beautifulWhite(self.right[row][col])), end='')
            for col in range(3):
                print(colored(' ███ ', self.beautifulWhite(self.back[row][col])), end='')
        for row in range(3):
            print('\n')
            space = True
            for col in range(3):
                if space:
                    for i in range(3):
                        print('     ', end='')
                print(colored(' ███ ', self.beautifulWhite(self.down[row][col])), end='')
                space = False
        print('\n')


    def printCubeText(self):
        for row in range(3):
            print('\n')
            space = True
            for col in range(3):
                if space:
                    for i in range(3):
                        print('            ', end='')
                print('[', self.switcher.get(self.upper[row][col]), ']', end=' ')
                space = False
        for row in range(3):
            print('\n')
            for col in range(3):
                print('[', self.switcher.get(self.left[row][col]), ']', end=' ')
            for col in range(3):
                print('[', self.switcher.get(self.front[row][col]), ']', end=' ')
            for col in range(3):
                print('[', self.switcher.get(self.right[row][col]), ']', end=' ')
            for col in range(3):
                print('[', self.switcher.get(self.back[row][col]), ']', end=' ')
        for row in range(3):
            print('\n')
            space = True
            for col in range(3):
                if space:
                    for i in range(3):
                        print('           ', end=' ')
                print('[', self.switcher.get(self.down[row][col]), ']', end=' ')
                space = False
        print('\n')

    def beautifulWhite (self, color):
        if color == "white":
            return "grey"
        return color

########  ALLOW TO CHECK IF CUBE IS DONE  ########

    def mathHash(self):
        hashObj = hashlib.md5()
        string = ""
        for i in range(3):
            for j in range(3):
                string = string + self.front[i][j]
                string = string + self.back[i][j]
                string = string + self.right[i][j]
                string = string + self.left[i][j]
                string = string + self.upper[i][j]
                string = string + self.down[i][j]
        hashObj.update(string.encode('utf-8'))
        self.hash = hashObj.hexdigest()