""" Minimum spanning tree 

    spanning tree :-  A tree having n node and n-1 edges is spanning tree
    there can be many spanning tree in one graph but the tree having minimum sum will be minimum spanning tree

    also there is similar logic as compare to dijkstra algorithm and return minimum sum of spanning tree

    ## Prims Algorithm (Greedy approach)

    implementaion is done using prority queue

    sum = 0
    V = no. of vertices
    visit = [0] * V
    pq = priorirty queue

    
    # 0,0 = (weight, node)
    pq.push({0,0})

    while pq.isempty() : 
        weightnode = pq.top()
        pq.pop()

        weight = weightnode.first
        node = weightnode.second

        if visit[node] == 1: continue
        visit[node] = 1
        sum+=weight

        for conn in node.connection():
            wieght = conn.second
            node = conn.first
            if !visited[conn]:
                pq.push(weight, node)            

    return sum

"""