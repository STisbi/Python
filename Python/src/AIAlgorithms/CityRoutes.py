from CommonUse import ReadFromFile as rff

import os
import sys

class City():
    cityName = ""
    goesTo   = ""
    
    
    def __init__(self, cityName = "", goesTo = ""):
        self.cityName = cityName
        self.goesTo   = goesTo


class CityRoutes():
    util = rff.ReadFile()
    
    pathFound = False
    totalDistance = 0 
    
    fromCity = ""
    toCity   = ""
    
    pathToFile = ""
    
    routeMap  = {}
    routes    = []
    cityPaths = []
    
    def __init__(self, argList):
        self.ParseArgs(argList)
        
    
    def ParseArgs(self, argList):
        for index, arg in enumerate(argList):
            if arg == "-f":
                self.fromCity = argList[index + 1]
            elif arg == "-t":
                self.toCity = argList[index + 1]
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
    
    
    def PrintCities(self):
        for cities in self.cityPaths:
            print(cities)
    
    
    def AddCityToList(self, cityName, goesTo):
        if not self.cityPaths:
            self.cityPaths.append([cityName, goesTo])
        else:
            for cities in self.cityPaths:
                if cities[len(cities) - 1] == cityName:
                    newPath = cities
                    newPath.append(goesTo)
                    self.cityPaths.append(newPath)
                    break
                elif cities[len(cities) - 2] == cityName:
                    newPath = cities[:-1]
                    newPath.append(goesTo)
                    self.cityPaths.append(newPath)
                    break
        
    
    
    def CheckForRoutes(self):
        self.CheckRoutes([self.fromCity])
    
    
    def CheckRoutes(self, currentCities):
        #print("Checking for route from " + self.fromCity + " to " + self.toCity + " in " + str(currentCities))
        
        newCities = []
        
        for key in self.routeMap:
            if not self.routeMap[key]:
                if key[0] in currentCities:
                    newCities.append(key[1])
                    
                    self.routeMap[key] = True
                    
                    self.AddCityToList(key[0], key[1])
                    
                    
                elif key[1] in currentCities:
                    newCities.append(key[0])
                    
                    self.routeMap[key] = True
                    
                    self.AddCityToList(key[1], key[0])
        
        if not newCities:
            self.pathFound = False
        elif self.toCity not in newCities:
            self.CheckRoutes(newCities)
        else:
            self.pathFound = True
    
    
    def GetRoute(self):
        print("Route: ")
        
        for cities in self.cityPaths:
            if cities[0] == self.fromCity and cities[len(cities) - 1] == self.toCity:
                for index, path in enumerate(cities[:-1]):
                    for route in self.routes:
                        if cities[index] in route and cities[index + 1] in route:
                            print(cities[index] + " to " + cities[index + 1] + ": " + route[2] + " km")
                            self.totalDistance += int(route[2])
                            
        if not self.pathFound:
            print("none")
    
    def GetRouteDistance(self):
        distance = 0
        
        for cities in self.cityPaths:
            if cities[0] == self.fromCity and cities[len(cities) - 1] == self.toCity:
                for index, path in enumerate(cities[:-1]):
                    for route in self.routes:
                        if cities[index] in route and cities[index + 1] in route:
                            distance += int(route[2])
                            
        print("Distance: ", end='', flush=True)
    
        if self.pathFound:
            print(str(distance))
        else:
            print("infinity")
    
    
    
    def GetNodesExpanded(self):
        print("Nodes Expanded: ", end='', flush=True)
    
        if self.pathFound:
            print(str(len(self.cityPaths) + 1))
        else:
            print()
            
    
    def GetMaxMemoryNodes(self):
        print("Max nodes in memory: ", end='', flush=True)
    
        if self.pathFound:
            print(str(len(self.cityPaths) + 1))
        else:
            print()        
            
            
    def GetNodesGenerated(self):
        print("Nodes Generated: ", end = '', flush=True)
        
        if self.pathFound:
            print(str(len(self.cityPaths) + 1))
        else:
            print()
    
    
    def PrintInfo(self):
        self.GetNodesExpanded()
        self.GetNodesGenerated()
        self.GetMaxMemoryNodes()
        self.GetRouteDistance()
        self.GetRoute()
        
        
    def Run(self):
        if (self.fromCity == "") or (self.toCity == "") or (self.pathToFile == "") or not (os.path.isfile(self.pathToFile)):
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
        #routes.PrintRoutes()
        routes.CheckForRoutes()
        routes.PrintInfo()
    else:
        print("No argument given.")
        

# The 0th argument is the file name
if __name__ == "__main__":
    main(sys.argv[1:])