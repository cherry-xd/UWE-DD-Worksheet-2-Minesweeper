from cells import Grid
from input import Input
import settings

def main():
    prompt = input("Type 'start' or 'settings': ") 
    if prompt == "settings":
        settings.settings()
        
    if prompt == "start":
        print("\nStarting game!\nGrid size: {}\nDifficulty: {}".format(Grid.size, Grid.difficulty))
        drawGame()

    else:
        print("Unrecognised command")
        main()

def drawGame():
    Grid.calcDiff()
    grid = Grid()
    grid.draw()

    prompt = input("Enter desired cell ({} mines left): ".format(Grid.minecount))
    print(prompt)
    dict = Input.read(prompt)

if __name__ == "__main__":
    main()
