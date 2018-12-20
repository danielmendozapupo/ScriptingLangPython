import re
def run(myTuple, myWord):
    print("Daniel Mendoza")
    print(myWord)
    print(myTuple)
    #resulTuple = re.compile(myWord)
    Str = filter(lambda x: re.search(myWord, x), myTuple)
    return Str
