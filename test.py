mydict = {1:"a",2:"w,",3:"n"}
print(mydict.get(4))
'''
.get() returns a 

'''
print(mydict.get(2))

print(mydict[3])
mydict[2]="w"
mydict.update({4:"i"}) #update/add new value
print(mydict)
# mydict.popitem() 
print(mydict)
# print(mydict.values()) get all the values
# print(mydict.items())
# mydict.pop(2) removes item with specified key
# mydict.clear() clears the whole list
# del mydict
a = (1,2,3)
b = "l"


print(mydict.setdefault(4,"ffyc")) #adds value to the dictionary if no value is specified in dictionary AND returns value if it has value or it does nothing
# print(dict.fromkeys(a,b)) #gives dictionary from specified keys and a value
print(mydict)


x = {"rajni":19,"awni":20,"ravi":1,"swas":20.5}
print(max(x, key=x.get)) #get key with max value
a= str(input())
print(x.get(str(a)))

print(type('awni'))






