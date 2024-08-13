""" Bellman for algorithm work on N-1 Iteration called relax all the edges 

    Relax code if dist[u] + wt[u,v] < dist[v] then dist[v] = dist[u] + dist[v]
    it work for n-1 iteration and find all value in dist[] array with minimum distance value

    why N-1 it answer is given in raj hingu graph video
    How to handle negative Cycle ??
    if there is negative value cycle then there will be more than N-1 times iteration

    Writing solution from learning online from Raj Hingu video

    n = total number of Vertices
    edges  =  data having node and edges between them
    S = Source Index

    dist = [1e8]*n
    dist[S] = 0

    for i in range(n-1):
        for u,v,wt in edges:
            if dist[u]!=1e8 and dist[u] < dist[v] + wt:
                dist[v] = dist[u] + wt

    ## for checking negative cycle if grater than n chagen value then it return 01
    for u,v,wt in edges:
        if dist[u]!=1e8 and dist[u] < dist[v] + wt:
            return -1
    
    return dist

    """