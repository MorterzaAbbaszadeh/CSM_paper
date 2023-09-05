

from os import path,  getcwd, walk
from sys import path as sys_path


class Welcome_party:

    def __init__(self) -> None:

        self.pth=path.dirname(getcwd())
        self.insertables= [x[0] for x in walk(self.pth) if x[1] != []]
        self.ignorables=['.git']


    def initialize(self):

        for insert in self.insertables:
            for ignorant_to in self.ignorables:
                if ignorant_to not in insert:
                    print(insert)
                    sys_path.insert(1, insert)    
                    






    if __name__=='__main__':
        self.initialize()

