# TODO: Implement me as Singleton
# https://stackoverflow.com/questions/6760685/creating-a-singleton-in-python


class Log(object):
    DEBUG = True
    
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
        