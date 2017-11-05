from collections import Counter
from Graph import Graph


def main():
    filename = '../movies.txt'
    graph = Graph(filename, '/')
    count = Counter()
    for v in graph.vertices():
        count[v] = graph.degree(v)
    for c in count.most_common(10000):
        print(*c)


    # print(graph)
    # with open('graphviz.txt', 'w') as out:
    #     out.write(graph.gen_graphviz())
if __name__ == "__main__":
    main()
