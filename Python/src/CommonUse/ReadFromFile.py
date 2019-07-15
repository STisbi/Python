import sys
import os
import re

class ReadFile:
    charList = []
    strList  = []
    
    regex    = re.compile('[\W_]+')
    
    path     = ""
    
    
    def ReadFile(self):
        file = open(self.path, "r")
        
        with open(self.path) as file:
            for line in file:
                self.AddLineByChar(line)
                self.AddLineByWord(line)
    
        
    def AddLineByChar(self, line):
        string = self.regex.sub(' ', line)
        self.charList.append(list(string))
        
                
    def AddLineByWord(self, line):
        self.strList.append(line.split())
        
        
    def GetCharList(self):
        return self.charList
    
    
    def GetStrList(self):
        return self.strList
    
    
    def ClearData(self):
        self.charList = []
        self.strList  = []
        self.path     = ""
        
    
    def Run(self, path):
        if os.path.isfile(path):
            self.path = path
            self.ReadFile()
        else:
            print(path + " is not a file.")
            
            
#######################################################
#                        MAIN                         #
#######################################################
def main(argv):
    if not argv:
        print("No argument given.")

    else:
        util = ReadFile()
        
        util.Run(argv[0])
        
        print(util.GetStrList())
        

# The 0th argument is the file name
if __name__ == "__main__":
    main(sys.argv[1:])