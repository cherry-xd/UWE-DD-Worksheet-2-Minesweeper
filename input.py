from abc import abstractmethod

class Input:
    @abstractmethod
    def read(input):
        try:
            ## this ord() method is converting the letters of the grid coordinates into numbers so they can be actually used
            rowNum = ord(input[0]) - 97
            colNum = ord(input[1]) - 97
            dict = {"row" : rowNum, "col" : colNum, "action" : input[2]}
            return dict
        except:
            print("Invalid input")
            return
