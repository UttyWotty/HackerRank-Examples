##there si a new mobile game that starts with concesutively numered clouds.
# Some of the clouds are thunderheads and other s are comulus.
# The player can jumo on any comulus cloud havung a number that is equal of the current cliuds plus 1 or 2.
# The platers must avoid the thunderheads.
# Determine the minimum number of jumos it will take to jump from the starting point to the last cloud.
# iT WILL ALWATS POSSIBLE TO win the game.

##for each game, you will get an array of clouds numbered 0 if they are safe or 1 if it has to be avoided.

##example ;
##c = [0,1,0,0,0,1,0]

def jumpingOnClouds(c):
    jumps = 0
    position = 0

    while position < len(c) - 1:
        if position + 2 < len(c) and c[position + 2] == 0:
            position += 2
        else:
            position += 1
        jumps += 1

    return jumps


c = [0, 1, 0, 0, 0, 1, 0]
print(jumpingOnClouds(c))
