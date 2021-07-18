import pickle

def load_weights(f_name):
    with open(f_name, "rb") as f :
        network = pickle.load(f)

    return network
