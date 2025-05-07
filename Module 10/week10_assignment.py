def ford_fulkerson(graph, s, t):
    """
    Implement the Ford-Fulkerson algorithm to compute the maximum flow in the network 'graph' from source 's' to sink 't'.
    Return the value of the maximum flow.
    """

    def bfs_ff(graph, source, sink, parent):
        from collections import deque
        visited = [False] * len(graph)
        queue = deque([source])
        visited[source] = True


        while queue:
            u = queue.popleft()
            for v, capacity in enumerate(graph[u]):
                if not visited[v] and capacity > 0:
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u
                    if v == sink:
                        return True
        return False

    parent = [-1] * len(graph)
    flow = 0

    while bfs_ff(graph, s, t, parent):
        path_flow = float('inf')
        x = t
        while x != s:
            path_flow = min(path_flow, graph[parent[x]][x])
            x = parent[x]
        v = t
        while v != s:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]

        flow += path_flow

    return flow
    pass
