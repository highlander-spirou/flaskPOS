def WriteCache(filename, newtext):
    with open(filename, "r+") as txt:
        old_data = txt.read()
        txt.seek(0)
        txt.write(newtext + '\n' + old_data)



def ReadCache(filename):
    with open(filename, 'r') as txt:
        r = txt.readline()
    return r

def CountLine(filename):
    count = 0
    with open(filename, 'r') as txt:
        for line in txt:
            count += 1
    return count

def ClearCache(filename):
    lines = CountLine(filename)
    if lines > 100:
        t = ReadCache(filename)
        with open(filename, 'w') as txt:
            txt.write(t)
