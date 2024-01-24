from random import randint

def roll(n=1,d=20,show=False):

    rolls = []
    total = 0

    for i in range(n):
        roll = randint(1,d)
        rolls.append(roll)
        total = total + roll

    if show:
        return(total,rolls)
    else:
        return(total)
