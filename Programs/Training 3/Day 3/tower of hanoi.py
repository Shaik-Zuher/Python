# Problem link:
#https://www.geeksforgeeks.org/problems/tower-of-hanoi-1587115621/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=bottom_sticky_on_article
#for example
#disks must be moved from source to destination
#n=1
#
#                                       =>
#     1                                                                 1
# ---------  --------- -----------              ---------  --------- -----------
# source     extra       destination            source     extra       destination
#n=2
#
#     1                                 =>                                          =>                                          =>                          1
#     2                                             2          1                                            1         2                                     2
# ---------  --------- -----------              ---------  --------- -----------            ---------  --------- -----------         ---------  --------- -----------
# source     extra       destination            source     extra       destination          source     extra       destination          source     extra       destination
#n=3
#     1                                                                                                                                                                                                                                                                                     1
#     2                                 =>                                          =>              1                           =>                  1                   =>                                      =>                           2          =>                                  2
#     3                                            3            2       1                   3       2                                               2           3               1          2           3                  1                  3                                              3
# ---------  --------- -----------              ---------  --------- -----------        ---------  --------- -----------              ---------  --------- -----------      ---------  --------- -----------        ---------  --------- -----------              ---------  --------- -----------

# source     extra       destination            source     extra       destination       source     extra       destination            source     extra       destination   source     extra       destination      source     extra       destination              source     extra       destination
def tower(n,src,es,des):
    if n==1:
        print("Disk",n,"moved from",src,"to",des)
        return
    tower(n-1,src,des,es)
    print("Disk",n,"moved from",src,"to",des)######src to des because es is preesnt at place of des in main function argument
    tower(n-1,es,src,des)
tower(2,"source","extraspace","destination")

'''
# Below function is responsible for moving 
# n discs from src to dest using extra as temp space
def moveAllDiscs(n, src, extra, dest):
    if n == 1:
        print("Move 1st disc from", src, "to", dest)
        return 
    # Moving all (n - 1) discs from src to extra 
    # using dest as extraSpace
    moveAllDiscs(n - 1, src, dest, extra)
    print("Move", n, "th disc from", src, "to", dest)
    moveAllDiscs(n - 1, extra, src, dest)
 
moveAllDiscs(4, "source", "extraSpace", "destination")
print("\n\n\n\n\n")
'''
