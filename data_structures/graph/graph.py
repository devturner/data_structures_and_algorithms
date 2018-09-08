class Graph:
    def __init__(self):
        self.graph = {}

    def __repr__(self):
        return f'<Graph Length: {self._length}>'

    def __str__(self):
        return f' Graph Length: {self._length}'

    def __len__(self):
        return len(self.graph)

    def has_vert(self, val):
        """ checks for a key in the graph, do not allow duplicates
        """
        if val in self.graph:
            return True
        
        return False

    def add_vert(self, val):
        """ add vertice to graph
        """
        if self.has_vert(val):
            return "That value is already in the graph"
        # import pdb; pdb.set_trace()
        self.graph.update(val = {})
    
    def add_edge(self, v1, v2, weight):
        """ add a relationship and weight between two verts
        """
        if self.has_vert(v1):
            if v2 not in self.graph[v1]:
                self.graph[v1].update({v2: weight})
            else:
                return "That value already exsists"
        return 'That key is not in the graph'

    def get_neighbors(self, val):
        """ Given a val (key), return all all adjacent verts
        """
        neighbors = []
        if val in self.graph:
            for keys in self.graph[val]:
                neighbors.append(keys)
            return neighbors
        return "Value is not in graph"