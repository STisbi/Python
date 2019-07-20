from CommonUse import ReadFromFile as rff
from CommonUse import Printer

import os
import sys

class City():
    cityName = ""
    connections = []
    
    
    def __init__(self, cityName = ""):
        self.cityName    = cityName
        self.connections = []


class CityRoutes():
    util = rff.ReadFile()
    printer = Printer.Printer()
    
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
    
    cities     = []
    routes     = []
    heuristics = []
    cityPaths  = []
    
    def __init__(self, argList):
        self.ParseArgs(argList)
        
        self.printer.DEBUG = False
        
    
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
        self.printer.Print("Usage: <python command> " + os.path.basename(__file__) + " -f <from city> -t <to city> -p <path to file with routes> [-h <path to heuristic file>]")


    def GetRoutesFromFile(self):
        self.util.Run(self.pathToFile)
        self.routes = self.util.GetStrList()
        
        # If a heuristic file was given, parse it as well
        if self.pathToHeuristic:
            # Clear out data route path data first
            self.util.ClearData()
            self.util.Run(self.pathToHeuristic)
            self.heuristics = self.util.GetStrList()
            
            
            self.SetHeuristicCity(self.FindHeuristicCity())
            self.CreateHeuristicMap()
        
        
        self.SetUniqueCities()
        self.SetCityConnections()
        self.CreateRouteMap()
    
    
    def SetUniqueCities(self):
        # Iterate through every pair of cities
        for cityPair in self.routes:
            # If there are cities already in the unique cities list (i.e. the first iteration)
            if self.cities:
                uniqueCity0 = True
                uniqueCity1 = True
                
                # Check if these two cities are unique
                for city in self.cities:
                    if cityPair[0] == city.cityName:
                        uniqueCity0 = False
                    if cityPair[1] == city.cityName:
                        uniqueCity1 = False
                
                # Add the unique city
                if uniqueCity0:
                    self.cities.append(City(cityPair[0]))
                if uniqueCity1:
                    self.cities.append(City(cityPair[1]))
            else:
                # If for whatever reason they are the same, add just one
                if cityPair[0] == cityPair[1]:
                    self.cities.append(City(cityPair[0]))
                else:
                    self.cities.append(City(cityPair[0]))
                    self.cities.append(City(cityPair[1]))
    
    
    def SetCityConnections(self):
        # Iterate through every unique city
        for city in self.cities:
            # Then for each route
            for cityPair in self.routes:
                # If that unique city is in a route
                if city.cityName == cityPair[0]:
                    # Add the city it goes to and the distance
                    city.connections.append([cityPair[1], cityPair[2]])
                if city.cityName == cityPair[1]:
                    # Add the city it goes to and the distance
                    city.connections.append([cityPair[0], cityPair[2]])
                    
    
    
    def CreateRouteMap(self):
        for route in self.routes:
            key = tuple(route[:3])
            value = False
            self.routeMap[key] = value
            
    
    def CreateHeuristicMap(self):
        for city in self.heuristics:
            key = city[0]
            value = city[1]
            self.heuristicMap[key] = value
            
    
    def FindHeuristicCity(self):
        for value in self.heuristics:
            if int(value[1]) == 0:
                return value[0]
            
            
    def SetHeuristicCity(self, city):
        self.heuristicCity = city
                
    
    def GetHeuristicCity(self):
        return self.heuristicCity
        

    def PrintRoutes(self):
        for route in self.routes:
            self.printer.Print(route)
        
        self.printer.PrintNewLine()
    
    
    def PrintUniqueCities(self):
        for index, city in enumerate(self.cities):
            self.printer.Print("City " + str(index + 1) + ": " + city.cityName + " goes to: ", newLine=False)
            
            for connectingCity in city.connections:
                self.printer.Print(connectingCity[0] + "(" + connectingCity[1] + ") ", newLine=False)
            
            self.printer.PrintNewLine()
            
        self.printer.PrintNewLine()
    
    
    def PrintRouteMap(self):
        for key in self.routeMap:
            self.printer.Print("Key:   ", key)
            self.printer.Print("Value: ", self.routeMap[key])
            
        self.printer.PrintNewLine()
    
    
    def PrintHeuristics(self):
        for value in self.heuristics:
            self.printer.Print(value)
            
        self.printer.PrintNewLine()
        
    
    def PrintHeuristicMap(self):
        for key in self.heuristicMap:
            self.printer.Print("Key:   " + key)
            self.printer.Print("Value: " + self.heuristicMap[key])
            
        self.printer.PrintNewLine()
    
    
    def PrintCityPaths(self):
        for cities in self.cityPaths:
            self.printer.Print(cities)
    
    
    def PrintRoute(self):
        printAllPaths = False
        
        self.printer.Print("Route: ")
        
        for cities in self.cityPaths:
            if cities[0] == self.fromCity and cities[len(cities) - 1] == self.toCity:
                for index, path in enumerate(cities[:-1]):
                    for route in self.routes:
                        if cities[index] in route and cities[index + 1] in route:
                            self.printer.Print(cities[index] + " to " + cities[index + 1] + ": " + route[2] + " km")
                
                if not printAllPaths:
                    break
                 
        if not self.pathFound:
            self.printer.Print("none")
    
    
    def PrintRouteDistance(self):
        printAllPaths = False
        
        for cities in self.cityPaths:
            if cities[0] == self.fromCity and cities[len(cities) - 1] == self.toCity:
                for index, path in enumerate(cities[:-1]):
                    for route in self.routes:
                        if cities[index] in route and cities[index + 1] in route:
                            self.totalDistance += int(route[2])
                
                if not printAllPaths:
                    break
                 
        if not self.pathFound:
            self.printer.Print("none")
                            
        self.printer.Print("Distance: ", newLine=False)
    
        if self.pathFound:
            self.printer.Print(str(self.totalDistance))
        else:
            self.printer.Print("infinity")
    
    
    def PrintNodesExpanded(self):
        self.printer.Print("Nodes Expanded: " + str(self.nodesExpanded))
            
    
    def PrintMaxMemoryNodes(self):
        self.maxNodesInMem = len(self.cityPaths) - 1
        
        self.printer.Print("Max nodes in memory: " + str(self.maxNodesInMem))        
            
            
    def PrintNodesGenerated(self):
        self.maxNodesInMem = len(self.cityPaths)
        
        self.printer.Print("Nodes Generated: " + str(self.maxNodesInMem))
    
    
    def PrintInfo(self):
        self.PrintRoutes()
        self.PrintHeuristics()
        self.PrintUniqueCities()
        self.PrintNodesExpanded()
        self.PrintNodesGenerated()
        self.PrintMaxMemoryNodes()
        self.PrintRouteDistance()
        self.PrintRoute()
    
    
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
        self.printer.PrintDebug("Checking for route from " + self.fromCity + " to " + self.toCity + " in " + str(currentCities))
        
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
        self.printer.PrintDebug("Heuristic route from " + self.fromCity + " to " + self.toCity + " in " + str(currentCities))
        
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
        routes.CheckForRoutes()
        routes.PrintInfo()
    else:
        print("No argument given.")
        

# The 0th argument is the file name
if __name__ == "__main__":
    main(sys.argv[1:])