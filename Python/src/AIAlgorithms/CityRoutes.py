from CommonUse import ReadFromFile as rff

import os
import sys

class CityRoutes():
    util = rff.ReadFile()
    
    routes = []
    
    def __init__(self, path):
        self.util.Run(path)
        self.routes = self.util.GetStrList()
        

    def PrintRoutes(self):
        for route in self.routes:
            print(route)


#######################################################
#                        MAIN                         #
#######################################################
def main(argv):
    # The file is checked in ReadFromFile but double check
    if argv and os.path.isfile(argv[0]):
        routes = CityRoutes(argv[0])
        routes.PrintRoutes()
    else:
        print("No argument given.")
        

# The 0th argument is the file name
if __name__ == "__main__":
    main(sys.argv[1:])