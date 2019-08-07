import sys

class PosteriorProb():
    observations = []
    hypothesis   = []
    
    cherryProbs = []
    limeProbs   = []
    
    initProbCherry = 0
    initProbLime   = 0
    
    probOfCherry = 0
    probOfLime   = 0
    
    outputFile = None
    
    def __init__(self, observations = []):
        self.hypothesis = [.1, .2, .4, .2, .1]
        
        self.cherryProbs = [1.0, 0.75, 0.50, 0.25, 0.0]
        self.limeProbs   = [0.0, 0.25, 0.50, 0.75, 1.0] 
        
        self.initProbCherry = 0.5
        self.initProbLime   = 0.5
        
        self.probOfCherry = 0
        self.probOfLime   = 0 
        
        self.ParseCommandLine(observations)
        
        self.outputFile = open("result.txt","w")
        self.outputFile.write("Observation sequence Q: " + ', '.join(observations) + "\n")
        self.outputFile.write("Length of Q: " + str(len(self.observations)) + "\n")
        
    
    def ParseCommandLine(self, observations):
        for line in observations:
            for candy in line:
                self.observations.append(candy)
    
    
    def PrintObservations(self):
        print(self.observations)
    
    
    def ComputeInitialProbabilites(self, candy):
        probability = 0
        self.initProbCherry = 0
        self.initProbLime   = 0
        
        for index in range(0, len(self.hypothesis)):
            if candy == "C":
                probability += self.hypothesis[index] * self.cherryProbs[index]
            else:
                probability += self.hypothesis[index] * self.limeProbs[index]
        
        if candy == "C":
            self.initProbCherry = probability
            self.initProbLime   = 1 - probability
        else:
            self.initProbLime   = probability
            self.initProbCherry = 1 - probability
        
        
        self.WriteInitialProbability("{:.5}".format(self.initProbCherry), "{:.5}".format(self.initProbLime))
        
        print("Initial probabilities: %.5f %.5f" %(self.initProbCherry, self.initProbLime))
    
    def ComputeProbabilities(self):
        for candyIndex, candy in enumerate(self.observations):
            #self.ComputeInitialProbabilites(candy)
            self.WriteObservataion(candyIndex + 1, candy)
            
            for index in range(0, len(self.hypothesis)):
                if candy == "C":
                    self.hypothesis[index] = ((self.cherryProbs[index] * self.hypothesis[index]) / self.initProbCherry)    
                else:
                    self.hypothesis[index] = ((self.limeProbs[index]   * self.hypothesis[index]) / self.initProbLime)
    
                self.WriteHypothesisToFile(index + 1, "{:.5}".format(self.hypothesis[index]))
                print("Hypothesis: %.5f" %(self.hypothesis[index]))
            
            self.ComputeInitialProbabilites(candy)
        
            
    def WriteObservataion(self, index, candy):
        self.WriteToFile("\nAfter Observation {} = {}:\n\n".format(index, candy))
        
        
    def WriteInitialProbability(self, cherry, lime):
        self.WriteToFile("\nProbability that the next candy we pick will be C, given Q: {}\n".format(cherry))
        self.WriteToFile("Probability that the next candy we pick will be L, given Q: {}\n".format(lime))
    
    
    def WriteHypothesisToFile(self, index, hypothesis):
        self.WriteToFile("P(h{} | Q) = {}\n".format(index, hypothesis))
        
            
    def WriteToFile(self, output):  
        self.outputFile.writelines(output)
        
        
    
#######################################################
#                        MAIN                         #
#######################################################
def main(argv):
    if argv:
        postProb = PosteriorProb(argv)
        postProb.PrintObservations()
        postProb.ComputeProbabilities()
    else:
        print("No argument given.")
        

# The 0th argument is the file name
if __name__ == "__main__":
    main(sys.argv[1:])