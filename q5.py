class String:
    def __init__(self):

        self.user = " "

    def getString(self):
        self.user = input("Enter a string: ")

    def printString(self):
        print(self.user.upper())

# Test the class methods
String1 = String()
String1.getString()
String1.printString()
