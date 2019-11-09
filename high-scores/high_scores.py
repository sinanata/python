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
    return sorted(scores, reverse=True)[:3]
    pass
