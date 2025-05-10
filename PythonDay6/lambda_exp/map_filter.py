


list1 = ["king","smith","tom","javeed","arihaan","jim"]

##myfilter  = filter(lambda s1: len(s1) > 4 , list1)

#print(list(myfilter))

mymap  =  map(lambda x: len(x) ,   filter(lambda s1: len(s1) > 4 , list1))   

print(list(mymap))

