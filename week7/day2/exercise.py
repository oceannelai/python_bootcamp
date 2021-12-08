 #PART 1- BASIC
# PLEASE SOLVE THE FOLLOWING EXERCISES GOOD LUCK!
# 1
import numpy as np
# print(np.__version__)
#2
vectors = np.zeros(10)
# print(x)
# 3
# print(vectors.size * vectors.itemsize)
# 4
# print(np.info(np.add))
# 5
# print('update fifth value to 1')
# vectors[5]=1
# 6
# print(vectors)
# 7
v = np.arange(10,50)
# print(v)
# 8
vr=v[::-1]
# print(vr)
#9
matrix = np.arange(0,9).reshape(3,3)
# print(matrix)
# 10
arr =[1,2,0,0,4,0]
kale =np.nonzero(arr)
# print(kale)
# 11
matrix2 = np.identity(3)
# print(matrix2)
# 12
matrix3 = np.random.random((3,3,3))
# print(matrix3)
# 13
array =np.random.random((10,10))
# print(array.max())
# print(array.min())
# 14
house = np.random.random(30)
# print(house.mean())

# 15
x = np.ones((4,4))
x[1:-1,1:-1] = 0
# print(x)
# 16
x = np.pad(x, pad_width=1, mode='constant', constant_values=8)
# print(x)
# 17
exp_1=0 * np.nan  #result is NAN
exp_2=np.nan == np.nan #result is False
exp_3=np.inf > np.nan #result is False
exp_4=np.nan - np.nan #result is NAN
exp_5=0.3 == 3 * 0.1 #result is False
# print(exp_5)

# 18
matrix5 = np.diag((1,2,3,4,7))
# print(matrix5)

# 19
checker = np.zeros((8,8))
checker[1::2,::2] = 1 #every 2 index for the odd rows will be 1
checker[::2,1::2] = 1 #every 2 index for the even rows will be 1
# print(checker)

# 20
# print (np.unravel_index(100, (6,7,8)))
#21
checkers = np.array([[0,1], [1,0]])
checkers = np.tile(checkers,(4,4))
# print(checkers)

#22
matrix7 = np.random.random((5,5))
max = matrix7.max()
min = matrix7.min()
subtract1 = matrix7 - matrix7.min()
subtract2 = matrix7.max() - matrix7.min()
# print(subtract1/subtract2)


# 23
# color = np.dtype([("r", np.ubyte, 1),
# ("g", np.ubyte, 1),
# ("b", np.ubyte, 1),
# ("a", np.ubyte, 1)])
# print(color)

# 24
matrix8 =np.array((5,3))
matrix9 = np.array((3,2))
dot_product = np.dot(matrix8, matrix9)
# print(dot_product)

# 25
array3= np.arange(11)
array3[(3<array3) & (array3<=8)] *= -1
# print(array3)

# 26
Author: 'Jake VanderPlas '
# print(sum(range(5),-1)) =9
from numpy import *
# print(sum(range(5),-1)) =10

# 27
# Z**Z #legal
#  Z<-Z #not legal
# 1j*Z #not legal

# 28
# np.array(0)/ np.array(0) #float
# np.array(0)//np.array(0) #integer


# 29
vector_ceil = np.random.rand(10)
# print(np.copysign(vector_ceil, -1))
# print(np.ceil(vector_ceil))

# 30
arr1 = np.array([1,2,3,4])
arr2 = [2,4,6,8]
# print(np.intersect1d(arr1,arr2))
# 31
#31
set = np.seterr(all='ignore')
np.geterr()
# arr = np.int16(32000) * np.int16(3)
# print(arr)

#32
#np.sqrt(-1) == np.emath.sqrt(-1)  #False

#33
yesterday = np.datetime64('today', 'D') - np.timedelta64(1, 'D')
# print(yesterday)
today = np.datetime64('today', 'D')
# print(today)
tomorrow = np.datetime64('today', 'D') + np.timedelta64(1, 'D')
# print(tomorrow)

#34
Z = np.arange('2016-08', '2016-09', dtype='datetime64[D]')
# print(Z)

#35
A = np.ones(3)*1
B = np.ones(3)*2
C = np.ones(3)*3
# print(np.add(A,B,out=B))
# print(np.divide(A,2,out=A))
# print(np.negative(A,out=A))
# print(np.multiply(A,B,out=A))

#36
Z = np.random.uniform(0,10,10)
# print (Z - Z%1)
# print (np.floor(Z))
# print (np.ceil(Z)-1)
# print (Z.astype(int))
# print (np.trunc(Z))

#37
arr5 = np.zeros((5,5))
arr5 += np.arange(5)
# print(arr5)

#39
arr6 = np.linspace(0,1,12,endpoint=True)[1:-1]
# print(arr6)

# 40
rat = np.random.random(10)
rat.sort()
# print(rat.sort())

#---------------------------------------------------
#panda basic
# 1
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
import pandas as pd
# 2,3
url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'
chipo = pd.read_csv(url, sep = '\t')
# 4
# print(chipo.head(10))
# 5
# print(chipo.shape[0])
# 6
# print(len(chipo.columns))
# 7
# print(chipo.columns.values)

#8
def num_float(x):
    return float(x[1:-1])
chipo.item_price = chipo.item_price.apply(num_float)
# print(chipo.head())

# 9
canned_soda = chipo.loc[chipo['item_name']=='Canned Soda',:]
# print(canned_soda.loc[canned_soda['quantity'] > 1,'quantity'].count())

# 10
# print(chipo.groupby('order_id').count()['quantity'])

# 11

# 12
# print(chipo['quantity'].sum())


# 13


# 14


