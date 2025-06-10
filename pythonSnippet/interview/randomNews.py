import random
import datetime

status = ["urgent", "update", "none"]
title = ["warning to customer", "sale", "no news"]
text = ["meteor shower", "50% off moons!", "slow day"]
start_date = datetime.datetime(year=2050,month=1,day=1,hour=0,minute=0,second=0)

for i in range(99):
    n = random.randint(0,2)
    itemDate = start_date + datetime.timedelta(seconds=random.randint(0,3839508000))
    itemValue = "'" + "','".join([status[n],title[n],text[n],str(itemDate)]) + "'"    
    itemStatement = "insert into News(status,title,text,date_time) values ("    
    print(itemStatement + itemValue + ");") 
