
import random

random.seed(10)
class Vertex:
    def __init__(self, name):
        self.name = name



class Graph:
    vertices = {}
    edges = []
    edge_indicies = {}
    edge_mapper=[]

    def add_vertex(self, vertex):
        if(isinstance(vertex,Vertex)) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            for row in self.edges:
                row.append(0)
            self.edges.append([0] * (len(self.edges) + 1))
            self.edge_indicies[vertex.name] = len(self.edge_indicies)
            self.edge_mapper.append(vertex.name)
            return True

        else:
            return False

    def add_edge(self, u, v, weight):
        if u in self.vertices and v in self.vertices:
            self.edges[self.edge_indicies[u]][self.edge_indicies[v]] = weight
            self.edges[self.edge_indicies[v]][self.edge_indicies[u]] = weight
           
            return True
        else:
            return False

    def print_graph(self):
        for v in self.vertices:
            print("   " + v , end = " ")
        print()
        for v, i in sorted(self.edge_indicies.items()):
            print(v + ' ' , end = ' ')
            for j in range(len(self.edges)):
                print(str(self.edges[i][j]) + "   ", end =' ')
            print(' ')
            print()



g = Graph()

g.add_vertex(Vertex('A'))
g.add_vertex(Vertex('B'))
g.add_vertex(Vertex('C'))
g.add_vertex(Vertex('D'))
g.add_vertex(Vertex('E'))
g.add_vertex(Vertex('F'))



edges = ['AC', 'CE', 'EF', 'FB','AE', 'DE','CB', 'DB', 'DA', 'EB', 'FA']
for edge in edges:
    g.add_edge(edge[0], edge[1],(random.randrange(1, 9)))

g.print_graph()

#   Simulated Annieling 
# track where we have been
# include random with higher probability in the begining
# choose lowest cost available if not effected by temp. 


# check number of connections and pick the lowest (or one of the lower ones if a tie) as the start
min = 100
starters = []
for v in g.vertices:
    
    total = sum(s.count(v) for s in edges)
    if total < min:
        min = total
        starters = []
        starters.append(v)
    elif total == min:
        starters.append(v)
    print(v,total)

print(starters)
if len(starters) > 1:
    starter = random.randrange(0, len(starters))
else:
    starter = starters[0]

print(starters[starter])

print( g.edges[g.edge_indicies['D']])
l =  g.edges[g.edge_indicies['D']]
print(type(l))
print(l)
#print(g.edge_mapper)
#min_cost = min(l)
min_value=100
min_index =0
index = 0

for  i in range(0,len(l)):
    if l[i] < min_value and l[i] >0:
        min_value = l[i]
        min_index = i

print("The index with the lowest value is ", min_index,  min_value)


### TODO Simulatd Anneiling
# Create a start score ie 100
# each step score decreases by  100 / N (where n is the number of Vertex's that have been visited)
# Example At step 100 % chance of choosing a less optimal path if chosen randomly
# Next Step 83% chance of choosing a less optimal path if chosen randomly.  Othwise choose lowest cost
## Next Step 67% chance of choosing a less optimal path if chosen randomly.  Othwise choose lowest cost
# Next Step 51% chance of choosing a less optimal path if chosen randomly.  Othwise choose lowest cost
## Next Step 35% chance of choosing a less optimal path if chosen randomly.  Othwise choose lowest cost
## Next Step 19% chance of choosing a less optimal path if chosen randomly.  Othwise choose lowest cost%
## Next Step 3% chance of choosing a less optimal path if chosen randomly.  Othwise choose lowest cost%
#Pick the smallest amount regardless (if this is the last one there should only be one left)

# Alternative approaches can also be used that drop the percentage quicker
# random.randrange(0, 100) can be used to and if it is below the score value allow less optimal node selection

### TODO Keep track of the nodes visited already to ensure nodes dont go to the same node twice
### for 6 nodes we can keep track of a visited array of length 6 initialized as [ 0,0,0,0,0,0]
## When visited, we can swap a node index from 0 to 1.  Only try to move to nodes that are currently 0
