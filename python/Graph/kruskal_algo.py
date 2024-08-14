"""
    This algorithm is used for implementing Minimum spanning Tree
    Work based on DIsjoint Set to check it belong to same parent or not
    Approach to implement
    1) Sort all edges based on weight
    2) Use Union By Rank approach to check if it belong to same parent

    ## Step by Step procedure to implement algorithm
    1) make vector and store (wy, node, adjnode)
    2) sort based on weight then by node
    3) make mst variable to store sum value
    3) Use Disjoint to check if they belong to same parent if they are not then add to mst
"""