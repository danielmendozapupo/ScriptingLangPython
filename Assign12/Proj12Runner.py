import dbm.dumb

def run(databaseName):

    print('Daniel Mendoza')

    db = dbm.open(databaseName, 'c')

    myKeys = b'name',b'age',b'gender'
    myValues = b'Joe',b'39',b'male'
    
    
    for i in range(len(myKeys)):
        db[myKeys[i]] = myValues[i]

    db.close()
            
    
    

