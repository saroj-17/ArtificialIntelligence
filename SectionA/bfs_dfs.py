'''
#        A
#       /  \
#      B    C 
#     /\    /\
#    D  E  F  G
#   /\  |
#  H  K J



'''
graph = {
    'A':['B','C'], 
    'B':['D','E'], 
    'C':['F','G'],
    'D':['H','K'],
    'E':['J'],
    'F':[],
    'g':[],
    'H':[],
    'J':[],
    'K':[]

}

#Print helper function 
def print_table_row(step, node, fringe, visited):
    print(f"{step:<5} | {node:<10} | {str(fringe) :<10} |{str(visited)}")

#dfs 
def dfs(graph, start, goal):
    visited= []
    stack = [start]
    step = 0

    print("\n DFS implementation with Tracing ")

    #TABLE headers 
    print("Step  | Current | Fringe        |visited")

    #DFS traversal 

    while stack: 
        node = stack.pop()
        step +=1 

        if node not in visited:
            visited.append(node)
            #display table 
            print_table_row(step, node,stack[::-1],visited)

        if node == goal: 
            print(f"Goal is found i.e {goal} using {step} steps")
            break 

        #backtracking 
        for child in reversed(graph[node]):
            if child not in visited: 
                stack.append(child)

#BFS 
def bfs(graph, start, goal):
    visited =[]
    queue = [start]
    step = 0

    #print table header 
    print("\n BFS Fringe Tracking in Table")
    print("Step     | Current   | Fringe(Queue)               | Visited")
    print("------------------------------------------------------------")

    #BFS Traversal 
    while queue: 
        node = queue.pop(0) #take the front node 
        step += 1
        
        if node not in visited: 
            visited.append(node)

            #diplay the current state 
            print_table_row(step, node, queue, visited)

        if node == goal: 
            print(f"\n Goal found at {goal} with {step} steps \n\n ")
            break 

        #enqueue all childrens not already visited or queued 

        for child in graph[node]:
            if child not in visited and child not in queue: 
                queue.append(child)




#set the start point and goal node 
start_node = 'A'
goal_node = 'K'

#Run DFS 
dfs(graph, start_node, goal_node)

#Run BFS 
bfs(graph, start_node, goal_node)

