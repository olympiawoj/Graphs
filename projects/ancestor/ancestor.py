
'''
Input- LIST of data describing a graph of relationships between parents and children, formatted as a list of (parnt, child) pairs
- Each individual is assigned a *UNIQUE* integer identifer 

Ex: 
Input of 3 is a child of 1 and 2
Input of 4 is a child of 2 and 5

ancestors is our list
starting_node is id of where we start

Return - *id* of the ancestor furthest from the input individual 

If middle of a maze - want to get to end
1) DEPTH FIRST
If you wanna visit every single thing closest to maze
2) BREADTH

Spill cup of water- spread evenly from center
Remember what you use for each one 
Queue for Breadth
Stack for Depth

**Change the while loop**

#1 --> 10
#2 --> -1
#3 -->10
#4 --> -1
#5 --> 4


'''

from util import Stack, Queue  # These may come in handy

#crate a graph
class Graph:
    """
    Represent a graph of ancestor nodes, mapping parents relationship to children
    """
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex_id):
        #add a vertext to the graph
        self.vertices[vertex_id] = set()
    def add_edge(self, v1, v2):
        #add relationship/edge to graph between ancestor/descendent DIRECTED means 1  way
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise ValueError("Value Error: Vertex does not exist")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            raise ValueError("Error: Vertex does not exist")
        
def earliest_ancestor(ancestors, starting_node):
    # Build the graph
    graph = Graph()
    for pair in ancestors:
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])
        # Build edges in reverse
        # graph.add_edge(pair[1], pair[0])
    for pair in ancestors:
        graph.add_edge(pair[1], pair[0])
    # Do a BFS (storing the path)
    q = Queue()
    q.enqueue([starting_node])
    max_path_len = 1
    earliest_ancestor = -1
    while q.size() > 0:
        path = q.dequeue()
        v = path[-1]
        # If the path is longer or equal and the value is smaller, or if the path is longer)
        if (len(path) >= max_path_len and v < earliest_ancestor) or (len(path) > max_path_len):
            earliest_ancestor = v
            print('earliest ancestor', earliest_ancestor)
            max_path_len = len(path)
        for neighbor in graph.vertices[v]:
            path_copy = list(path)
            path_copy.append(neighbor)
            q.enqueue(path_copy)
    return earliest_ancestor

# def earliest_ancestor(ancestors, starting_node):
#     #depth first search
#     '''
#     Return an index for the ancestor furthest from starting node OR -1
#     '''
#     #build the graph to loop over
#     g = Graph()


#     #loop over every ancestor
#     #build up visited ancestors dict
#     #once we do that, find max distance, furthest ancestor by calling max on keyso f dict
#     #return the smallest id from max_distance list

#     for vertex in ancestors:
#         #create graph in reverse
#         g.add_vertex(vertex[0])
#         g.add_vertex(vertex[1])
#         #build edges in reverse
#         g.add_edge(vertex[1], vertex[0])

#     #Do a BFS (storing the path)
#     q = Queue()
#     #enqueue starting node
#     q.enqueue([starting_node])

#     earliest_ancestor = -1
#     max_path_len = 1
#     # Enqueue means to add an element to front, dequeue to remove an element from front
#     # Queue is FIFO

#     while q.size() > 0:
#         path = q.dequeue()
#         print('path', path)
#         current_vertex = path[-1]
#         print('cur vtx', current_vertex)

#       # If the path is longer or equal and the value is smaller, or if the path is longer)
#         if (len(path) >= max_path_len and current_vertex < earliest_ancestor) or (len(path) > max_path_len):
#             earliest_ancestor = current_vertex
#             max_path_len = len(path)
#         for neighbor in g.vertices[current_vertex]:
#             path_copy = list(path)
#             path_copy.append(neighbor)
#             q.enqueue(path_copy)
#     return earliest_ancestor



ancestors=[(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

print(earliest_ancestor(ancestors, 1))
#10


print(earliest_ancestor(ancestors, 2))
#-1 


print(earliest_ancestor(ancestors, 3))
#10