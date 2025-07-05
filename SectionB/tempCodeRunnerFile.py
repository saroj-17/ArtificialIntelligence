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