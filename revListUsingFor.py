orig_list=[1, 3, "Monu","Sonu","Golu"]
new_list=[]
for i in range(len(orig_list)-1,-1,-1):
    new_list.append(orig_list[i])
print(new_list)