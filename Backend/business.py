import os

def getdata():
    filepath = os.path.join(os.path.dirname(__file__), 'test.txt')
    with open(filepath, 'r') as file:
        data = file.read()
        data = data.split()
    return data