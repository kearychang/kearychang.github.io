import random

category = ["planet","comet","asteroid","moon"]
planet = ["mercury", "venus", "mars", "jupiter", "saturn", "neptune", "uranus"]
comet = ["P/", "C/", "X/", "D/"]
asteroid = ["AXQ/", "DQV/", "VKO/", "UUW/"]
moon = ["deimois", "phobos", "luna", "io", "europa", "ganymede", "callisto", "mimas", "enceladus"]


#planet
for e in range(len(planet)):
    itemTitle = planet[e]
    itemText = "Prime estate on " + itemTitle
    itemPrice = str(random.randint(1000000,4000000)/100)
    itemCategory = "planet"
    itemPicture = itemTitle + ".jpg"
    itemStatement = "insert into Place(title,price,text,category,picture) values ("
    itemStatement2 = str((",").join(list(map(lambda e: "'" + e + "'", [itemTitle, itemPrice, itemText, itemCategory, itemPicture]))))
    print(itemStatement + itemStatement2 + ");") 

#moon
for e in range(len(moon)):
    itemTitle = moon[e]
    itemText = "Prime estate on " + itemTitle
    itemPrice = str(random.randint(500000,2000000)/100)
    itemCategory = "moon"
    itemPicture = itemTitle + ".jpg"
    itemStatement = "insert into Place(title,price,text,category,picture) values ("
    itemStatement2 = str((",").join(list(map(lambda e: "'" + e + "'", [itemTitle, itemPrice, itemText, itemCategory, itemPicture]))))
    print(itemStatement + itemStatement2 + ");") 


#asteroid
for e in range(len(asteroid)):
    for i in range(random.randint(2,5)):
        itemTitle = asteroid[e] + str(random.randint(100,999))
        itemText = "Prime estate on " + itemTitle
        itemPrice = str(random.randint(1000000,3000000)/100)
        itemCategory = "asteroid"
        itemPicture = itemCategory + str(e+1) + ".jpg"
        itemStatement = "insert into Place(title,price,text,category,picture) values ("
        itemStatement2 = str((",").join(list(map(lambda e: "'" + e + "'", [itemTitle, itemPrice, itemText, itemCategory, itemPicture]))))
        print(itemStatement + itemStatement2 + ");") 

#comet
for e in range(len(comet)):
    for i in range(random.randint(2,5)):
        itemTitle = comet[e] + str(random.randint(10,99))
        itemText = "Prime estate on " + itemTitle
        itemPrice = str(random.randint(1500000,3500000)/100)
        itemCategory = "comet"
        itemPicture = itemCategory + str(e+1) + ".jpg"
        itemStatement = "insert into Place(title,price,text,category,picture) values ("
        itemStatement2 = str((",").join(list(map(lambda e: "'" + e + "'", [itemTitle, itemPrice, itemText, itemCategory, itemPicture]))))
        print(itemStatement + itemStatement2 + ");") 
