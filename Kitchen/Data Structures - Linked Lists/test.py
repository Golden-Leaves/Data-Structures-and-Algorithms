obj1 = {"12": "近一和"}
obj2 = obj1
del obj1 #obj1 doesn't get deleted since there is sitll a reference(obj2) pointing to it
print(2,obj2)