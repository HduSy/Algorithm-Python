# the graph
# 表示出有向图中每个节点的邻居
graph = {}
graph['a'] = {}
graph['a']['b'] = 5
graph['a']['c'] = 2

graph['b'] = {}
graph['b']['d'] = 2
graph['b']['e'] = 4

graph['c'] = {}
graph['c']['b'] = 8
graph['c']['d'] = 7

graph['d'] = {}
graph['d']['f'] = 1

graph['e'] = {}
graph['e']['d'] = 6
graph['e']['f'] = 3

graph['f'] = {}

# the costs table
infinity = float("inf")
costs = {}
costs['b'] = 5
costs['c'] = 2
costs['d'] = infinity
costs['e'] = infinity
costs['f'] = infinity

# the parents table
parents = {}
parents['b'] = 'a'
parents['c'] = 'a'
parents['d'] = None
parents['e'] = None
parents['f'] = None

processed = []

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    # Go through each node.
    # node => key
    for node in costs:
        cost = costs[node]
        # If it's the lowest cost so far and hasn't been processed yet...
        if cost < lowest_cost and node not in processed:
            # ... set it as the new lowest-cost node.
            lowest_cost = cost
            lowest_cost_node = node
    # 若所有节点均被处理过返回None
    return lowest_cost_node

# Find the lowest-cost node that you haven't processed yet.
node = find_lowest_cost_node(costs)
# If you've processed all the nodes, this while loop is done.
while node is not None:
    cost = costs[node]
    # Go through all the neighbors of this node.
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        # If it's cheaper to get to this neighbor by going through this node...
        if costs[n] > new_cost:
            # ... update the cost for this node.
            costs[n] = new_cost
            # This node becomes the new parent for this neighbor.
            parents[n] = node
    # Mark the node as processed.
    processed.append(node)
    # Find the next node to process, and loop.
    node = find_lowest_cost_node(costs)

print("Cost from the start to each node:")
print(costs)