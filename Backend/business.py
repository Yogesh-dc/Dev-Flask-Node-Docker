def getdata():
    with open('test.txt', 'r') as file:
        data = file.read()
        data=data.split()
        
    return {"data": data}