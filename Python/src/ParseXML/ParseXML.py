import xml.etree.ElementTree as ET

def Parse(script):
    tree = ET.parse(script)
    root = tree.getroot()

    for child in root:
        gotStuff = DoStuff(str(child.text))
        print(gotStuff)


def DoStuff(text):
    stuff = text.split()

    # Go through the list
    for x in stuff:
        return x






#######################################################
#                        MAIN                         #
#######################################################
def main():
    file = "script.xml"
    Parse(file)

if __name__ == "__main__":
    main()
