import random
import sys

first_node_num = 2
m = 2
r = 1


def select_random_node():
    rand = random.random()
    edge_count = 0
    for i, node in enumerate(node_list):
        edge_count += node
        check_range = edge_count/(len(edge_list_tuple) * 2)
        if rand < check_range:
            return i
    return -1


def create_new_edge(node_id):
    s_node = select_random_node()
    while(s_node in edge_list[node_id]):
        s_node = select_random_node()
    edge_list[s_node].append(node_id)
    edge_list[node_id].append(s_node)
    node_list[s_node] += 1
    node_list[node_id] += 1
    edge_list_tuple.append((node_id, s_node))


def create_new_node(first):
    node_list.append(0)
    edge_list.append([])
    if first==True:
        return
    if m == len(node_list) - 1:
        for i in range(m):
            edge_list[len(node_list) - 1].append(i)
            edge_list[i].append(len(node_list) - 1)
            node_list[i] += 1
            node_list[len(node_list) - 1] += 1
            edge_list_tuple.append((len(node_list) - 1, i))
        return
    for i in range(m):
        create_new_edge(len(node_list) - 1)


# main

node_list = []
edge_list = []
edge_list_tuple = []
args = sys.argv

for i in range(first_node_num):
    create_new_node(True)

for i in range(int(args[1])):
    create_new_node(False)
    print(edge_list_tuple)

print(node_list)
print(edge_list)
print(edge_list_tuple)

for i in edge_list:
    if -1 in i:
        print("error!")
