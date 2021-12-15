from tarjan import Graph

if __name__ == "__main__":
    g = Graph()
    g.read_data("tarjan_in.txt")
    print(g.tarjan())