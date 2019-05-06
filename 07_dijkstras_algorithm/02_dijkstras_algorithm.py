# the graph
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
# the costs
costs = {}
infinity = float('inf')
costs['b'] = 5
costs['c'] = 2
costs['d'] = infinity
costs['e'] = infinity
costs['f'] = infinity
# processed
processed = []
# parents
parents = {}
parents['b'] = 'a'
parents['c'] = 'a'
parents['d'] = None
parents['e'] = None
parents['f'] = None


# find the lowest cost node
def find_lowest_node(costs):
    lowest_cost = infinity
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if node not in processed and cost < lowest_cost:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


if __name__ == '__main__':
    node = find_lowest_node(costs)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            # 起始点经当前'试验点'出发到其邻居开销和计算
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
    node = find_lowest_node(costs)
    print("Cost from the start to each node:")
    print(costs)
