import dbm.dumb

def run(myKeys,myValues,databaseName):

    print("Daniel Mendoza")

    db = dbm.open(databaseName, 'c')

    for i in range(len(myKeys)):
        db[myKeys[i]] = myValues[i]


#    for i in db:
#        print( i, db[i])

    db.close()
              
