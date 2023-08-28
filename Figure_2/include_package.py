
import os
import sys


class Welcome_party:

    def __init__(self) -> None:

        self.pth=os.path.dirname(os.getcwd())
        self.insertables= [x[0] for x in os.walk(self.pth) if x[1] != []]
        print(self.insertables)
        self.ignorables=['.git']


    def initialize(self):

        for insrt in self.insertables:
            for ignorant_to in self.ignorables:
                if ignorant_to not in insrt:
                    print(insrt)
                    sys.path.append(insrt)    
                    






    if __name__=='__main__':
        self.initialize()

