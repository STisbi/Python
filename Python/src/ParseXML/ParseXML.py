import xml.etree.ElementTree as ET


#######################################################
# Description: Gets the tree structure
#                  and calls the other methods
#              Comment in/out the functions as needed
#
# Parameters:  The XML file
#######################################################
def Parse(script):
    tree = ET.parse(script)
    root = tree.getroot()
    
    PrintTA(root)
    Find(root)
    

#######################################################
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
        rank = country.find('rank').text
        
        # .get prints the attribute
        name = country.get('name')
        
        print(name, rank)
        


#######################################################
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
#                        MAIN                         #
#######################################################
def main():
    file = "script.xml"
    Parse(file)

if __name__ == "__main__":
    main()
