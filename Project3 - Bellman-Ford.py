a = []      #a list of all vertices
#b = []
list1 = []  #used to hold data in the data extraction function.
new = {}    #dictionary to hold the vertices(keys) and connected edges in form of objects.
v = []
dist = {}   #dictionary for distance between edges. Initial val = inf
prev = {}   #dictionary for previous values. Initial val = NIL
sTree = {}  #dictionary for spanning Tree. Key: [values]

"""
Defining the object structure to hold the name of each node
and the distance of the node from another vertice.
"""
class DataExtraction:
    def __init__(self, Name, Distance) -> None:
        self.Name = Name
        self.Distance = Distance

class object1:
  def __init__(self, index, value):
      self.index = index
      self.value = value

class PriorityQueue(object):
    def __init__(self):
        self.queue = []
 
    def __str__(self):
        return ' '.join([str(i) for i in self.queue])
 

    def isEmpty(self):
        return len(self.queue) == 0
 
    def insert(self, index, data):
        if index != None:
            for i in self.queue:
                if i.index == index: 
                    self.queue[self.queue.index(i)] = data
        else:
            self.queue.append(data)
 
    def delete(self):
        try:
            max_val = 0
            for i in range(len(self.queue)):
                if self.queue[i].value < self.queue[max_val].value:
                    max_val = i
            item = self.queue[max_val]
            del self.queue[max_val]
            return item
        except IndexError:
            print()
            exit()
"""
extracting the vertices, edges, and edge weight for the 'graph' to be processed from a text file.
"""
counter = 0
with open("dist.txt", "r") as f:
  while True:
    lines = f.readline()  
    lines.strip()
    if not lines:
      break
    # Loop through all lines.
   
    pos = lines.index(' - ')
    buildings = lines[:pos]
    nodes = lines[pos+3:]
    nodes = nodes.replace('\n','')
   
    list1 = nodes.split(" - ")
   
    a.append(buildings) #list of building names
    new[buildings] = []
   
    for var in list1:
       
        value = [int(m) for m in var.split() if m.isdigit()]
        value = value[0]
        var = ''.join((x for x in var if not x.isdigit()))
        var = var.rstrip()
        DataBinding = DataExtraction(var,value)
        v.append(DataBinding)
        
    new[a[counter]] = v
    v = []
    counter+=1


for i in v:
    if type(i) == str:
        i = ''.join((x for x in i if not x.isdigit()))
        #print(i)



"""
A representation of the graph to show the edges and edge weight between the vertices(buildings).
"""

for i in new:
    print(i, end='')
    k = new[i]
    for j in range(len(k)):
        print(' -> ', end='')
        print(k[j].Name, k[j].Distance, end ='')
    print()

print()
print("------------------------------OUTPUT--------------------------------")   
print()

"""
Beginning of Bellman-Ford:
       
"""

#listing out all the edges from the graph
edges = []
for each in new:
    ls = new[each]
    for x in ls:
        edge = [each, x.Name, x.Distance]
        edges.append(edge)



def shortPath():
    for i in new:
        dist[i] = float("inf")
        prev[i] = 'NIL'
        
    dist['Computer Science'] = 0
    
    vertices = len(dist)
    for x in range(vertices - 1):
        for edge in edges:
            update(edge)
    

def update(edge):
    u = edge[0]
    v = edge[1]
    weight = edge[2]
    
    if dist[v] > dist[u] + weight:
        dist[v] = dist[u] + weight
        prev[v] = u
    
#call the Bellman-Ford shortest path function    
shortPath()

"""
Initializing the spanning tree to hold the shortest path to each node in a list.
"""
for each in prev:
    sTree[each] = []

#populating the spanning tree    
for each in prev:
    l = prev[each]   
    
    while l != 'NIL':
        p = prev[l]
        sTree[each].insert(0,l)
        l = p

#printing the spanning tree
#print(sTree) 
for i in sTree:
    if i == 'Computer Science':
        continue
    print("Computer Science to ", i)
    print(sTree[i])       


#Dijkstra

hashmap = {}
j = 0
for i in new:
    hashmap[i] = j
    j+=1
distance = []
prev= []
hashmap1 = hashmap.copy()
hashmap2 = hashmap.copy()

#global distance


def dijkstra(Graph, distances, src):
  priorityQueue = PriorityQueue()
  for i in Graph:
    distances.append(float('inf'))
    prev.append('')
  distances[hashmap[src]] = 0
  for i in hashmap:
    obj1 = object1(i,distances[hashmap[i]])
    priorityQueue.insert(None, obj1)
  while not priorityQueue.isEmpty():
    u = priorityQueue.delete()
    for i in Graph[u.index]:
      if distances[hashmap[i.Name]] > distances[hashmap[u.index]] + i.Distance:
        distances[hashmap[i.Name]] = distances[hashmap[u.index]] + i.Distance
        prev[hashmap[i.Name]] = u.index
        obj1 = object1(i.Name, distances[hashmap[i.Name]])
        priorityQueue.insert(i.Name,obj1) 
  print("------------------------------OUTPUT--------------------------------")   

  
  j = 0
  for i in hashmap:
    hashmap[i] = distances[j]
    j+=1

dijkstra(new, distance, 'Computer Science')
emptyh = []
counter = 0
for i in hashmap1:
    counter = 0
    while id != 'Computer Science':
        if counter == 0:
            if i == 'Computer Science':
                break
            id = prev[hashmap1[i]]
            counter =1
        else:
            id = prev[hashmap1[id]]
        emptyh.append(id)
    id = '-1'
    emptyh =emptyh[::-1]
    emptyh.append(i)
    hashmap2[i] = emptyh
    emptyh = []

print()
print()

print("Dijkstra")
for i in hashmap2:
    if i == 'Computer Science':
        continue
    print("Computer Science to ", i)
    print(hashmap2[i])