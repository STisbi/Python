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
    
    totalDistance  = 0
    nodesExpanded  = 0
    nodesGenerated = 0
    maxNodesInMem  = 0 
    
    fromCity      = ""
    toCity        = ""
    heuristicCity = ""
    
    pathToFile = ""
    pathToHeuristic = ""
    
    routeMap     = {}
    heuristicMap = {}
    
    routes     = []
    heuristics = []
    cityPaths  = []
    
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
            elif arg == "-h":
                self.pathToHeuristic = argList[index + 1]
            else:
                pass


    def ShowHelp(self):
        print("Usage: py " + os.path.basename(__file__) + " -f <from city> -t <to city> -p <path to file with routes>")


    def GetRoutesFromFile(self):
        self.util.Run(self.pathToFile)
        self.routes = self.util.GetStrList()
        
        if self.pathToHeuristic:
            self.util.ClearData()
            self.util.Run(self.pathToHeuristic)
            self.heuristics = self.util.GetStrList()
            
            # Remove end of input line
            del self.heuristics[len(self.heuristics) - 1]
            
            self.SetHeuristicCity()
            self.CreateHeuristicMap()
        
        # Remove end of input line
        del self.routes[len(self.routes) - 1]
        
        
        self.CreateRouteMap()
    
    
    def CreateRouteMap(self):
        for route in self.routes:
            key = tuple(route[:2])
            value = False
            self.routeMap[key] = value
            
    
    def CreateHeuristicMap(self):
        for city in self.heuristics:
            key = city[0]
            value = city[1]
            self.heuristicMap[key] = value
            
    
    def SetHeuristicCity(self):
        for value in self.heuristics:
            if int(value[1]) == 0:
                self.heuristicCity = value[0]
                
    
    def GetHeuristicCity(self):
        print(self.heuristicCity)
        

    def PrintRoutes(self):
        for route in self.routes:
            print(route)
        
        print()
    
    
    def PrintRouteMap(self):
        for key in self.routeMap:
            print("Key:   ", key)
            print("Value: ", self.routeMap[key])
            
        print()
    
    
    def PrintHeuristics(self):
        for value in self.heuristics:
            print(value)
            
        print()
    
    
    def PrintCities(self):
        for cities in self.cityPaths:
            print(cities)
    
    
    def GetRoute(self):
        printAllPaths = False
        
        optimalPath = []
        
        print("Route: ")
        
        for cities in self.cityPaths:
            if cities[0] == self.fromCity and cities[len(cities) - 1] == self.toCity:
                for index, path in enumerate(cities[:-1]):
                    for route in self.routes:
                        if cities[index] in route and cities[index + 1] in route:
                            print(cities[index] + " to " + cities[index + 1] + ": " + route[2] + " km")
                            self.totalDistance += int(route[2])
                
                if not printAllPaths:
                    break
                            
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
        print("Nodes Expanded: " + str(self.nodesExpanded))
            
    
    def GetMaxMemoryNodes(self):
        self.maxNodesInMem = len(self.cityPaths) - 1
        print("Max nodes in memory: " + str(self.maxNodesInMem))        
            
            
    def GetNodesGenerated(self):
        self.maxNodesInMem = len(self.cityPaths)
        
        print("Nodes Generated: " + str(self.maxNodesInMem))
    
    
    def PrintInfo(self):
        self.GetNodesExpanded()
        self.GetNodesGenerated()
        self.GetMaxMemoryNodes()
        self.GetRouteDistance()
        self.GetRoute()
    
    
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
        if self.heuristicCity:
            self.CheckRouteHeuristically([self.fromCity])
        else:
            self.CheckRoutes([self.fromCity])
    
    
    def CheckRoutes(self, currentCities):
#         print("Checking for route from " + self.fromCity + " to " + self.toCity + " in " + str(currentCities))
        
        fringe = []
        
        for key in self.routeMap:
            if not self.routeMap[key]:
                if key[0] in currentCities:
                    fringe.append(key[1])
                    
                    self.routeMap[key] = True
                    
                    self.AddCityToList(key[0], key[1])
                    
                    
                elif key[1] in currentCities:
                    fringe.append(key[0])
                    
                    self.routeMap[key] = True
                    
                    self.AddCityToList(key[1], key[0])
                    
        
        if not fringe:
            self.pathFound = False
        elif self.toCity not in fringe:
            self.nodesExpanded += len(fringe)
            self.CheckRoutes(fringe)
        else:
            self.pathFound = True
    
    
    def CheckForRouteHeuristically(self):
        self.CheckRouteHeuristically([self.fromCity])
        
    
    def CheckRouteHeuristically(self, currentCities):
#         print("Heuristic route from " + self.fromCity + " to " + self.toCity + " in " + str(currentCities))
        
        fringe = []
        
        for city in currentCities:
            for pair in self.routes:
                if city == pair[0]:
                    fringe.append(pair[1])
                    
                    self.AddCityToList(city, pair[1])
                    
                    if pair[1] == self.toCity:
                        self.pathFound = True
                        break
                    
                elif city == pair[1]:
                    fringe.append(pair[0])
                    
                    self.AddCityToList(city, pair[0])
                    
                    if pair[0] == self.toCity:
                        self.pathFound = True
                        break
            
            if self.pathFound:
                break
            
        if not self.pathFound:
            self.nodesExpanded += len(fringe)
            self.CheckRouteHeuristically(self.SortFringe(fringe))
            
            
    def SortFringe(self, fringe):
        sortedFringe = []
        
        for fCity in fringe:
            for value in self.heuristicMap:
                if fCity == value:
                    if sortedFringe:
                        for hCity in sortedFringe:
                            if int(self.heuristicMap[fCity]) == int(self.heuristicMap[hCity]):
                                sortedFringe.insert(1, fCity)
                                break
                            elif int(self.heuristicMap[fCity]) < int(self.heuristicMap[hCity]):
                                sortedFringe.insert(0, fCity)
                                break
                    else:
                        sortedFringe.append(fCity)
                    
                    break
        
        return sortedFringe
        
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
#         routes.PrintRoutes()
#         routes.PrintHeuristics()
        routes.CheckForRoutes()
        routes.PrintInfo()
    else:
        print("No argument given.")
        

# The 0th argument is the file name
if __name__ == "__main__":
    main(sys.argv[1:])