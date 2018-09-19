

def get_edge(in_graph, locations):
    output = [False, 0]
    for i in locations:
        if in_graph.has_vert(i) is False:
            return output
        else:
            for k, v, in in_graph.graph[i].items():
                if k in locations:
                    output[0] = True
                    output[1] += v
    return output
