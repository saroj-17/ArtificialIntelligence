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


#driver code 
start_node = 'A'
goal_node = 'K'

dfs(graph, start_node, goal_node)

