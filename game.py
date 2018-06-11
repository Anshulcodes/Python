import random


def keygen():
    # key generator
    keyl1 = 'A'
    keyh1 = 'Z'
    keyl2 = 'a'
    keyh2 = 'z'
    keyarray = []
    key1 = random.randrange(ord(keyl1), ord(keyh1))
    keyarray.append(key1)
    key2 = random.randrange(ord(keyl2), ord(keyh2))
    keyarray.append(key2)
    key = random.choice(keyarray)
    return key


def protect():
    # shield generator for the attack
    shieldl = 90
    shieldh = 108
    return random.randrange(shieldl, shieldh)
    

def destroy():
    # Attacking power
    hp = 500  # initial health
    atkl = 100
    atkh = 120
    while hp > 1:
        key = str(chr(keygen()))
        print('Press', key)
        match = input()
        if key == match:
            gain = protect()
            hp = hp + gain   # shield
            print('Health gain is of', gain, 'and the current health is', hp)
        dmg = random.randrange(atkl, atkh)
        hp = hp - dmg
        if hp < 120:
            if hp < 0:
                hp = 0
            elif hp > 0:
                print('You have been transferred to the rest room as your health is critically low.')
        print('Health of the player is', hp, 'and the damage is', dmg)
        if hp == 0:
            print('You died!')
    return hp
    

a = True
b = 1
finalhp = destroy()
while a is True:
    choice = str(input('Want to respawn? Y/N'))
    if choice == 'Y':
        finalhp = destroy()
        b = b + 1
    else:
        break
print('Number of times game played: ', b)
print('Hope you enjoyed!')
