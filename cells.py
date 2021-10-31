import random
import string

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
    size = 5
    difficulty = "Medium"
    diffScale = 4
    minecount = round((size ^ 2) /  diffScale)
        
    def __init__(self):
        self.grid = [[Cell() for i in range(self.size)] for i in range(self.size)]
        
    def calcDiff():
        Grid.diffScale = Grid.diffScale
        Grid.difficulty = Grid.difficulty
        Grid.minecount = round((Grid.size ^ 2) /  Grid.diffScale)
        
    def setSize(size):
        Grid.size = size

    @staticmethod
    def randomCell():
        x = random.randint(0, Grid.size - 1)
        y = random.randint(0, Grid.size - 1)

        return x, y

    def draw(self):
        print('\n')
        alphabet_string = string.ascii_lowercase
        cols = list(alphabet_string)
        print('    ', end = '')
        for x in range(Grid.size):
            print(cols[x] + '   ', end = '')
        line = '----'
        print('\n  -' + (line * Grid.size))
        for y in range(Grid.size):
            print(cols[y], '| ', end = '')
            for x in range(Grid.size):
                self.grid[y][x].draw()
                print(' | ', end = '')
            print('\n  -' + (line * Grid.size))