thislist = ["a", "b", "a", "c", "c"]
#convert to dictionary
thislist = list( dict.fromkeys(thislist) )
print(thislist)