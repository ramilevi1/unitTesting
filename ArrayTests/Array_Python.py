from array import array
from ctypes import sizeof


def create_array(int):
         array = [] * int
         return array

def print_array(array):
        #print ("The new created array is : ", end =" ")
        for i in range (0, len(array)):
            print (array[i] , end =" ")
        print ('', end ='\n')

def get_size(array):
        size = len(array)     
    #    print(size)
        return size

def check_if_empty(array):
            if not array:
                print("Set is empty")
            else: print("Set is not empty")

def add_item(array, item):
    if check_for_item(array, item):
        array.append(item)
    else:
      print("item already found")

def remove_item(array, item):
    if check_for_item(array, item):
        pass
    else:
      array.remove(item)

def check_for_item(array, item):
    if item not in array:
            return True
    else:
        return False





















# value = 1
# s =(value,)
# print(s)
# print(len(s))
# value2 = 2
# s2 = (value2,)
# s = s + s2
# print(s)
# print(len(s))
# if value in s:
#     print("find")
# else:
#     print("not find")
# value3 = 3
# s3 = (value3,)
# s = s + s3
# print(s)
# print(len(s))
# value4=4
# value5=5
# value6=6
# s4 = (value4,value5,value6,)
# s = s+s4
# print(s)
# print(len(s))

# if 2 in s:
#     print("find")
# else:
#     print("not find")

# s5 = () * 5
# print(s5)
# s5 = (1,2,5,6,7,)
# print(s5)
# s5 = s5+ (8,)
# print(s5)
# print(len(s5))