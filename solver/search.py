def dfs(graph, start_node, visited=None, res=None):
    '''
    depth first search of a graph

    Parameters:
        graph:dict: the graph to be searched
        start_node: str: the node to start the search from
        visited: list: visited nodes
        res: list: result list 
    '''
    if visited is None:
        visited = set()  # set to store visited nodes
    if res is None:
        res = [] # list to store the result

    stack = [start_node] # stack to store the nodes to be visited
    while stack:
        node = stack.pop() # get the last node in the stack
        if node not in visited: 
            visited.add(node) # mark the node as visited
            res.append(node) # add the node to the result list
        
            for nbr in reversed(graph.get(node, [])): # reverse so neighbors are visited in original order
                if nbr not in visited:
                    stack.append(nbr) # add the neighbor to the stack
    return res 
 
