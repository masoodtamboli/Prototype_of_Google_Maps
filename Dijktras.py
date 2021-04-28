from model import graph

def Dij_Algo(graph, start, goal):
    shortest_distance = {} # used this dict to store distance on the node for ex node(Pune) -> 99999
    track_previous_nodes = {} # used to track the predecessor means visited Nodes
    Nodes = graph # this dict is for our maps or u can say to store our graph
    infinity = 99999 # Dijktras algorithm initially makes all node to inifite so we used this int infinite
    trace_path= [] # to trace the path means from source to destination

    #Iterate in all nodes and assign infinite value to all nodes execpt start or source node
    for node in Nodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0

    #iterate Through every single Node 
    while Nodes:
        min_distance_node = None

        #take a node and keep it in min_distance_node until it does not get marked
        for node in Nodes:
            if min_distance_node is None:
                min_distance_node = node
            elif shortest_distance[node] < shortest_distance[min_distance_node]: #This condition is always false as infinite is always greater than any other value
                min_distance_node = node
        path_options = graph[min_distance_node].items() # find the adjacent nodes to the min_distacne_node and their distance

        #Iterate through this adjacewnt nodes and distance between them 
        for adjacentNode, distance in path_options:
            if distance + shortest_distance[min_distance_node] < shortest_distance[adjacentNode]:  # e.g 3 + 0 < 9999(infinite)
                shortest_distance[adjacentNode] = shortest_distance[min_distance_node] + distance # if true assign this add to adjacent node
                track_previous_nodes[adjacentNode] =  min_distance_node # further add visited i.e pune as visited
        Nodes.pop(min_distance_node) # and pop pune node if its all adjacent nodes are assigned distance 
    
    #Now we have found our goal so we have to trace back to the source node 
    currentNode = goal 
    while currentNode != start:
        try:
            trace_path.insert(0, currentNode) #Just add the visited nodes from goal to start in trace_path
            currentNode = track_previous_nodes[currentNode] #so now we have visited nodes in track_previous_nodes, fetch nodes from it
        except Exception as e:
            print(e)

    trace_path.insert(0, start) # the start does not gets inserted in it as while condition gets false so add it manually

    #If our goal is infinite means that we havnt reached the destination
    if shortest_distance[goal] != infinity:
        # print("Shortest Distance is"+str(shortest_distance[goal]))
        # print("Optimal path is :"+str(trace_path))
        return str(shortest_distance[goal]), trace_path