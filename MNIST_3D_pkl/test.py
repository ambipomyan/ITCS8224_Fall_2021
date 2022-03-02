import pickle
import cv2
import numpy as np
import os

'''
# pkl data pre-view
f = open('preview/atlas.pkl', 'rb')
data = pickle.load(f)
print(type(data))
print(data)
print('\n')
'''

'''
# DIR-LAB image pre-view
f = open('preview/case1_T00_s.img', 'rb')
data = np.fromfile(f, np.dtype('int16'))
data = data.reshape(94,256,256) # 4DCT1: 256x256x94, but not quite sure that if the data type is int16?
print(data)
print('\n')
'''

'''
' try to create data for pre-train model: 2D to 3D, based on MNIST
' ONE atlas
' 100 train
' 20  validation
' 10  test
'''

# DIR-LAB image pre-view
f = open('Images/case1_T40_s.img', 'rb')
data = np.fromfile(f, np.dtype('int16')) #???
data = data.reshape(94,256,256)
z = 94
y = 192
x = 224

'''
print(data[0])
print('\n')
print(type(data[0]))

for pics in range(100,110):
    cv2.imwrite('case10_slice'+str(pics)+'.jpg', data[pics])

# atlas
arr = np.zeros((160, 192, 224), np.dtype('float32'))

for i in range(28):
    arr[i,1:29,1:29] = cv2.imread('atlas.jpg', 0)
#print(arr)
'''
# write tuple to pkl
file_to_go = 'Images/case1_T40_s.pkl'

f = open(file_to_go, 'wb')
list_to_go = [[[ [0 for col1 in range(224)] for col2 in range(192)] for row in range(160)] for ind in range(2)]

for i in range(x):
    for j in range(y):
        for p in range(z):
            list_to_go[0][p][j][i] = data[p,j,i]
                
for i in range(x):
    for j in range(y):
        for p in range(z):
            list_to_go[1][p][j][i] = data[p,j,i]

tuple_to_go = tuple(np.array(list_to_go, np.dtype('float32')))

pickle.dump(tuple_to_go, f)
f.close()

'''
# check
f = open('train/50750.jpg.pkl', 'rb')
data = pickle.load(f)
print(type(data)) #should be tuple
print(data[0][0])
'''

# for train, val and test folders
train_folder = 'train/'
val_folder = 'val/'
test_folder = 'test/'

'''
l_train = os.listdir(train_folder)
for index in range(100):
    for i in range(28):
        arr[i,1:29,1:29] = cv2.imread('train/'+l_train[index], 0)

    # write tuple to pkl
    file_to_go = 'train/'+l_train[index]+'.pkl'

    f = open(file_to_go, 'wb')

    for i in range(28):
        for j in range(28):
            for p in range(28):
                list_to_go[0][p][j][i] = arr[p,j,i]
                    
    for i in range(28):
        for j in range(28):
            for p in range(28):
                list_to_go[1][p][j][i] = arr[p,j,i]

    tuple_to_go = tuple(np.array(list_to_go, np.dtype('float32')))

    pickle.dump(tuple_to_go, f)
    f.close()

l_val = os.listdir(val_folder)
for index in range(20):
    for i in range(28):
        arr[i,1:29,1:29] = cv2.imread('val/'+l_val[index], 0)
    #print(arr)

    # write tuple to pkl
    file_to_go = 'val/'+l_val[index]+'.pkl'

    f = open(file_to_go, 'wb')

    for i in range(28):
        for j in range(28):
            for p in range(28):
                list_to_go[0][p][j][i] = arr[p,j,i]
                    
    for i in range(28):
        for j in range(28):
            for p in range(28):
                list_to_go[1][p][j][i] = arr[p,j,i]


    tuple_to_go = tuple(np.array(list_to_go, np.dtype('float32')))

    pickle.dump(tuple_to_go, f)
    f.close()

l_test = os.listdir(test_folder)
for index in range(10):
    for i in range(28):
        arr[i,1:29,1:29] = cv2.imread('test/'+l_test[index], 0)

# write tuple to pkl
    file_to_go = 'test/'+l_test[index]+'.pkl'

    f = open(file_to_go, 'wb')

    for i in range(28):
        for j in range(28):
            for p in range(28):
                list_to_go[0][p][j][i] = arr[p,j,i]
                
    for i in range(28):
        for j in range(28):
            for p in range(28):
                list_to_go[1][p][j][i] = arr[p,j,i]

    tuple_to_go = tuple(np.array(list_to_go, np.dtype('float32')))

    pickle.dump(tuple_to_go, f)
    f.close()

# 1, 0, 5, 2, 6, 1, 7, 96
'''
