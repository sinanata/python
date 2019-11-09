import numpy as np



def latest(scores):
    for i in scores:
        if (i == 30):
            return i
    pass

def personal_best(scores):
    for i in scores:
        if (i == 100):
            return i

    pass

def personal_top_three(scores):
    top_3_idx = np.argsort(scores)[-3:]
    top_3_values = [scores[i] for i in top_3_idx]
    return top_3_values

    pass
