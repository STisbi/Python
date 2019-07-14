from CommonUse import ReadFromFile as rff

import os
import sys

class RouteData():
    fromCity = ""
    toCity   = ""
    distance = 0
    
    def __init__(self, fromCity = "", toCity = "", distance = 0):
        self.fromCity = fromCity
        self.toCity   = toCity
        self.distance = distance


class CityRoutes():
    util = rff.ReadFile()
    
    routeData = RouteData()
    
    pathToFile = ""
    
    routeMap = {}
    routes   = []
    
    def __init__(self, argList):
        self.ParseArgs(argList)
        
    
    def ParseArgs(self, argList):
        for index, arg in enumerate(argList):
            if arg == "-f":
                self.routeData.fromCity = argList[index + 1]
            elif arg == "-t":
                self.routeData.toCity = argList[index + 1]
            elif arg == "-p":
                self.pathToFile =  argList[index + 1]
            else:
                pass


    def ShowHelp(self):
        print("Usage: py " + os.path.basename(__file__) + " -f <from city> -t <to city> -p <path to file with routes>")


    def GetRoutesFromFile(self):
        self.util.Run(self.pathToFile)
        self.routes = self.util.GetStrList()
        
        # Remove end of input line
        del self.routes[len(self.routes) - 1]
        
        self.CreateRouteMap()
    
    
    def CreateRouteMap(self):
        for route in self.routes:
            key = tuple(route[:2])
            value = False
            self.routeMap[key] = value
        

    def PrintRoutes(self):
        for route in self.routes:
            print(route)
        
        print()
    
    
    def PrintRouteMap(self):
        for key in self.routeMap:
            print("Key:   ", key)
            print("Value: ", self.routeMap[key])
            
        print()
    
    
    def CheckForRoutes(self):
        self.CheckRoutes([self.routeData.fromCity])
    
    
    def CheckRoutes(self, currentCities):
        print("Checking for route from " + self.routeData.fromCity + " to " + self.routeData.toCity + " in " + str(currentCities))
        
        newCities = []
        
        for key in self.routeMap:
            if not self.routeMap[key]:
                if key[0] in currentCities:
                    newCities.append(key[1])
                    self.routeMap[key] = True
                elif key[1] in currentCities:
                    newCities.append(key[0])
                    self.routeMap[key] = True
        
        if self.routeData.toCity in newCities:
            print(newCities)
        else:
            self.CheckRoutes(newCities)
        
            
    def Run(self):
        if (self.routeData.fromCity == "") or (self.routeData.toCity == "") or (self.pathToFile == "") or not (os.path.isfile(self.pathToFile)):
            self.ShowHelp()
        else:
            self.GetRoutesFromFile()


#######################################################
#                        MAIN                         #
#######################################################
def main(argv):
    # The file is checked in ReadFromFile but double check
    if argv:
        routes = CityRoutes(argv)
        routes.Run()
        routes.PrintRoutes()
        routes.PrintRouteMap()
        routes.CheckForRoutes()
    else:
        print("No argument given.")
        

# The 0th argument is the file name
if __name__ == "__main__":
    main(sys.argv[1:])