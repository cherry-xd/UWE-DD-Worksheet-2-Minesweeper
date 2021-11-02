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

    def openCell(self, row, col, grid):
        if self.open:
            return
        else:
            self.open = True
            nearCells = []
            for y in range(-1,2):
                if (col + y) < 0 or (col + y) > settings.gridSize - 1:
                    continue
                for x in range(-1,2):
                    if (row + x) < 0 or (row + x) > settings.gridSize - 1:
                        continue
                    nearCells.append(grid.grid[row + x][col + y])
            self.mines = 0
            for i, cell in enumerate(nearCells):
                if nearCells[i].isMine():
                    self.mines += 1

    def draw(self):
        if self.flag and not self.open:
            print('F', end = '')

        elif self.open:
            self.flag = False
            if self.mines > 0:
                print('{}'.format(self.mines), end = '')
            elif self.mines <= 0:
                print('-', end = '')
            if self.mine:
                print('#', end = '')
                
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