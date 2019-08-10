from CommonUse import ReadFromFile as rff
import string as String
import sys
import math


class Calculate():
    numCombinations = 0
    
    util = rff.ReadFile()
    
    pathToFile = None
    
    variables    = []
    trainingData = []
    
    probability = {}
    
    def __init__(self, argList):
        self.ParseArguments(argList)
        
        self.util.Run(self.pathToFile)
        self.trainingData = self.util.GetTypeStrList()
        
        if self.util.IsStrListNumerical():
            self.SetVariables()
            self.CalculateProbabilities()
        else:
            print("The training data contained non-numerical values.")
            
            
    def ParseArguments(self, argList):
        for index, arg in enumerate(argList):
            if arg == "-p":
                self.pathToFile = argList[index + 1]
    
    
    def PrintTrainingData(self):
        for row in self.trainingData:
            print(row)
    
    
    def PrintVariables(self):
        print(self.variables)
    
            
    def PrintInitialProbabilities(self):
        for key in self.probability:
            print("Key: {0:5} Value: {1:0}".format(key, self.probability[key]))
    
    
    def SetVariables(self):
        self.variables = list(String.ascii_uppercase)[0:self.util.GetNumStrColm()]
        
        
    def GetNumComb(self):
        if self.numCombinations == 0:
            self.CalcNumVarComb()
        
        return int(self.numCombinations)
        
        
    def CalcNumVarComb(self):
        n = len(self.variables)
        numerator = math.factorial(n)
        for k in range(0, n):
            denominator = math.factorial(k) * math.factorial(n - k)
            self.numCombinations += numerator / denominator
        
    
    # This method in combination with the AddToRoot method
    # builds a tree from each of the variables in the list
    # and adds each node as it grows. It builds the tree
    # in a depth first recursive manner.
    #
    # Ex: A -> AB -> ABC -> ABCD
    #                ABD
    #          AC -> ACD
    #          AD                                                       
    
    def CalcInitialProbabilities(self):
        for index, variable in enumerate(self.variables):
            self.AddToRoot(variable, index + 1)
            
        self.probability[self.variables[len(self.variables) - 1]] = 0
            
    
    # This method adds one variable to the root and then recursively
    # calls itself until the index parameter matches the length of the
    # total number of variable available. See description for 
    # CalcInitialProbabilities
    def AddToRoot(self, root, start):
        if start == len(self.variables):
            pass
        else:
            if root not in self.probability:
                    self.probability[root] = 0
                    
            for varIndex in range(start, len(self.variables)):
                key = root + self.variables[varIndex]
                if key not in self.probability:
                    self.probability[key] = 0
                    self.AddToRoot(key, varIndex + 1)
                        
    
            
    def CalculateProbabilities(self):
        self.CalcInitialProbabilities()
    
#######################################################
#                        MAIN                         #
#######################################################
def main(argv):
    if argv:
        calc = Calculate(argv)
        calc.PrintInitialProbabilities()
    else:
        print("No argument given.")
        

# The 0th argument is the file name
if __name__ == "__main__":
    main(sys.argv[1:])