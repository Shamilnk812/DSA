def insert_values(v):
    if v in graph :
        print(v, 'is already presnt in this graph')
    else :
        graph[v] = []

def add_edges(v1,v2):
    if v1 not in graph :
        print(v1,'is not present')
    elif v2 not in graph:
        print(v2,'is not present')
    else :
        graph[v1].append(v2)
        graph[v2].append(v1)

def add_edges_cost(v1, v2, cost):
    if v1 not in graph :
        print(v1,'is not present')
    elif v2 not in graph:
        print(v2,'is not present')
    else :
        list1 = [v1,cost]
        list2 = [v2,cost]
        graph[v1].append(list2)
        graph[v2].append(list1)

def delete_node(v) :
    if v not in graph :
        print(v, 'is not present')
    else :
        graph.pop(v)
        for i in graph:
            temp = graph[i]
            if v in temp :
                temp.remove(v)

def delete_edges(v1, v2):
    if v1 not in graph :
        print(v1,'is not present')
    elif v2 not in graph:
        print(v2,'is not present')
    else : 
        if v2 in graph[v1]:
            graph[v1].remove(v2)
            graph[v2].remove(v1)

def DFS(node):
    if node not in graph :
        print('noto present')
    else :
        stack.append(node)
        while stack :
            current = stack.pop()
            if current not in visited:
                print(current,end=' ')
                visited.add(current)
                for i in graph[current]:
                    stack.append(i)    


from collections import deque
def BFS(node):
    if node not in graph :
        print('not presetn')
    else :
        q = deque()
        q.append(node)
        visited.add(node)
        while q:
            current = q.popleft()
            print(current)
            for i in graph[current] :
                if i not in visited :
                    visited.add(i)
                    q.append(i)
            
            

graph = {}
stack =[]
visited = set()

strr = 'ABCD'
for i in strr:
    insert_values(i)

add_edges('A','B')
add_edges('A','C')
add_edges('B','D')

DFS('A')