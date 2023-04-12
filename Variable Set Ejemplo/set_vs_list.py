import time


list_1 = list(range(10000000))
set_1 = set(list_1)

#VARIABLE LIST
a = time.time()
print (8452294 in list_1)
b = time.time()-a

#VARIABLE SET
a_1 = time.time()
print (8452294 in set_1)
b_1 = time.time()-a_1

print ("Tiempo con LIST: {}".format(b))
print ("Tiempo con SET: {}".format(b_1))

raw_input()
