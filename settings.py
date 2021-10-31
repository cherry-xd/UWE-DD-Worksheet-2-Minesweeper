from cells import Grid
import main

def settings():

    prompt = input("'G' = Grid Size, 'D' = Difficulty, 'B' = Back: ")
    
    if prompt == "G":
        size = input("Type desired grid size (default 5): ")
        try:
            if int(size) >= 2 and int(size) <= 8:
                Grid.setSize(int(size))
                print("Set grid size to {}".format(size))
                settings()
        except:
            print("Invalid grid size")
            settings()
            
    if prompt == "D":
        diff = input("'Easy', 'Medium', 'Hard' (default Medium): ")
        if diff == "Easy" or "Medium" or "Hard":
            print("Set difficulty to {}".format(diff))
            diffs = {"Easy" : 4.5, "Medium" : 4, "Hard" : 3.5}
            diffScale = diffs.get(diff)
            Grid.calcDiff(diffScale, diff)
            settings()
        else:
            print("Unrecognised difficulty")
            settings()
            
    if prompt == "B":
        main.main()

    else:
        print("Unrecognised command")
        settings()