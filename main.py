import cells ; from cells import Grid
from input import Input
from settings import Settings

settings = cells.getSettings()

def main():
    prompt = input("Type 'Play', 'Grid size', or 'Difficulty': ") 
    if prompt.lower() in {"play", "p"}:
        drawGame()
        return
    
    if prompt.lower() in {"grid size", "g", "gridsize", "s", "size"}:
        while True:
            size = input("Type desired grid size (current {}): ".format(settings.gridSize))
            try:
                if int(size) >= 4 and int(size) <= 10:
                    settings.gridSize = int(size)
                    print("Set grid size to {}".format(settings.gridSize))
                    return main()
                else:
                    print("Invalid grid size")
            except:
                print("Invalid grid size")
            
    if prompt.lower() in {"difficulty", "d", "diff"}:
        while True:
            difficulty = input("'Easy', 'Medium', 'Hard' (current {}): ".format(settings.difficulty.capitalize()))
            if difficulty.lower() in settings.diffs.keys():
                settings.difficulty = difficulty
                print("Set difficulty to {}".format(settings.difficulty.capitalize()))
                return main()
            else:
                print("Unrecognised difficulty")

    else:
        print("Unrecognised command")
        main()

def drawGame():
    print("\nStarting game!\nGrid size: {}\nDifficulty: {}".format(settings.gridSize, settings.difficulty.capitalize()))
    grid = Grid()
    grid.draw()
    settings.calcDiff()

    prompt = input("Enter desired cell ({} mines left): ".format(settings.minecount))
    print(prompt)
    dict = Input.read(prompt)

def getSettings():
    return settings

if __name__ == "__main__":
    main()
