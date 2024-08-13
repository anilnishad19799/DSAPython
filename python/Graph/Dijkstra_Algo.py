""" Dijkstra algorithm work for finding shortest path algorithm

    Approach to implement Dijsktra algorithm
    1) Queue
    2) Priority Queue
    3) set

    Implement using Priority Queue
    find minimum distance value and add up then add using priority queue (min heap)

    Basic Code for Dijkstra algorithm

    n = length of vertices 
    
    pq = priority queue
    s = Source Vertex
    dist = []
    for i in V:
        dist[i] = 1e8
    
    pq.push([0, S])
    while !pq.isEmpty():
        dis = pq.first()
        node = pq.second()
        
        pq.pop()

        for iter in node.connection():
            connnode = iter[0]
            connweight = iter[1]

            ## initially all set to infinity then if node to connection wieght then it set to that value
            if dis + connweight < dist[connnode]:
                dist[connnode] = dis + connnode
                pq.push([dist[connnode],connnode])

    return dist

"""