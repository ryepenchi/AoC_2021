from collections import defaultdict

caves = defaultdict(lambda: [])

def find_all_paths(graph, start, end, path=[], vsc=[]):
    path = path + [start]

    if start.islower():
        this_vsc = vsc + [start]
    else:
        this_vsc = vsc
    # print(path, this_vsc)
    if start == end:
        # print("path found: ", )
        return ([path], this_vsc)
    if not start in graph:
        print("end?", start)
        return ([], this_vsc)

    paths = []
    for node in graph[start]:
        # print("ping")
        small_cave_twice_visited = 2 in [this_vsc.count(x) for x in this_vsc]
        if (node not in path or node.isupper() or not small_cave_twice_visited) and node != "start":
            newpaths, vsc = find_all_paths(graph, node, end, path=path, vsc=this_vsc)
            for newpath in newpaths:
                paths.append(newpath)
        else:
            # print(node, "no")
            pass
    return (paths, vsc)

with open("input12.txt") as file:
    for line in file:
        u, v = line.strip().split("-")
        caves[u].append(v)
        caves[v].append(u)

allpaths, _ = find_all_paths(caves, "start", "end")
print(len(allpaths))
