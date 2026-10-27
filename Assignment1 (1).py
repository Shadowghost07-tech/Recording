graph={
    "pune":{"mumbai":140},
    "mumbai":{"pune":140,"jalna":230,"sind":220},
    "sind":{"ratnagiri":110,"mumbai":220,"jalna":43},
    "jalna":{"mumbai":230,"sind":43,"nagpur":432,"lucknow":111},
    "nagpur":{"kanpur":250,"jalna":432},
    "kanpur":{"nagpur":250},
    "lucknow":{"jalna":111,"ratnagiri":440},
    "ratnagiri":{"lucknow":440,"sind":110},
}
#heurastic values
h={
    "pune":200,
    "mumbai":300,
    "sind":100,
    "jalna":102,
    "nagpur":322,
    "kanpur":433,
    "lucknow":322,
    "ratnagiri":0,
}
start="pune"
goal="ratnagiri"

def bfs():
    queue=[[start,[start]]]
    visited=[start]
    while queue:
        city,path=queue.pop(0)
        if city==goal:
            return path
        for neighbour in graph[city]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append([neighbour,path+[neighbour]])


def ucs():
    queue=[[0,start,[start]]]
    visited=[]
    while queue:
        index=0
        for i in range(1,len(queue)):
            if queue[i][0]<queue[index][0]:
                index=i
        #cost,city=queue.pop(index)
        cost,city,path=queue.pop(index)
        if city in visited:
            continue
        visited.append(city)

        if city==goal:
            return path,cost
        for neighbour in graph[city]:
            new_cost=cost+graph[city][neighbour]
            queue.append([new_cost,neighbour,path+[neighbour]])
def Astar():
    queue=[[h[start],0,start,[start]]]
    best={start:0}
    while queue:
        index=0
        for i in range(1,len(queue)):
            if queue[i][0]<queue[index][0]:
                index=i
        f,cost,city,path=queue.pop(index)
        if cost!=best[city]:
            continue
        if city==goal:
            return path,cost
        for neighbour in graph[city]:
            new_cost=cost+graph[city][neighbour]
            if neighbour not in best or new_cost<best[neighbour]:
                best[neighbour]=new_cost
                new_f=new_cost+h[neighbour]
                queue.append([new_f,new_cost,neighbour,path+[neighbour]])

print("BFS:","->".join(bfs()))

path,cost=ucs()
print("UCS:","->".join(path)," Distance:",cost,"km")
path,cost=Astar()
print("A*: ","->".join(path)," Distance:",cost,"km")