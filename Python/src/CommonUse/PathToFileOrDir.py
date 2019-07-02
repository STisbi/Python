from CommonUse import PathData as PD
from CommonUse import Log

import sys
import os


class Path:
    logger = Log.Log()
    
    RECURSIVE = False
    
    path = ""
    pathList = []
    
    def AddPath(self, path):
        self.logger.PrintDebug(path)
        
        self.pathList.append(path)
    
    
    def GetPaths(self):
        return self.pathList
    
    
    def IsFile(self, path):
        return os.path.isfile(path)
    
    
    def IsDirectory(self, path):
        return os.path.isdir(path)
    
        
    def HandleDirectory(self, path):
        # Iterate through every item in this directory
        for fileName in os.listdir(path):
            # Use system independent way of adding file name to directory path
            file = os.path.join(path, fileName)
            
            # Make sure the file isn't this one currently running
            if self.IsFile(file) and fileName != os.path.basename(__file__):
                self.AddPath(file)
            # Are we checking sub-directories?
            elif self.RECURSIVE:
                self.HandleDirectory(file)
            else:
                pass
    
    
    def Dessiminate(self):
        # Is this path valid?
        if os.path.exists(self.path):
            self.logger.PrintDebug("The path given exists.")
                
            # Directory or file?
            if self.IsDirectory(self.path):
                self.logger.PrintDebug("The path given points to a directory.")
                self.logger.PrintDebug("The recursive flag " + ("was " if self.RECURSIVE else "was not ") + "set.")
                
                self.HandleDirectory(self.path)
            else:
                self.logger.PrintDebug("The path given is to a file.")
                
                self.GetPathToFile(self.path)
        # An invalid path was given
        else:
            self.logger.PrintDebug("The path given does not exist or is not valid.")
        
                
                
    def ParseArguments(self, argList = []):
        # Iterate through each argument
        for index, args in enumerate(argList):
            # The path flag
            if args == "-p":
                self.setPath(argList[index + 1])
            # The recursive flag
            elif args == "-r":
                self.setRecursive(True)
            # Ignore other flags or arguments
            else:
                pass
            
        # If no path was specified, use the current working directory
        if self.path == "":
            self.setPath(os.getcwd())
            self.logger.PrintDebug("No path specified, using \"" + self.path + "\" instead.")
            
    
    def setPath(self, path):
        self.path = path
        
        
    def setDebug(self, debug):
        self.DEBUG = debug
        
        
    def setRecursive(self, recursive):
        self.RECURSIVE = recursive
#######################################################
#                        MAIN                         #
#######################################################
def main(argv):
    path = Path()
    
    if argv:
        path.ParseArguments(argv)
        path.Dessiminate()
    else:
        path.logger.Print("USAGE: \"py " + os.path.basename(__file__)  + " -p <path to file or directory> [-r]\" where -r is an optional flag on whether to iterate through subdirectories.")
        path.ParseArguments()
        path.Dessiminate()


# The 0th argument is the file name
if __name__ == "__main__":
    main(sys.argv[1:])