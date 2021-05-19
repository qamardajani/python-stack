# Biggie Size 
# def change (array):
#     for i in range (0,len(array)):
#         if array[i] > 0 :
#             array[i] = "big"
    
#     return array
# print (change([-1,-2,4,5]))

# Count Positives
# def count_positive (array):
#     count = 0
#     for x in range (0,len(array)):
#         if array[x] > 0 :
#             count = count + 1
#             array[-1] = count
#     return array
# print (count_positive([1,-2,-3,4,5,6]))
 
# Sum Total
# def sumtotal (arr):
#     sum = 0
#     for i in range (0,len(arr)):
#         sum = sum + arr[i]
#     return sum 
# print (sumtotal([1,2,3,4]))

# Average 
# def average (arr):
#     sum = 0
#     avg = 0
#     for i in range (0,len(arr)):
#         sum = sum + arr[i]
#         avg = sum / len(arr)
#     return avg
# print (average([10,10,10]))

# Length 

# def length (arr):
#     for i in range (0,len(arr)):
        
        
#         return len(arr)
# print (length ([1,2,3]))

#Minimum
# def Minimum (list):
#     min=list[0]
#     for i in range (0,len(list)):
#         if list[i] < min:
#             min=list[i]
#     return min
# print(Minimum ([1,2,3]))

# #Maximum
# def Maximum (list):
#     max=list[0]
#     for i in range (0,len(list)):
#         if list[i] > max:
#             max=list[i]
#     return max
# print(Maximum ([1,2,3]))

# #Ultimate Analysis
# def Ultimate_Analysis(arr):
#     dictionary = {
#         "sumtotal": sum(arr),
#         "average": sum(arr) / len(arr),
#         "minimum": min(arr),
#         "maximum": max(arr),
#         "length": len(arr),
#     }
#     return dictionary

# arr = [37,2,1,-9]
# print(Ultimate_Analysis(arr))

# #Reverse List
# def Reverse_List(arr):
#     for i in range (int (len(arr)/2)):
#         arr[i],arr[len(arr)-1 -i] = arr[len(arr)-1 -i],arr[i]
#     return arr
# print(Reverse_List([37,2,1,-9]))
