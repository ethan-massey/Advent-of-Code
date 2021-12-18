import networkx as nx
# https://networkx.org/documentation/stable/tutorial.html


# format data
def format_data(datafile: str) -> nx.Graph:
    G = nx.Graph()
    lines = open(datafile, "r").readlines()
    for line in lines:
        edge = line.strip().split('-')
        G.add_edge(edge[0], edge[1])
    return G


# PART 1
# adapted from https://www.geeksforgeeks.org/find-paths-given-source-destination/
def print_all_paths_p1(graph, s, d, cur_path):
    # Mark the current node as visited and store in path
    cur_path.append(s)

    # If current vertex is same as destination, then print
    # current path[]
    if s == d:
        print(cur_path)
    else:
        # If current vertex is not destination
        # Recur for all the vertices adjacent to this vertex
        for i in graph[s]:
            if i != 'start':
                if i[0].islower():
                    if cur_path.count(i) < 1:
                        print_all_paths_p1(graph, i, d, cur_path)
                else:
                    print_all_paths_p1(graph, i, d, cur_path)

    # Remove current vertex from path[] and mark it as unvisited
    cur_path.pop()


# PART 2
def print_all_paths_p2(graph, s, d, cur_path):
    # Mark the current node as visited and store in path
    cur_path.append(s)

    # If current vertex is same as destination, then print
    # current path[]
    if s == d:
        print(cur_path)
    else:
        # If current vertex is not destination
        # Recur for all the vertices adjacent to this vertex
        for i in graph[s]:
            if i != 'start':
                if i[0].islower():
                    # dict of occurrences of i in
                    count = {n: cur_path.count(n) for n in cur_path if n[0].islower()}
                    # first time seeing i?
                    if i not in cur_path:
                        count[i] = 0
                    # no small caves have been visited more than once
                    if max(count.values()) <= 1:
                        print_all_paths_p2(graph, i, d, cur_path)
                    # a cave has been seen more than once. Only go to this small
                    # cave if it hasn't been seen yet
                    else:
                        if count[i] == 0:
                            print_all_paths_p2(graph, i, d, cur_path)
                else:
                    print_all_paths_p2(graph, i, d, cur_path)

    # Remove current vertex from path[] and mark it as unvisited
    cur_path.pop()


def main():
    G = format_data("data.txt")

    # Part 1
    # print_all_paths_p1(G, 'start', 'end', [])
    # Part 2
    print_all_paths_p2(G, 'start', 'end', [])


if __name__ == "__main__":
    main()