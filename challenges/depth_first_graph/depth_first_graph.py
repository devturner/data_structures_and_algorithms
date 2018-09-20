

def get_neighbors(self, val):
    """ Given a val (key), return all all adjacent verts
    """
    neighbors = []
    if val in self.graph:
        for keys in self.graph[val]:
            neighbors.append(keys)
        return neighbors
    return "Value is not in graph"


def depth_first_graph(in_graph, vert):
    if vert in in_graph.graph:
        queue = []
        output = []
        queue.append(vert)
        while queue:
            v = queue.pop()
            for key in in_graph.graph[v]:
                if v not in output:
                    queue.append(key)
                    output.append(v)
        return output
    
    return "That is not a valid starting point"
