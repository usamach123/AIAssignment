
from config import*
def getStateNumber(deque):
    for x in range(noOfStates):
        if(stateDescriptions[x]==deque):
            return (x)