from CommonUse import ReadFromFile as rff
import sys
from tensorflow.python.ops.gen_array_ops import const

class BayesianNetwork():
    util = rff.ReadFile()
    
    trainingData = []
    
    probability = {}
    
    def __init__(self, filePath):
        self.util.Run(filePath[0])
        self.trainingData = self.util.GetStrList()
        
        self.probability = {"A":0, "B":0, "C":0, "D":0, "AA":0, "AB":0, "AC":0, "BA":0, "BC":0, "BD":0, "CA":0, "CB":0, "CD":0, "DA":0, "DB":0, "DC":0, "ACD":0}
        
        self.CalculateProabilities()
        
    
    def PrintTrainingData(self):
        for line in self.trainingData:
            print(line)
        
    
    def PrintProabilities(self):
        for constant in self.probability:
            print("Probability of", constant, "is:", self.probability[constant])
                
            
    def CalculateProabilities(self):
        A = 0 
        B = 0
        C = 0
        D = 0
        AB = 0
        AC = 0
        AD = 0
        BA = 0
        BC = 0
        BD = 0
        CA = 0
        CB = 0
        CD = 0
        DA = 0
        DB = 0
        DC = 0
        ACD = 0
        
        
        
        total = len(self.trainingData)
        
        for line in self.trainingData:
            if int(line[0]) == 1:
                A += 1
                
                if int(line[1]) == 1:
                    AB += 1
                if int(line[2]) == 1:
                    AC += 1
                    if int(line[3]) == 0:
                        ACD += 1
                if int(line[3]) == 1:
                    AD += 1    
            if int(line[1]) == 1:
                B += 1
                
                if int(line[0]) == 1:
                    BA += 1
                if int(line[2]) == 1:
                    BC += 1
                if int(line[3]) == 1:
                    BD += 1
                    
            if int(line[2]) == 1:
                C += 1
                
                if int(line[0]) == 1:
                    CA += 1
                if int(line[1]) == 1:
                    CB += 1
                if int(line[3]) == 1:
                    CD += 1
                    
            if int(line[3]) == 1:
                D += 1
                
                if int(line[0]) == 1:
                    DA += 1
                if int(line[1]) == 1:
                    DB += 1
                if int(line[2]) == 1:
                    DC += 1
                
        self.probability["A"]  = A  / total
        self.probability["B"]  = B  / total
        self.probability["C"]  = C  / total
        self.probability["D"]  = D  / total
        self.probability["AB"] = AB / total
        self.probability["AC"] = AC / total
        self.probability["AD"] = AD / total
        self.probability["BA"] = BA / total
        self.probability["BC"] = BC / total
        self.probability["BD"] = BD / total
        self.probability["CA"] = CA / total
        self.probability["CB"] = CB / total
        self.probability["CD"] = CD / total
        self.probability["DA"] = DA / total
        self.probability["DB"] = DB / total
        self.probability["DC"] = DC / total
        self.probability["ACD"] = ACD / total
         
    
#######################################################
#                        MAIN                         #
#######################################################
def main(argv):
    if argv:
        bayNet = BayesianNetwork(argv)
        bayNet.PrintProabilities()
    else:
        print("No argument given.")
        

# The 0th argument is the file name
if __name__ == "__main__":
    main(sys.argv[1:])