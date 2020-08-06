mydict = {"first":"bhN",
   "second":"k",
   "third":"cHt"
   }
'''
print(mydict)
print(mydict["first"])
print(mydict.get("first"))
#mydict["first"]= "m"
print(mydict)
print(mydict.get("a")) #gives vaule of given key
dict2={
    1:"a",
    2:"b"
}
print(dict2)
dict2[1]="c"
print(dict2)
dict2[3]="d"#updated
print(dict2) 
dict2.pop(1) #removed 
print(dict2)
# print(dict2.popitem()) #kuch bhi
print()
dict.update({4:"i"}) #update/add new value
'''
# print(len(mydict))
# print(mydict.keys()) #tells all keys of dictionary
# mydict.update({1:"abc"})

# print(mydict.values()) #tells all values from dictionary
print(mydict.setdefault("first",1))
print(mydict)