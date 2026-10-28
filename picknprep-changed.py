# MySQL setup is required to run the original project.
# Database connection code is not included in this public version.
receipt={}
#CREATING SQL TABLES REQUIRED AND INSERTING VALUES:
#mycursor.execute("create table main_menu(item_no int,dish_name varchar(50),price int)")
#mydb.commit()
#mycursor.execute("insert into main_menu values(1,'Biriyani',8),(2,'Naan',3),(3,'Butter Chicken',7),(4,'Shawarma',12),(5,'Sandwich',9)")
#mydb.commit()
#mycursor.execute("create table beverages(item_no int,drink_name varchar(20),price int)")
#mydb.commit()
#mycursor.execute("insert into beverages values(1,'Soft Drinks',2),(2,'Tea',1),(3,'Coffee',3),(4,'Falooda',3),(5,'Ice Cream',2)")
#mydb.commit()
#mycursor.execute("create table my_recipes(dish_name varchar(50),ing_1 varchar(30),ing_2 varchar(30),ing_3 varchar(30),price int,memory varchar(30),notes varchar(255)")
#mydb.commit()
def menu(): #Menu option
    try:
        print("\nMain Dishes:") #MAIN DISHES
        mycursor.execute("select * from main_menu")
        mainmenu=mycursor.fetchall()
        for i in mainmenu:
            print(str(i[0])+'. '+str(i[1])+' - $'+str(i[2]))
        print("\nEnter the item no. of the dishes you want to order (separated by commas)\nOr enter zero to skip")
        maindish1=input("-> ")
        maindish=maindish1.split(",")
        print("\nYOU ORDERED:")
        checkm='T'
        for i in maindish:
            if i.strip() not in ('0','1','2','3','4','5'):
                checkm='F'
                break
            if checkm=='T':
                for i in maindish:
                    if i.strip()=='1':
                        receipt['Biriyani']=[8,1]
                        print(mainmenu[0][1],"- $8")
                    elif i.strip()=='2':
                        receipt['Naan']=[3,1]
                        print(mainmenu[1][1],"- $3")
                    elif i.strip()=='3':
                        receipt['Butter Chicken']=[7,1]
                        print(mainmenu[2][1],"- $7")
                    elif i.strip()=='4':
                        receipt['Shawarma']=[12,1]
                        print(mainmenu[3][1],"- $12")
                    elif i.strip()=='0':
                        print("None from main dish")
                    else:
                        receipt['Sandwich']=[9,1]
                        print(mainmenu[4][1],"- $9")
        if checkm=='F':
            print("None... \ndue to invalid item no. entered")
            print("\nPlease try again")
            menu()
            print("*"*20)
        beverages()
    except:
        print("\nAn error occured due to invalid input. Please input appropriate values only")
        print("Try again")
        menu()
def beverages():
    try:
        print("\nBeverages:") #BEVERAGES
        mycursor.execute("select * from beverages")
        bev=mycursor.fetchall()
        for i in bev:
            print(str(i[0])+'. '+str(i[1])+' - $'+str(i[2]))
        print("\nEnter the item no. of dishes you want to order (separated by commas)\nOr enter zero to skip")
        bever1=input("-> ")
        bever=bever1.split(",")
        checkb='T'
        print("\nYOU ORDERED:")
        for i in bever:
            if i.strip() not in ('0','1','2','3','4','5'):
                checkb='F'
                break
            if checkb=='T':
                for i in bever:
                    if i.strip()=='1':
                        receipt['Soft Drinks']=[2,1]
                        print(bev[0][1],"- $2")
                    elif i.strip()=='2':
                        receipt['Tea']=[1,1]
                        print(bev[1][1],"- $1")
                    elif i.strip()=='3':
                        receipt['Coffee']=[3,1]
                        print(bev[2][1],"- $3")
                    elif i.strip()=='4':
                        receipt['Falooda']=[3,1]
                        print(bev[3][1],"- $3")
                    elif i.strip()=='0':
                        print("None from beverages")
                    else:
                        receipt['Ice Cream']=[2,1]
                        print(bev[4][1],"- $2")
        if checkb=='F':
            print("None selected due to invalid item no. entered")
            print("\nPlease try again")
            beverages()
        print("*"*20)
        ch5=input("\nDo you want to order more? (y/n):").lower()
        if ch5=='y':
            select()
        elif ch5=='n':
            purchase()
        else:
            print("\nInvalid data entered. Redirecting to purchase...")
            purchase()
    except:
        print("\nAn error occured due to invalid input. Please input appropriate values only")
        print("Try again")
        beverages()
def custom(): #Custom recipe
    try:
        print("\n1. Order from my recipes\n2. Add my recipes")
        c1=int(input("(1/2) -> "))
        if c1==1:
            customorder()
        elif c1==2:
            custommake()
        else:
            print("\nInvalid choice")
            print("Defaulting to 'order from my recipes'")
            customorder()
    except:
        print("\nAn error occured due to invalid input. Please input appropriate values only")
        print("Try again")
        custom()
