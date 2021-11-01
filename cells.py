from settings import Settings
import random, string

settings = Settings()

def getSettings():
    return settings

class Cell:
    def __init__(self):
        self.open = False
        self.flag = False
        self.mine = False
        self.mines = -1

    def isMine(self):
        return self.mine

    def isFlagged(self):
        return self.flag

    def setFlag(self):
        if not self.open:
            self.flag = not self.flag

    def openCell(self):
        self.open = True
        
    def setMines(self, mines):
        self.mines = mines

    def draw(self):
        if self.mines != -1:
            print(self.mines, end = '')
        elif self.flag:
            print('F', end = '')
        else:
            print(' ', end = '')

class Grid:
    def __init__(self):
        self.grid = [[Cell() for i in range(settings.gridSize)] for i in range(settings.gridSize)]

    @staticmethod
    def randomCell():
        x = random.randint(0, settings.gridSize - 1)
        y = random.randint(0, settings.gridSize - 1)

        return x, y

    def draw(self):

        print('\n')
        alphabet_string = string.ascii_lowercase
        cols = list(alphabet_string)
        print('    ', end = '')
        for x in range(settings.gridSize):
            print(cols[x] + '   ', end = '')
        line = '----'
        print('\n  -' + (line * settings.gridSize))
        for y in range(settings.gridSize):
            print(cols[y], '| ', end = '')
            for x in range(settings.gridSize):
                self.grid[y][x].draw()
                print(' | ', end = '')
            print('\n  -' + (line * settings.gridSize))