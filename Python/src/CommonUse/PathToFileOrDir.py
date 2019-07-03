from CommonUse import Log

import sys
import os


class Path:
    logger = Log.Log()
    
    RECURSIVE = False
    
    path = os.getcwd()
    
    filePathList = []
    
    
    def GetPaths(self):
        return self.filePathList
    
    
    def AddPath(self, path):
        self.logger.PrintDebug(path)
        
        self.filePathList.append(path)
    
    
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
            # If flag is set, check sub-directories
            elif self.RECURSIVE:
                self.HandleDirectory(file)
            else:
                pass
    
    
    def Run(self):
        # Is this path valid??
        if os.path.exists(self.path):
            self.logger.PrintDebug("The path given exists.")
                
            # Directory or file?
            if self.IsDirectory(self.path):
                self.logger.PrintDebug("The path given points to a directory.")
                self.logger.PrintDebug("The recursive flag " + ("was " if self.RECURSIVE else "was not ") + "set.")
                
                self.HandleDirectory(self.path)
            elif self.IsFile(self.path):
                self.logger.PrintDebug("The path given is to a file.")
                
                self.AddPath(self.path)
            else:
                pass
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
        path.Run()
    else:
        path.logger.Print("USAGE: \"py " + os.path.basename(__file__)  + " -p <path to file or directory> [-r]\" where -r is an optional flag on whether to iterate through subdirectories.")
        path.ParseArguments()
        path.Run()


# The 0th argument is the file name
if __name__ == "__main__":
    main(sys.argv[1:])