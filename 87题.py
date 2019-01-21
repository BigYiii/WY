#列表转换为字典
#方法1
list1 = ['key1','key2','key3']
list2 = ['1','2','3']
a=dict(zip(list1,list2))
print(a)

#方法2
new_list= [['key1','value1'],['key2','value2'],['key3','value3']]
print(dict(new_list))


#方法3
list3= [['key1','value1'],['key2','value2'],['key3','value3']]
new_dict = {}
for i in list3:
    new_dict[i[0]] = i[1]
print(new_dict)
