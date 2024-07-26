#linked lst and hasmap are related
#one powerful algo is hare tortosie mechanism
#1 2 3 4 5 we have this find middle
#turtle moves 1 poinet and hare moves 2 points
# 1 2 3 4 5
# t
# h
#1 2 3 4 5
#  t h
#1 2 3 4 5
#    t   h --done so hare.next!=Null
#even case
# 1 2 3 4 5 6
# t
# h
#1 2 3 4 5 6
#  t h
#1 2 3 4 5 6
#    t   h
#1 2 3 4 5 6
#      t      h --done so hare.next!=Null will gives error so take hare!=Null also
# so while hare and hare.next:
###############################
#This can be used for lot of things finding loops
#1 2 3(3 once again connected to 1)
#t
#h
#  t
#h
#    t(met)
#    h
#when started both are same if they both are same somewher in point then there is loop we can use hashmap here
"""Can also be used t find length of loop once both meet keep one pointer in same place iterate another poinetr
with 1 step and count the nxt time they meet the count is given"""#while hare==turtle but before this make sure hare=hare.next so it acn enter loop
"""Can also be used to find starting point in loop
when both meet make turtle =head and incerment both with 1 the nxxt time they meet that is start
take examples and visuize in mind"""
