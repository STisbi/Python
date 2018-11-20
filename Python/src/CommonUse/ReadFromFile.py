import sys
import re

#######################################################
#                        MAIN                         #
#######################################################
def main(argv):
    global edgeWeights
    
    if(not argv):
        print("No argument given.")

    else:
        print("File to open:", argv[0])
        
        file = open(argv[0], "r")
        
        edges = []
        regex = re.compile('[\W_]+')
        
        with open(argv[0]) as file:
            for line in file:
                string = regex.sub('', line)
                edges.append(list(string))
                
        print(edges)
                
        

        

    

    

# The 0th argument is the file name
if __name__ == "__main__":
    main(sys.argv[1:])