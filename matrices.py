import numpy as np

data = np.array([[1,2,3],[4,5,6],[7,8,9]])
trans_data = np.transpose(data)
print ("data is", data)
if data.shape[0] > 1:
    print "This is a matrix"
