def bfs(graph, start_node):
    """Perform BFS on the graph starting from start_node."""
    visited = set()
    queue = [start_node]
    visited.add(start_node)

    while queue:
        node = queue.pop(0)
        print(node)  # Process the node (e.g., print it)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)