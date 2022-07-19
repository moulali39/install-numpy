import numpy as np
# a=np.array([[10,20,30],
#             [50,70,80]])
# b=np.array([[20,40,50],
#              [40,60,80]])
# c=a+b
# d=a*b
# e=a-b
# f=3*a           
# print(c)
# print(d)
# print(e)
# print(f)


# g=np.eye(2)
# print(g)
# h=np.eye(2,dtype=int)
# print(h)
# i=np.eye(3,dtype=int)
# print(i)
# h=np.array([x for x in range(9)])
# i=h.reshape((3,3))
# print(i)
# i=np.array([x for x in range(25)])
# j=i.reshape((5,5))
# print(j)
# k=np.eye(3)
# print(k)
# p=np.array([3.4,5.6,8.9,5.7])
# q=p.astype(int)
# print(q)
# a=np.array([[1,2,3,5],
#              [5,6,7,8]])
# b=np.array([[7,8,9,10],
#             [3,4,5,6]]) 
# c=np.hstack((a,b))             
# print(c) 
# a=np.array([[1,2],
#              [3,4],
#               [5,6]]) 
# b=np.array([[4,5],
#              [5,7], 
#               [7,8]]) 
# c=np.vstack((a,b)) 
# print(c)                   
# x=[x for x in range(6,30,2)]
# y=np.array(x)
# print(y)
# y=np.arange(2,30,1)
# print(y)
# a=np.array([1,2,3,4])
# b=np.array([1,2,4,5])
# c=np.where(a == b)
# print(c)
# a=np.full((3,3),7)
# # print(a)
# a=np.array([1,2,3,4])
# b=np.array([1,2,3,5])
# c=np.where(a == b)
# print(c)
# a=np.array([[1,2,3],
#             [4,5,6],
#             [4,5,6]])
# b=np.array([[4,5,6],
#             [5,6,7],
#             [6,7,8]]) 
# c=a@b
# print(c)            
a=np.array([[1,2,3],
            [4,5,6],
            [6,7,8]])
b=a.T            
print(b)