# TODO: Implement me as Singleton
# https://stackoverflow.com/questions/6760685/creating-a-singleton-in-python


class Printer(object):
    DEBUG = False
    
    def Print(self, *arguments, newLine = True):
        for string in arguments:
            if newLine:
                print(string)
            else:
                print(string, end=' ', flush=True)
    
    
    def PrintDebug(self, *arguments, newLine = True):
        if self.DEBUG:
            for string in arguments:
                if newLine:
                    print(string)
                else:
                    print(string, end=' ', flush=True)
                    
                    
    def PrintNewLine(self):
        print()
        