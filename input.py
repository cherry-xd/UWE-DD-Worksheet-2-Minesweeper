from abc import abstractmethod

class Input:
    @abstractmethod
    def read(input):
        while True:
            try: 
                dict = {"row" : input[3], "col" : input[1], "row" : input[0]}
                print(dict)
                return dict
            except:
                print("Invalid input")
