import heapq  

def find_shortest_path(graph, start_node, end_node):
    # everyone starts infinitely far away
    distances = {node: float('inf') for node in graph.adjacency_list}
    # except our starting point
    distances[start_node] = 0
    # track how we got to each place
    predecessor = {node: None for node in graph.adjacency_list}

    # start with our beginning spot
    heap = [(0, start_node)]

    while heap:
        # grab the closest place we haven't fully checked
        current_distance, current_node = heapq.heappop(heap)

        # found the destination? we're done
        if current_node == end_node:
            break

        # look at all neighbors
        for neighbor, weight in graph.adjacency_list.get(current_node, []):
            # how far if we go this way?
            distance = current_distance + weight
            # is this better than what we had?
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                # remember how we got here
                predecessor[neighbor] = current_node
                # add to queue
                heapq.heappush(heap, (distance, neighbor))

    # couldn't reach it
    if distances[end_node] == float('inf'):
        return None, float('inf')

    # build the path backwards
    path = []
    node = end_node
    while node:
        # add to front of list
        path.insert(0, node)
        # go to previous node
        node = predecessor[node]

    return path, distances[end_node]