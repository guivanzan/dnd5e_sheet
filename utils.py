from random import randint

def d4(n=1):

    rolls = []
    total = 0

    for i in range(n):
        roll = randint(1,4)
        rolls.append(roll)
        total = total + roll

    return (total, rolls)

def d6(n=1):

    rolls = []
    total = 0

    for i in range(n):
        roll = randint(1,6)
        rolls.append(roll)
        total = total + roll

    return (total, rolls)

def d8(n=1):

    rolls = []
    total = 0

    for i in range(n):
        roll = randint(1,8)
        rolls.append(roll)
        total = total + roll

    return (total, rolls)

def d10(n=1):

    rolls = []
    total = 0

    for i in range(n):
        roll = randint(1,10)
        rolls.append(roll)
        total = total + roll

    return (total, rolls)

def d12(n=1):

    rolls = []
    total = 0

    for i in range(n):
        roll = randint(1,12)
        rolls.append(roll)
        total = total + roll

    return (total, rolls)

def d20(n=1):

    rolls = []
    total = 0

    for i in range(n):
        roll = randint(1,20)
        rolls.append(roll)
        total = total + roll

    return (total, rolls)

def d100(n=1):

    rolls = []
    total = 0

    for i in range(n):
        roll = randint(1,100)
        rolls.append(roll)
        total = total + roll
