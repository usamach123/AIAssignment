from config import *
from getChildren import *
from checkExplored import *
from findPlan import *
def bFS(testCases):

    for y in range(len(testCases)):
        print("TEST CASE ",y+1," :", end =" ")
        parentData.clear()
        frontier.clear()
        goalFound=False
        exploredSet.clear()
        frontier.append(testCases[y]['initial'])
        if(testCases[y]['initial']==testCases[y]['final']):
            print('Do Nothing')
        else:
            while(len(frontier)!=0 ):
                if(goalFound==True):
                    #print("mil gya")
                    break
                dequed=frontier.pop(0)
                exploredSet.append(dequed)

                children=getChildren(dequed)
                #print(len(children))
                for x in range(len(children)):
                    #print(children[x])
                    if(children[x]==testCases[y]['final']):
                        goalFound=True
                        #print("mil gya")
                    else:
                        #print("kg gaye")
                        temp=checkExplored(children[x]);
                        #print(temp)
                        if(temp==False):
                            frontier.append(children[x])
                            #print(len(frontier))


            if(len(frontier)==0 and goalFound==False):
                print("GOAL NOT FOUND")
            else:
                print("GOAL FOUND")
                print("PLAN : ", end =" ")
                findPlan(testCases[y]['initial'],testCases[y]['final'])

