from CommonUse import PathToFileOrDir as PT
from CommonUse import Log

import os
import sys

class ChangeExt:
    logger = Log.Log()
    
    fromExt   = ""
    toExt     = ""
    recursive = False
    path      = os.getcwd()
        

    def ChangeFileExt(self):
        # Instantiate
        pathObj = PT.Path()
        
        # Set the variables
        pathObj.setPath(self.path)
        pathObj.setRecursive(self.recursive)
        
        # Run it
        pathObj.Dessiminate()
        
        for fileName in pathObj.GetPaths():
            # Find the position of the last '.'
            dotIndex = fileName.rfind(".")
            
            # Get this files extension without the dot
            fileExt = fileName[dotIndex + 1:]
            
            # Compare to what we're looking for
            if (fileExt == self.fromExt):
                # Create a temporary file without the dot or extension
                tempName = fileName[:dotIndex]
                
                # Add the new extension to it
                newName = tempName + "." + self.toExt
                
                # THE ACTUAL RENAMING IN THE SYSTEM
                os.rename(fileName, newName)
        
    
    def ShowHelp(self):
        print("Usage: python ChangeFileExtension.py -f <from extension without dot> -t <to extension without dot> [optional -p <path to file or directory>]")
        
    def GetInput(self):
        self.fromExt = input("Extension to change (without dot): ")
        self.toExt   = input("Extension to change to (without dot): ")
        self.path    = input("Optionally, specify the full path to a file or directory. Or press enter to use the current directory: ")
        
        self.path = self.path if self.path else os.getcwd() 
        
        self.ChangeFileExt()
        
        
    def SetFlags(self, argList):
        for index, args in enumerate(argList):
            if args == "-f":
                self.fromExt = argList[index + 1]
            elif args == "-t":
                self.toExt = argList[index + 1]
            elif args == "-p":
                self.path = argList[index + 1]
            elif args == "-r":
                self.recursive = True
            else:
                pass
        
    def ParseArgs(self, argList):
        numArgs = len(argList)
            
        if numArgs > 2:
            self.SetFlags(argList)
            self.ChangeFileExt()
        else:
            print("Too many arguments given")
        

def main(argv):
    ui = ChangeExt()
    
    if argv:
        ui.ParseArgs(argv)
    else:
        ui.ShowHelp()
        ui.GetInput()

if __name__ == '__main__':
    main(sys.argv[1:])