import cells ; from cells import Grid
from input import Input

## this is done this way to avoid a circular import, it works so i dont think i need any other solution right now
settings = cells.getSettings()

def main():
    prompt = input("\nType 'Play', 'Grid size', or 'Difficulty': ") 
    if prompt.lower() in {"play", "p"}:
        drawGame()

    elif prompt.lower() in {"grid size", "g", "gridsize", "s", "size"}:
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
            
    elif prompt.lower() in {"difficulty", "d", "diff"}:
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
    settings.calcDiff()
    grid = Grid()
    minecount = 0
    ## i thought about making this check to see if a mine is already present and then skip that cell if true but i like the randomness of this
    for i in range(settings.mines):
        x, y = grid.randomCell()
        cell = grid.grid[x][y]
        if not cell.isMine():
            cell.mine = True
            minecount += 1
    print("\nStarting game!\nGrid size: {}\nDifficulty: {}\nMines: {}\n(format for input: 'row' 'col' 'O = open, F = flag')\nEG. 'ado' opens row a, column d".format(settings.gridSize, settings.difficulty.capitalize(), minecount))
    grid.draw()
            
    while True:
        prompt = input("Enter desired cell: ")
        dict = Input.read(prompt)
        ## i do not need validation for < 0 as there is no letter which corresponds to 0 or < 0
        if dict["row"] > settings.gridSize or dict["col"] > settings.gridSize:
            print("Cell entered does not exist")
        else:
            cell = grid.grid[dict["row"]][dict["col"]]
            print(cell)
            if dict["action"].lower() == "o":
                cell.openCell()
                if cell.isMine():
                    grid.draw()
                    input("\nGAME OVER!!! type anything to return to the menu: ")
                    main()
                    return
                else: 
                    grid.draw()
            if dict["action"].lower() == "f":
                cell.setFlag()
                grid.draw()
            

def getSettings():
    return settings

if __name__ == "__main__":
    main()
