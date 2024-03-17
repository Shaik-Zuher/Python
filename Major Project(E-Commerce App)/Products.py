from Orders import *
def shopping():
    while(1):
        pro=input("1.Electronics\n2.Groceries\n3.Textiles\n4.My Cart\n5.Exit\nEnter product you want to visit:")
        if(pro=="1" or pro=="Electronics" or pro=="electronics"):
            print("Welcome To Electronics.")
            choice=input("1.Mobiles\n2.Watches\n3.Laptops\nWhat Do You Want To Visit:")
            if(choice=="1" or choice=="Mobiles" or choice=="mobiles"):
                mob.display()
            elif(choice=="2" or choice=="Watches" or choice=="watches"):
                wat.display()
            elif(choice=="3" or choice=="Laptops" or choice=="laptops"):
                lap.display()
            else:
                print("Invalid")
        elif(pro=="2" or pro=="Groceries" or pro=="groceries"):
            print("Welcome To Groceries.")
            choice=input("1.Vegetables\n2.Fruits\n3.Oils\nWhat Do You Want To Visit:")
            if(choice=="1" or choice=="Vegetables" or choice=="vegetables"):
                veg.display()
            elif(choice=="2" or choice=="Fruits" or choice=="fruits"):
                fru.display()
            elif(choice=="3"or choice=="Oils" or choice=="oils"):
                oil.display()
            else:
                print("Invalid")
        elif(pro=="3" or pro=="textiles" or pro=="Textiles"):
            print("Welcome To Textiles.")
            choice=input("1.Men's Wear\n2.Women's Wear\n3.Kids Wear\nWhat Do You Want To Visit:")
            if(choice=="1"or choice=="Men's Wear" or choice=="men's wear" or choice=="mens wear" or choice=="Men's wear" or choice=="men's Wear"):
                m.display()
            elif(choice=="2"or choice=="Women's Wear" or choice=="women's wear" or choice=="womens wear" or choice=="Women's wear" or choice=="women's Wear"):
                w.display()
            elif(choice=="3"or choice=="Kids Wear"  or choice=="kids wear" or choice=="Kids wear" or choice=="kids Wear"):
                k.display()
            else:
                print("Invalid")
        elif(pro=="4" or pro=="My Cart" or pro=="My cart" or pro=="my cart" or pro=="my Cart"):
            print("Items in cart:",carty.items)
            print("Number of Items in cart:",carty.cart)
            print("Your bill of Items in your cart:",carty.total)            
        elif(pro=="5" or pro=="Exit" or pro=="exit"):

            print("Thanks For Shopping.\nSee you on Next Visit.")
            break
        else:
            print("Invalid")