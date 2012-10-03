#
# Write a function, `bipartite` that
# takes as input a graph, `G` and tries
# to divide G into two sets where 
# there are no edges between elements of the
# the same set - only between elements in
# different sets.
# If two sets exists, return one of them
# or `None` otherwise
# Assume G is connected
#
import random

def bipartite(G):
    root = random.choice(G.keys())
    open_list = [root]
    blue = set()
    red = set()
    flag = True    
    red.add(root)
    next_level = []
    
    while open_list:
        current = open_list[0]
        print open_list
        print 'current', current
        del open_list[0]
        for neighbor in G[current]:
            if neighbor not in blue and neighbor not in red:
                if flag == True:
                    blue.add(neighbor)
                if flag == False:
                    red.add(neighbor)
                next_level.append(neighbor)
                print 'next level', next_level
                print 'red', red
                print 'blue', blue
            if neighbor in blue and flag == False:
                return None
            if neighbor in red and flag == True:
                return None 
        if not open_list:
            if flag == True:
                flag = False
                print flag
                print 'swithc'      
            elif flag == False:
                flag = True
                print 'swtcj'
                print flag
            print 'flag switch', flag
            open_list = next_level
            next_level = []
        raw_input()
    return blue


########
#
# Test

def make_link(G, node1, node2, weight=1):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = weight
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = weight
    return G


def test():
    edges = [(1, 2), (2, 3), (1, 4), (2, 5),
             (3, 8), (5, 6)]
    G = {}
    for n1, n2 in edges:
        make_link(G, n1, n2)
    g1 = bipartite(G)
    print 'g1', g1
    assert (g1 == set([1, 3, 5]) or
            g1 == set([2, 4, 6, 8]))
    edges = [(1, 2), (1, 3), (2, 3)]
    G = {}
    for n1, n2 in edges:
        make_link(G, n1, n2)
    g1 = bipartite(G)
    assert g1 == None





print test()


