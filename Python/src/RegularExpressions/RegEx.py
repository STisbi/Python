import re

def RegEx():
    print("RegEx")
    
    string = "Cats are not smarter or friendlier than dogs."
    
    # match starts the search from the beginning
    
    # "Ca" will be found because it starts the string
    matchObj = re.match("Cats are n", string)
    print("match: ", type(matchObj), len(matchObj.group()), matchObj.group())
    
    # "are" will not be found because it is in the middle 
    # of the string and not the beginning
    matchObj = re.match("are", string)
    # This will throw an error
    #print(len(matchObj.group()), matchObj.group())
    
    # search searches the entire string and returns the first found match
    matchObj = re.search("ie", string)
    
    # There is no group(1)
    print("search:", type(matchObj), len(matchObj.group()), matchObj.group(0))
    
    # findall returns a list of all found matches
    
    matchObj = re.findall("ar", string)
    print("find  :", type(matchObj), len(matchObj), matchObj)
    
    # sub does a find and and returns the replaced version in matchObj
    
    string = "This has a mistakx"
    
    matchObj = re.sub("x", "e", string)
    print("sub   :", type(matchObj), matchObj, string)
    
    
    
    

#######################################################
#                        MAIN                         #
#######################################################
def main():
    file = "..\TestFiles\FullyNamespaced.xml"
    RegEx()

if __name__ == "__main__":
    main()