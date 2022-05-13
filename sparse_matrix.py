#import
from scipy import sparse 

#create 
sparse_matrix = sparse.csc_matrix(numpy_array) 
sparse_matrix = sparse.csc_matrix(numpy_matrix) 
#save 
sparse.save_npz('file name.npz', sparse_matrix) 
#load 
sparse_matrix = sparse.load_npz('/tmp/sparse_matrix.npz') 
