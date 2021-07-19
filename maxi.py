def number():
    numbers = [3, 5, 7, 34, 2, 89, 2, 5]
    a=numbers[0]
    i=0
    while i<len(numbers):
        if numbers[i]>a:
            a=numbers[i]
        i=i+1
    print(a)
number() 

# def number():
#     numbers = [1, 2, 3, 4, 5]
#     sum=0
#     i=0
#     while i<len(numbers):
#         sum=sum+numbers[i]
#         i=i+1
#     print(sum)
# # number()

# def unorder_list():
#     unorder_list = [6, 8, 4, 3, 9, 56, 0, 34, 7, 15] 
#     print(unorder_list)
#     i=0
#     while i<len(unorder_list):
#         j=0
#         while j<i:
#             if unorder_list[i]<unorder_list[j]:
#                 a=unorder_list[i]
#                 unorder_list[i]=unorder_list[j]
#                 unorder_list[j]=a
#             j=j+1
#         i=i+1
#     print(unorder_list)
# unorder_list()

# def reverse_list():
#     alphabet = ["Z", "A", "A", "B", "E", "M", "A", "R", "D"]
#     a=reversed(alphabet)
#     l=[]
#     i=0
#     for i in a:
#         l.append(i)
#     print(l)
# reverse_list()

# def min():
#     list = [8, 6, 4, 8, 4, 50, 2, 7]
#     i=0
#     a=list[0]
#     while i<len(list):
#         if list[i]<a:
#             a=list[i]
#         i=i+1
#     print(a)
# min()

    



































