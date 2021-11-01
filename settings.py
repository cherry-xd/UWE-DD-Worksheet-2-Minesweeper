class Settings:
    def __init__(self):
        self.diffs = {"easy" : 4.1, "medium" : 3.75, "hard" : 3.15, "hidden" : 2.5}
        self.gridSize = 7
        self.difficulty = "medium"

    def calcDiff(self):
        self.diffScale = self.diffs.get(self.difficulty)
        self.minecount = round((self.gridSize ** 2) / self.diffScale)