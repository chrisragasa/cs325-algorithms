'''' 
Christopher Ragasa
CS 325
HW 5, Problem 5

This program demonstrates the BFS algorithm. The program takes a text file
as input that has a list of wresters. The algorithm is being utilized
to determine whether it is possible to designate some of the wrestlers
as Babyfaces and the remainder as Heels such that each rivalry is between
a Babyface and a Heel. 
'''

import sys

# each vertex represents a wrestler
class Vertex:
    # initializes variables of the vertex
    def __init__(self, n):
        # wrestler name
        self.name = n
        # wrestler type
        self.type = ''
        # neighors in graph
        self.neighbors = list()
        # distance between nodes -- initialize to a large number
        self.distance = float('inf')
        # track if vertex has been visited or not
        self.color = 'black'

    def add_neighbor(self, v):
        # validate that vertex is not already a neighbor before adding it
        if v not in self.neighbors:
            self.neighbors.append(v)
            self.neighbors.sort()

class Graph:
    # dictionary that holds all of the vertices 
    vertices = {}
    # indicates the start vertex
    start_vertex = None
    # indicates if the starting vertex of graph has already been set
    start_vertex_is_set = False
    # indicates if designation can be done -- if parent / child pairs 
    # are not of the same type
    can_designate = True

    # add a vertex to the graph
    def add_vertex(self, vertex):
        # confirm that vertex is an instance of the vertex class
        # confirm that vertex is not already in the graph
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            # add vertex
            self.vertices[vertex.name] = vertex
            # set the starting vertex if it hasn't been set already
            if not self.start_vertex_is_set:
                self.start_vertex_is_set = True
                self.start_vertex = vertex

    # add an edge betweeen vertices a and b
    def add_edge(self, a, b):
        # validate that vertices are in the vertices dictionary
        if a in self.vertices and b in self.vertices:
            # iterate through the items in vertices dictionary
            # for vertices a and b, add the other as a neighbor
            for key, value in self.vertices.items():
                if key == a:
                    value.add_neighbor(b)
                if key == b:
                    value.add_neighbor(a)

    # breadth first search
    def bfs(self, vertex):
        # create a queue
        q = list()

        # intiialize standard information for the vertex we start with
        vertex.type = 'Babyface'
        vertex.distance = 0
        vertex.color = 'red'

        # process the neighbors of the starting vertex
        for i in vertex.neighbors:
            # increment the distance for each neighbor
            self.vertices[i].distance = vertex.distance + 1
            # set all the neighbors as heels
            self.vertices[i].type = 'Heel'
            # enqueue the neighbor to the queue
            q.append(i)
    

        while len(q) > 0:
            # get the name of next node in the queue
            v = q.pop(0)
            # access this node as an object
            node = self.vertices[v]
            # track that this node has been visited
            node.color = 'red'
            # process the neighbors of this newly visited vertex
            for i in node.neighbors:
                node_i = self.vertices[i]
                # check if the node is visited
                if node_i.color == 'black':
                    # add node to the queue
                    q.append(node_i.name)
                    # check for the nodes distance
                    if node_i.distance > node.distance + 1:
                        node_i.distance = node.distance + 1
                    # assign vertex to babyface if distance is even,
                    # otherwise assign to heel
                    if node_i.distance % 2 == 0:
                        node_i.type = 'Babyface'
                    else:
                        node_i.type = 'Heel'
                    # check if child / parent are of the same type
                    if node_i.type == node.type:
                        self.can_designate = False

        # check that all vertices have been visited
        for v in self.vertices:
            if self.vertices[v].color == 'black':
                self.bfs(self.vertices[v])

    def print_wrestlers(self, type_name):
        results = []
        for v in self.vertices:
            if self.vertices[v].type == type_name:
                results.append(self.vertices[v].name)
        print(type_name + "s: "),
        for x in results:
            print(x),
        print('')

# function that checks if a string can be represented as an integer
def represents_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

# open the input file for reading
# appends a new element in an input_data array for each new line in txt file
with open(sys.argv[1], 'r') as f:
    input_data = []
    for line in f:
            #removes the trailing \n characters
            line = line.rstrip()
            input_data.append(line)

# create a new graph
graph = Graph()

# cycle through each of the elements in the input array 
i = 0

# check that the first element is a number,
# add the next i elements of the array to a graph
if represents_int(input_data[i]):
    # cast string to number
    number = int(input_data[i])
    # add the next i elements as vertices of the graph
    for j in range(i + 1, i + 1 + number):
        # create a vertex
        new_vertex = Vertex(input_data[j])
        graph.add_vertex(new_vertex)
    # print("Vertices added to graph.")
    # increment i to the next number in the text file
    i = i + 1 + number

# check that the next element is a number
if represents_int(input_data[i]):
    # cast string to number
    number = int(input_data[i])
    # add the next i elements as vertices of the graph
    for j in range(i + 1, i + 1 + number):
        split_string = input_data[j].split()
        graph.add_edge(split_string[0], split_string[1])
    # print("Edges added to graph.")

# run bfs on graph

graph.bfs(graph.start_vertex)

# print results
if graph.can_designate:
    print("Yes")
    graph.print_wrestlers('Babyface')
    graph.print_wrestlers('Heel')







