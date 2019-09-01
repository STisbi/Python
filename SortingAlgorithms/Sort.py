import abc

class Sort(metaclass=abc.ABCMeta):
    
    def __init__(self):
        pass    
    
    @abc.abstractmethod
    def sort(self, algorithm, array):
        print("abstract", algorithm)
            
        