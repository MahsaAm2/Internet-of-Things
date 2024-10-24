

""" in this function, the node's destinations are determined
 you can use this function, if you have algorithms for determining network TTL also nodes' data. 
in this function, you can choose one destination or a group of destinations or choose them based on the algorithms """
import random

dest1, dest2, dest3 ,dest4 = random.sample(range(0,49), 4)

def F_destination(NUMBER_NODES, Center_node, NETWORK_TTL):
    destination_c = []

    destination_c.append(dest1)
    destination_c.append(dest2)
    destination_c.append(dest3)
    destination_c.append(dest4)
    
    data = random.randint(1, 100)
    TTL = NETWORK_TTL
    return destination_c, data, TTL