def custommake(): #Custom creating
    try:
        print("\nCraft your own recipe!")
        cstname = input("Recipe name: ")
        ing1 = input("Enter main ingredient 1: ")
        ing2 = input("Enter main ingredient 2: ")
        ing3 = input("Enter main ingredient 3: ")
        print("\nChoose meal type:\n1.Festival meal\n2.Comfort meal")
        mem=int(input("(1/2) -> "))
        if mem==1:
            memory="Festival meal"
        elif mem==2:
            memory="Comfort meal"
        else:
            memory="None"
        print("\nWhy is this meal special to you (optional)")
        special=input("Type here or press enter to skip - ")
        print("\nAny extra notes you want to add for the recipe? (ex: 'top with dark chocolate')")
        notes=input("Type here or press enter to skip - ").strip()
        if notes=="":
            notes="None"
        price = int(input("\nSuggested price ($10-$25): $"))
        if price < 10 or price > 25:
            print("Unrealistic price. Setting it to $15 by default.")
            price = 15
        q1 = "INSERT INTO my_recipes VALUES ('{}', '{}', '{}', '{}', {},'{}','{}')".format(cstname, ing1, ing2, ing3, price,memory,notes)
        mycursor.execute(q1)
        mydb.commit()
        print("\nRecipe recorded! May it bring back the taste from your memories...")
        customorder()
    except:
        print("\nAn error occured due to invalid input. Please input appropriate values only")
        print("Try again")
        custommake()
def customorder(): #CUSTOM ORDER
    try:
        mycursor.execute("select * from my_recipes")
        cstrcp=mycursor.fetchall()
        if len(cstrcp)!=0:
            print("\n--MY RECIPES--")
            for i in cstrcp:
                print(str(cstrcp.index(i)+1)+". "+i[0])
                print("Price: $"+str(i[4])+"| Notes: "+i[6])
                print("-"*25)
        else:
            print("\nNo recipes added. Please add recipes")
            custommake()
        print("\nEnter the item numbers of the recipes to add to order (separated by commas)")
        custom1=input("-> ")
        custom=custom1.split(",")
        check='T'
        for i in custom:
            if int(i)>len(cstrcp) or int(i)==0:
                check='F'
                break
        if check=='T':
            for i in custom:
                index=int(i)-1
                dish=cstrcp[index][0]
                dishprice=cstrcp[index][4]
                receipt[dish]=[dishprice,1]
                print("-- ",dish," added to your order")
        if check=='F':
            print("\nINVALID ITEM NO. ENTERED. PLEASE TRY AGAIN")
            customorder()
        ch6=input("\nDo you want to order more (y/n): ").lower()
        if ch6=='y':
            select()
        elif ch6=='n':
            purchase()
        else:
            print("\nINVALID DATA ENTERED. Redirecting to purchase...")
            purchase()
    except:
        print("\nAn error occured due to invalid input. Please input appropriate values only")
        print("Try again")
        customorder()
def homepage(): #HOMEPAGE
    print()
    for i in range(115):
        print("=",end=".")
    print()
    with open("logo.txt", "r") as file: #Accessing logo from text file
        for line in file:
            print(" "*89,end=line.rstrip())
            print()
    print()
    for i in range(115):
         print("=",end=".")
    print()
    print(" "*85+"""=====_____-----ONLINE FOOD SERVICE-----_____=====""")
    print("\n ****GREETINGS****") #Opening message
    print(''' Welcome to PicknPrep, an online food ordering service which helps you to order meals and beverages,
    a one stop shop for all your favourite meals, even for your personal recipes.''')
    print(" We offer choices you see nowhere else. On this platform, you can make your own custom meals to add to your custom menu!")
    select()
def select(): #INITIAL CHOICES OFFERED
    try:
        print("\n Choose from the options below to take a look at the great features we provide!")
        print(" 1. Show Main Menu")
        print(" 2. Custom Recipes")
        c0=int(input("\n What is your choice (1/2):"))
        if c0==1:
            menu()
        elif c0==2:
            custom()
        else:
            print("\nInvalid choice")
            print("Showing menu instead...")
            menu()
    except:
        print("\nAn error occured due to invalid input. Please input appropriate values only")
        print("Try again")
        select()
def purchase(): #CHANGING QUANTITY
    try:
        print("\n***YOUR CURRENT ORDER***")
        for i in receipt:
            print(str(i)+' Qty:'+str(receipt[i][1]))
        print('*'*25)
        ch4=input("\nDo you want to update the quantity of any item? (y/n) :")
        if ch4.lower()=='y':
           qtyno=int(input("\nEnter the number of items you want to change quantity of: "))
           if qtyno<=len(receipt):
                for i in range(qtyno):
                    rndmno=0
                    qtynm1=input("\nEnter the name of the item to change quantity: ").strip()
                    qtynm=qtynm1.lower()
                    for i in receipt:
                            if i.lower()==qtynm:
                                newqty=int(input("Enter new quantity: "))
                            if newqty>0:
                                receipt[i][1]=newqty
                                rndmno=1
                            else:
                                print("\nUnrealistic quantity. Setting quantity to 1")
                                rndmno=1
                    if rndmno==0: #IF ITEM NOT FOUND IN DICTIONARY WHEN CHANGING QUANTITY
                        print("\nItem not found")
                bill()
           else:
                print("\nInvalid data entered. No changes made to quantity")
                bill()
        elif ch4.lower()=='n':
            bill()
        else:
            print("\nInvalid data entered. No changes made to quantity")
            bill()
    except:
        print("\nAn error occured due to invalid input. Please input appropriate values only")
        print("Try again")
        purchase()
def bill(): #PRINTING FINAL BILL
    print("\n ---YOUR RECEIPT---")
    total=0
    for i in receipt:
        prc=receipt[i][0]*receipt[i][1]
        print(str(i)+' $'+str(receipt[i][0])+" x "+str(receipt[i][1])+" = $"+str(prc))
        total+=prc
    print("-"*25)
    print('Grand total = $'+str(total))
    homepage()
    print("\n***Thank you for choosing PicknPrep. We hope you had a great purchase***")