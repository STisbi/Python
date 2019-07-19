from CommonUse import PathToFileOrDir as PT
from CommonUse import Printer

import os
import sys

class ChangeExt:
    logger = Printer.Printer()
    
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
        pathObj.Run()
        
        extChanged = False
        
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
                
                extChanged = True
                self.logger.Print("Changing \"" + fileName + "\" to \"" + newName + "\"")
        
        if not extChanged:
            self.logger.Print("No extensions were changed at " + self.path)
        
    
    def ShowHelp(self):
        self.logger.Print("Usage: py " + os.path.basename(__file__) + " -f <from extension without dot> -t <to extension without dot> [optional -p <path to file or directory>]")
        
    
    # Bold assumptions made here that the next argument after a flag is value for that flag
    def ParseArgs(self, argList):
        # Iterate through the argument list
        for index, args in enumerate(argList):
            # The from flag
            if args == "-f":
                self.fromExt = argList[index + 1]
            # The to flag
            elif args == "-t":
                self.toExt = argList[index + 1]
            # The path flag, defaults to the current working directory
            elif args == "-p":
                self.path = argList[index + 1]
            # Iterate through sub-directories?
            elif args == "-r":
                self.recursive = True
            else:
                pass
            
    def Run(self):
        # Proceed only if the flags were set
        if self.fromExt and self.toExt:
            self.ChangeFileExt()
        else:
            self.logger.Print("No flags were set, see usage.")
            self.ShowHelp()
        

def main(argv):
    ui = ChangeExt()
    
    if argv:
        ui.ParseArgs(argv)
        ui.Run()
    else:
        ui.ShowHelp()

if __name__ == '__main__':
    main(sys.argv[1:])