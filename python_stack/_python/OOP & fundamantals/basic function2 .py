# # Countdown
# newlist = []
# def Countdown(num):
#   for i in range(num, -1, -1):
#     newlist.append(i)
#   return newlist
# print(Countdown(5))

# # Print and Return

# def print_and_return (list):

#     print ( list[0])
#     return list[1]
# print (print_and_return([1,2]))

# #   First Plus Length
# def First_Plus_Length (arr):
#   firstvalue= arr[0]
#   length=len(arr)
#   return firstvalue + length
# print(First_Plus_Length([4,5,6,8]))

# Values Greater than Second

# def greater(list):
#     newlist = []
#     secondvalue = list[1]
#     for i in range(0, len(list)):
#         if (list(i) > secondvalue):
#                  newlist.append(list[i])
#     print(len(newlist))
#     return newlist

# print (greater([2, 3, 4, 5, 6]))

#This Length, That Value
def length_value (size, value):
    newlist=[]
    for x in range(size):
        newlist.append(value)
    return newlist
print(length_value(2,3))

