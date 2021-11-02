class Settings:
    def __init__(self):
        ## i did this for easy expandability, i'm also considering using json files to store these settings more permanently
        self.diffs = {"easy" : 4, "medium" : 3.65, "hard" : 3, "hidden" : 2.15}
        self.gridSize = 7
        self.difficulty = "medium"

    def calcDiff(self):
        self.diffScale = self.diffs[self.difficulty]
        self.mines = round((self.gridSize ** 2) / self.diffScale)