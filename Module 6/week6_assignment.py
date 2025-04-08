def bfs(graph, start):
    """
    Traverse the graph using Breadth First Search starting from the given node.
    Return the order in which the nodes are visited.
    """
    # based on https://youtu.be/HZ5YTanv5QE
    visited = [start]
    queue = [start]
    while queue:
        travels = queue.pop(0)
        for x in graph[travels]:
            if x not in visited:
                visited.append(x)
                queue.append(x)
    return visited
    pass

def dfs(graph, start):
    """
    Traverse the graph using Depth First Search starting from the given node.
    Return the order in which the nodes are visited.
    """
    visited = [] #clean slate
    queue = [start]
    while queue:
        traveling = queue.pop()
        if traveling not in visited:
            visited.append(traveling)
            queue.extend(reversed(graph[traveling])) # Reversed so that nodes are traveled vertically first
    return visited
    pass

def dijkstra(graph, start):
    """
    Compute the shortest path from the start node to all other nodes in the graph using Dijkstra's algorithm.
    Return a list of minimum distances from the start node to every other node.
    """
    pass
