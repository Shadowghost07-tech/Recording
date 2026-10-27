n=int(input("enter no of states: "))
graph={}
for i in range(n):
    state=input("enter the state: ")
    graph[state]=[]
    k=int(input("no of neighbouring states: "))
    for j in range(k):
        neighbour=input("enter the neighbour name: ")
        graph[state].append(neighbour)
colors=["Red","Green","Blue","Brown"]
assigned={}

def valid(state,color):
    for neighbour in graph[state]:
        if neighbour in assigned and assigned[neighbour]==color:
            return False
    return True

def solve(index):
    states=list(graph.keys())
    if index==len(states):
        return True
    state=states[index]
    for color in colors:
        if valid(state,color):
            assigned[state]=color
            if solve(index+1):
                return True
            del assigned[state]
    return False

if solve(0):
    print("\nmap coloring: ")
    for state in assigned:
        print(state,"->",assigned[state])
else:
    print("no valid coloring")


