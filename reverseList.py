name_list=["Mohan","Sonu","Monu","Lolu"]
index =len(name_list)-1
new_list=[]
while index>=0:
    new_list.append(name_list[index])
    index-=1
print(new_list)