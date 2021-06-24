import numpy as np
my_array=np.array([])

i=0
while i<6:
    number=int(input("Enter Numbers: "))
    i+=1
    my_array=np.append(my_array,number)
    

print( my_array)
print("Size of the memory occupied by the  array:")
print("%d bytes" % (my_array.size * my_array.itemsize))