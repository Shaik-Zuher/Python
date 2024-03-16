#creating list
luffy=[1,2,"kalyan"]
#access list
print(luffy)
print(luffy[2])
#slicing
monkey=luffy
monkey=monkey[1:2]
print(monkey)
#loops acessing
for i in range(0,len(luffy)):
    print(luffy[i])
#append
n=input("Enter value:")
luffy.append(n)
print(luffy)
#insert
monkey.insert(1,"d")
print(monkey)
#update the value
monkey[1]="Pirate"
#multi
multi=[luffy,monkey]
print(multi)
for j in range(0,len(multi)):
    print(multi[j])
print(multi[0][0])

