import pickle as pk

def save_data(data,filename):
    f = open(filename,'wb')
    pk.dump(data,f)
    f.close()

def load_data(filename):
    f = open(filename, 'rb')
    data = pk.load(f)
    f.close()
    return data
