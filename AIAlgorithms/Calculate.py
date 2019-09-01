from CommonUse import ReadFromFile as rff
import string as String
import sys
import math


class Calculate():
    ASCII_A   = 65
            
    numVarComb = 0
    
    util = rff.ReadFile()
    
    pathToFile = None
    
    variables    = []
    trainingData = []
    
    charProbability  = {}
    tupleProbability = {}
    
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
    
            
    def PrintProbabilities(self, useTuple = True):
        GAP = 1
        
        if useTuple:
            length = len(self.variables)
            for key in self.tupleProbability:
                x = length - len(key) + GAP
                print("Key: {0:1} {1:1} Value: {2:1}".format(" ".join(map(str, key)), " ".join([" "] * x), self.tupleProbability[key]))
        else:
            for key in self.charProbability:
                print("Key: {0:5} Value: {1:0}".format(key, self.charProbability[key]))
    
    
    def SetVariables(self):
        self.variables = list(String.ascii_uppercase)[0:self.util.GetNumStrColm()]
        
        
    def GetNumComb(self):
        if self.numVarComb == 0:
            self.CalcNumVarComb()
        
        return int(self.numVarComb)
        
        
    def CalcNumVarComb(self):
        n = len(self.variables)
        numerator = math.factorial(n)
        
        for k in range(0, n):
            denominator = math.factorial(k) * math.factorial(n - k)
            self.numVarComb += numerator / denominator
            
            
    def KeyToTuple(self):
        for key in self.charProbability:
            tempList  = []
            for charc in key:
                tempList.append(ord(charc) - self.ASCII_A)
                
            self.tupleProbability[tuple(tempList)] = 0
        
    
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
            
        self.charProbability[self.variables[len(self.variables) - 1]] = 0
            
    
    # This method adds one variable to the root and then recursively
    # calls itself until the index parameter matches the length of the
    # total number of variable available. See description for 
    # CalcInitialProbabilities
    def AddToRoot(self, root, start):
        if start == len(self.variables):
            pass
        else:
            if root not in self.charProbability:
                    self.charProbability[root] = 0
                    
            for varIndex in range(start, len(self.variables)):
                key = root + self.variables[varIndex]
                if key not in self.charProbability:
                    self.charProbability[key] = 0
                    self.AddToRoot(key, varIndex + 1)
                        
    
            
    def CalculateProbabilities(self):
        # Builds the combinations and initializes them to 0
        self.CalcInitialProbabilities()
        
        # Convert the alphabetical keys to numerical
        self.KeyToTuple()
        
        numRows = 0
        
        for rowIndex in range(0,len(self.trainingData)):
            numRows += 1
            for key in self.tupleProbability:
                match = True
                # Check if all elements in the key are in that row
                for index in key:
                    if self.trainingData[rowIndex][index] != 1:
                        match = False
                        break
            
                if match:
                    self.tupleProbability[key] += 1
                    
        values = []
        
        # Determine the probabilities and add it to both dictionaries
        for index, key in enumerate(self.tupleProbability):
            values.append(self.tupleProbability[key] / numRows)
            self.tupleProbability[key] = values[index]
            
        for index, key in enumerate(self.charProbability):
            self.charProbability[key] = values[index]
                
            
    
#######################################################
#                        MAIN                         #
#######################################################
def main(argv):
    if argv:
        calc = Calculate(argv)
        calc.PrintProbabilities()
    else:
        print("No argument given.")
        

# The 0th argument is the file name
if __name__ == "__main__":
    main(sys.argv[1:])