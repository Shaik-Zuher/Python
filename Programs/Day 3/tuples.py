#creating
'''
tuple=(1,"string",45,1)
print(tuple)
tuple=tuple+(9,8)
print(tuple)
print(tuple[0])
for i in range(0,5):
    n=int(input("Enter values:"))
    tuple=tuple+(n,)
    '''
#dictonaries
dict={"key":"value",104:106,"104":"suresh","place":97}
print(dict)
#accessing
print(dict["key"])
print(dict[104])
print(dict["104"])
#accessing through loop
for i in dict:
    print(dict[i])
#duplicate keys in dict during creation and looping
dicti={"key":"value",104:106,104:"suresh","key":97}
for i in dicti:
    print(dicti[i])
#duplicate values in dict during creation and looping
dicti={"key":"value",104:106,"104":106,"key":97}
print(dicti)
#delete value in dict
a=del dicti[0]
