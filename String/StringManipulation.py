class StringManipulation:
    def __init__(self):
        self.string1 = "Hello there python!"
        self.string2 = "How are you?"
        self.sting3 = "Hello there!, this is my new string. \nI feel good Learning python:)"

    def concatination(self):
        print(self.string1+" "+self.string2)

    def stringSplit(self,by=None):
        print(self.sting3.split(by))

    def reverse(self):
        reverse = ''
        for char in self.string1:
            reverse = char + reverse
        print(reverse)

stringmanipulation = StringManipulation()
stringmanipulation.concatination()
# split() no parameter split the string and remove \n,\t etc.,
stringmanipulation.stringSplit()
stringmanipulation.stringSplit(',')
stringmanipulation.stringSplit('\n')
# reverse the string
stringmanipulation.reverse()