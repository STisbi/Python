import xml.etree.ElementTree as ET


#######################################################
# Name: Parse
#
# Description: Gets the tree structure
#                  and calls the other methods
#              Comment in/out the functions as needed
#
# Parameters:  The XML file
#######################################################
def Parse(script):
    tree = ET.parse(script)
    root = tree.getroot()
    
    #PrintTA(root)
    #Find(root)
    #Modify(tree)
    #EmbeddedNamespace(root)
    FullyNamespaced(root)
    

#######################################################
# Name: PrintTA
#
# Description: Prints all tags and attributes         
#
# Parameters:  The XML root
#######################################################
def PrintTA(root):
    print("\nPrintTA\n")
    
    for data in root:
        print("Data Tag: ", data.tag)
        print("Data Attribute: ", data.attrib)
        for country in data:
            print("Country Tag: ", country.tag)
            print("Country Attribute : ", country.attrib)


#######################################################
# Name: Find
#
# Description: Variations on finding parts of the XML
#
# Parameters:  The XML file
#######################################################
def Find(root):
    print("\nFind\n")
    
    # Iterate through all elements with tag country
    for country in root.iter('country'):
        print(country.attrib)
        
    # Iterate through all elements with tag neighbor
    for neighbor in root.iter('neighbor'):
        print(neighbor.attrib)
        
    # Find all country elements
    for country in root.findall('country'):
        
        # Gets the first child 'rank'
        rankT = country.find('rank').text
        
        # Gets the first child 'rank''s attribute
        rankA = country.find('rank').get('update')
        
        # .get prints the attribute
        name = country.get('name')
        
        print(name, rankA, rankT)
        

#######################################################
# Name: Modify
#
# Description: Modifies the XML file
#
# Parameters:  The XML tree
#######################################################
def Modify(tree):
        print("\nModify\n")
        
        root= tree.getroot()
        
        # Iterate through element rank
        for rank in root.iter("rank"):
            
            # Adds/Subs 999 from its value
            newRank = int(rank.text) + 999
            rank.text = str(newRank)
            
            # Haven't found documentation on what the params for .set are
            rank.set("update", "yes")
            
        tree.write("script.xml")
            

#######################################################
# Name: EmbeddedNamespace
#
# Description: Find but with a partially namespaced XML
#
# Parameters:  The XML root
#######################################################
def EmbeddedNamespace(root):
    print("EmbeddedNamespace\n")
    
    # Dictionary using the namespaces from the XML 
    namespace = {"fiction" : "http://characters.example.com",
                 "xlms" : "http://people.example.com"}
    
    for actor in root.findall("xlms:actor", namespace):
        name = actor.find("xlms:name", namespace)
        print(name.text)
        
        for character in actor.findall("fiction:character", namespace):
            print(character.text)

#######################################################
# Name: FullyNamespaced
#
# Description: Find but with a fully namespaced XML
#
# Parameters:  The XML root
#######################################################
def FullyNamespaced(root):
    print("FullyNamespaced\n")
    
    # Dictionary using the namespaces from the XML 
    namespace = {"actor" : "http://characters.example.com",
                 "xlms" : "http://people.example.com"}
    
    # actor has to be defined in the above dictionary
    for male in root.findall("actor:male", namespace):
        for name in male.findall("actor:name", namespace):
            print(name.text)



#######################################################
#                        MAIN                         #
#######################################################
def main():
    file = "XML Scripts\FullyNamespaced.xml"
    Parse(file)

if __name__ == "__main__":
    main()
