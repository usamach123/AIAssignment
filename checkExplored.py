from config import*
def checkExplored(dequ):
    for x in range(len(exploredSet)):
        if(exploredSet[x]==dequ):
            return True
    return False