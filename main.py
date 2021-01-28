class Graph: 
  def __init__(self, vertices): 
    self.V = vertices 
    self.graph = [[0 for i in range(self.V)] for j in range(self.V)]
    self.edges = []

  def add_edge(self, src: int, dest: int, weight: int):  
    self.graph[src][dest] = weight
    self.graph[dest][src] = weight
    self.edges.append([src,dest,weight])
    
  def print_graph(self): 
    for i in range(self.V):
      print("node: ", str(i))
      for j in range(self.V):
        if(self.graph[i][j] != 0):
          print('path to node ', j, ': ', self.graph[i][j])
    print("\n")
  
  def matrix_print(self):
    print('node:', end =" ")
    for i in range(self.V):
      print(i,  end = " ")
    for j in range(self.V):
      print("\n   ", j,  end =" ")
      for k in range(self.V):
        print(self.graph[j][k], end = " ")
    print("\n")

  #Precondition: all graph components are connected
  #implementation of Prim's MST algorithm
  def mst(self):
    visited = [0 for i in range(self.V)] #visited set
    visited[0] = 1 #include first vertex in visited set 
    numEdges = 0 #number of edges included in spanning tree
    inf = 99999
    weightSum = 0
    print('MST spans across the following paths: \nEdge (weight)')
    #iterate until all vertices connected
    while(numEdges < (self.V - 2)):
      #find lowest weight edge from current vertex
      #local params
      minEdge = inf
      x = 0 #minEdge indicies in adj. matrix
      y = 0
      
      #iterate through adj. matrix
      for i in range(self.V):
        #min edge must start from a visited node to connect new node to existing tree
        if(visited[i] == 1):
          for j in range (self.V) :
            #new node must be unvisited and least edge
            if(visited[j] == 0):
              if(self.graph[i][j] < minEdge and self.graph[i][j] != 0):
                minEdge = self.graph[i][j]
                x = i
                y = j
  
      visited[y] = True #update visited vertex        
      weightSum += minEdge
      print('v',x, '<-> v',y, ' (weight: ', minEdge, ')')
      numEdges+=1
  
    print('Sum of weights in MST: ', weightSum)  
  
g = Graph(6)
#n0
g.add_edge(0,1,9)
g.add_edge(0,2,75)
#n1
g.add_edge(1,2,95)
g.add_edge(1,3,19)
g.add_edge(1,4,42)
#n2
g.add_edge(2,3,51)
g.add_edge(2,4,66)
#n3
g.add_edge(3,4,31)
#n4
g.print_graph()
g.mst()
