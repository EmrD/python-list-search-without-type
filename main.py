list = [ 1 , 2 , 3 , 4 , 5 ]

def search(key):
    for i in list:
        if i == key or str(i) == key or float(i) == key or int(i) == key or str(float(i)) == key:
            return True
    return False

print(search("1")) # Example Usage