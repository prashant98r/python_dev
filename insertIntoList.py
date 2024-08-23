orig_list=[10,45,69,88,98,114,120,150]
index=0
num=100
for i in orig_list:
    if i>num:
        index=index
    else:
        index=index+1
print(index)
orig_list.append([None])
for i in range(len(orig_list)-1,index,-1):
    orig_list[i]=orig_list[i-1]
orig_list[index]=num
print(orig_list)