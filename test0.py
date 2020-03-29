import numpy as np

def vec_seqs(seqs, dim = 100):
    rslts = np.zeros((len(seqs), dim))
    for i, seq in enumerate(seqs):
        rslts[i, seq] = 1.
    return rslts

x = [3, 1, 5]
x_vec = vec_seqs(x, 10)

print(x_vec)
