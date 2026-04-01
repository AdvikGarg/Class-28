class IOString:
    
    def __init__(self):
        self.str1=""
        
    def getstring(self):
        self.str1=input('Enter a string: ')
        
    def printstring(self):
        print("Result is: ", self.str1.upper())

ob=IOString()
ob.getstring()
ob.printstring()
        
            