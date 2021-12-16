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


# adapted from https://www.geeksforgeeks.org/find-paths-given-source-destination/
def print_all_paths(graph, s, d, lower_visited, cur_path):
    # Mark the current node as visited and store in path
    if s[0].islower():
        lower_visited[s] = True
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
                    if not lower_visited[i]:
                        print_all_paths(graph, i, d, lower_visited, cur_path)
                else:
                    print_all_paths(graph, i, d, lower_visited, cur_path)

    # Remove current vertex from path[] and mark it as unvisited
    if s[0].islower():
        cur_path.pop()
        lower_visited[s] = False


def main():
    G = format_data("data.txt")

    lower_visited = {}
    for n in G:
        if n[0].islower():
            lower_visited[n] = 0
    print_all_paths(G, 'start', 'end', lower_visited, [])


if __name__ == "__main__":
    main()