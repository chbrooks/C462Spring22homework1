
from random import randint, choice

### an edge is a link between two nodes. Right now, the only other
### information an edge carries is the weight of the link. Later we
### will add other azgrnnotations.

class Edge() :
    def __init__(self, src, dest, weight) :
        self.src = src
        self.dest = dest
        self.weight = weight

    def __repr__(self) :
        return "(%d,%d, %d)" % (self.src, self.dest, self.weight)


### The graph class itself.
### The edgeMap is a dictionary that maps nodes to lists of Edges emanating from that node.
### We will use integers to represent nodes.


class Graph() :
    def __init__(self):
        self.edgeMap = {}

    ### implements the 'in' keyword. Returns true if the node is in the graph.
    def __contains__(self, item):
        return item in self.edgeMap.keys()

    def add_node(self, src):
        if src not in self.edgeMap.keys() :
            self.edgeMap[src] = []

    def add_edge(self, src, dest, weight):
        e = Edge(src,dest,weight)
        self.add_node(src)
        self.add_node(dest)
        if src in self.edgeMap :
            self.edgeMap[src].append(e)
        else :
            self.edgeMap[src] = [e]

    def get_edges(self, src) :
        return self.edgeMap[src]

    ## Assume file is in the mtx format: % is a comment
    ## Otherwise it's source destination weight
    ### The file in the github repo will work as a sample for you.
    ### It's in the format: source, vertex, weight. You should assume that the graph is symmetric -
    ### if there's an edge from a to b, there's an edge from b to a.
    ### You can find lots of others here: http://networkrepository.com/index.php
    def read_from_file(self, fname):
        with open(fname) as f :
            for l in f.readlines() :
                if not l.startswith("%") :
                    (s,d,w) = [int(x) for x in l.split()]
                    self.add_edge(s,d,w)

    ## Make a random graph. It's acutally a little tricky to make a "random" graph, depending on the properties we need.
    ## This will make a random, fully-connected graph, and then randomly delete a fraction of the edges.
    ## note that it's an instance method, so we're assuming that you call it on an instantiated graph.
    ## let's assume weights are random numbers from 1-10

    def make_graph(self, num_vertices, fraction_edges_to_delete):
        edge_count = 0
        for i in range(num_vertices) :
            for j in range(num_vertices) :
                if i != j :
                    self.add_edge(i,j,randint(1,11))
                    edge_count += 1
        # now, delete some edges.
        for i in range(int(fraction_edges_to_delete * edge_count)) :
            ## pick a random vertex
            v = choice(list(self.edgeMap.keys()))
            edges = self.edgeMap[v]
            index = randint(0, len(edges)-1)
            edges.pop(index)


    ### inputs are the name of a startNode and endNode. Given this,
    ### return a list of Nodes that indicates the path from start to finish, using breadth-first search.

    def breadth_first_search(self, startNode, endNode):
        pass

    ### inputs are the name of a startNode and endNode. Given this,
    ### return a list of Nodes that indicates the path from start to finish, using depth-first search.

    def depth_first_search(self, startNode, endNode):
        pass

    ### implement Djikstra's all-pairs shortest-path algorithm.
    ### https://yourbasic.org/algorithms/graph/#dijkstra-s-algorithm
    ### return the array of distances and the array previous nodes.

    def djikstra(self, startNode):
        pass

    ### takes as input a starting node, and computes the minimum spanning tree, using Prim's algorithm.
    ### https:// en.wikipedia.org/wiki/Prim % 27s_algorithm
    ### you should return a new graph representing the spanning tree generated by Prim's.
    def prim(self, startNode):
        pass

    ### 686 students only ###
    ## takes as input a startingNode and returns a list of all nodes in the maximum clique containing this node.
    ### https://en.wikipedia.org/wiki/Clique_problem#Finding_a_single_maximal_clique

    def clique(self, start_node):
        pass