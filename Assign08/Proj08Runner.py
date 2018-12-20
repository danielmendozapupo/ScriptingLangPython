def run(myListA, Char):
    print("Daniel Mendoza")
    print(Char)
    print(myListA)
    myListB = []
    for word in myListA:
        if Char not in word:
            myListB.append(word)
    return myListB