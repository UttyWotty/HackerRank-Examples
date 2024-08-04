## a hiker keeps a record of his hikes. during the last hike that took exactly steps steps,
# for every step it was noted if it was an uphill, U, or a downhill , D step. hikes always
# start and end at sea level and rach step up or down represents a 1 unit change im altitude. we define the following ;
##a mountain is a sequence of consecutive steps above the sea level, starting with a step up
# from sea level and ending with a step down to sea level
##a valley is a sequence of consecutive steps below sea level, starting with a step down from sea level
# and ending with a step up to sea level.
##example ;
##steps = 8 path = [DDUUUUDD]

##the hiker first enters a valley 2 units deep. then they climb out and onto a montain 2 units high.
# finally the hiker return to sea level and ends the hike.

def counting_valleys(steps, path):
    sea_level = 0
    valleys = 0
    current_level = sea_level

    for step in path:
        if step == 'U':
            current_level += 1
        elif step == 'D':
            current_level -= 1

        if current_level == sea_level and step == 'U':
            valleys += 1
    return valleys

steps = 8
path = ['D','D','U','U','U','U','D','D']
print(counting_valleys(steps, path))
