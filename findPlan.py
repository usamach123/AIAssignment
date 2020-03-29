from config import*

def findPlan(source,goal):
    plan=[]
    plan.clear()
    while(source!=goal):
        for x in range(len(parentData)):
            if(parentData[x]['child']==goal):
                #print(parentData[x]['rule'])
                plan.append(parentData[x]['rule'])
                goal=parentData[x]['parent']
                break
    count=len(plan)
    for x in range(count):
        if(x==count-1):

            print(rules[plan.pop()])
        else:
            print(rules[plan.pop()],end="->")

    print("")

