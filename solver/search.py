def dfs(graph, start_node, visited=None, res=None):
    if visited is None:
        visited = set()
    if res is None:
        res = []

    visited.add(start_node)
    res.append(start_node)  # Add the node to the result list
    for neighbor in graph[start_node][1]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, res)
    
    return res
