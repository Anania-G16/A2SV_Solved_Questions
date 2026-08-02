def isDistinct(year):
    mySet = set()
    sYear = str(year)
    for ch in sYear:
        if ch not in mySet:
            mySet.add(ch)
        else:
            return False
    return True
    
while True:
    if isDistinct(year):
        print(year)
        break
    year += 1