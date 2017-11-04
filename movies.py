from Graph import Graph
def main():
    filename = '../movies.txt'
    graph = Graph(filename, '/')
    # print(graph)
    with open('graphviz.txt', 'w') as out:
        out.write(graph.gen_graphviz())
if __name__ == "__main__":
    main()
