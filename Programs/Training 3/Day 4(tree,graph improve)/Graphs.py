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

