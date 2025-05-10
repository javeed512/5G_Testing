

def  mydb_decorator(f1):

    def  wrapper():
        print('Database  connection establised successfully..')#mysql db logic
        f1()
    return wrapper




@mydb_decorator
def  updateData():
    i=0
    i=i+1
    print(i)
    print('Data updated in DB')


updateData()    


@mydb_decorator
def  insertData():
    print('inserting data')


insertData()