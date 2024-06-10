#In graph it is represnted as adajency matrix or adjaceny list
#graph={ undirected
#           a:[b,c]  #means a connected to b,c
#           b:[c,a]
#           c:[a,b]
#       }
#graph={directed
#           a:[b]  #means a connected to b,c
#           b:[c]
#           c:[a]
#       }
#graph={ weighed
#           a:[(b,7)]  #means a connected to b,c
#           b:[(a,2)]
#           c:[(a,2)]
#       }
#####bfs same as level order but we also have visited list so that connected elemnets won't be visited again
#bfs checks adjacbet ones not in depth
graph={
    "A":["B","C"],
    "B":["A","C","D"],
    "C":["A","B","E"],
    "D":["B","E"],
    "E":["C","D"]
    }
def bfs(start,graph):
    visited=[start]
    q=[start]
    while len(q)!=0:
        ele=q.pop(0)
        for i in graph[ele]: 
            if i not in visited:
                q.append(i)
                visited.append(i)
    return visited
print(bfs("B",graph))

#dfs checks in depth
#         a
#        / \
#       b - c
#graph={
#       "A":["b","c"]
#       "b":["a","b"]      
#       "c":["a","c"]
#}
#we have queue(visited) and stack
#take start as b
# b added to stack and visited
# and now b adjacents are checked a,b
#first a is added to stack and vsisited and then a adjacent are checked b,c
# a->b is already in visited so not added
#a-> c added to stack and queue
def dfs(start,graph,visited):
    visited.append(start)
    for i in graph[start]:
        if i not in visited:
            dfs(i,graph,visited)
    return visited
print(dfs("B",graph,[]))
    
