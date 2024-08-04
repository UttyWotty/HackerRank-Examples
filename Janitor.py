##The janitor of a high school is extremely efficient.
# By the end of each day, all of the school’s waste is in plastic bags weighing between 1.01 pounds and 3.00 pounds.
# All plastic bags are then taken to the trash bins outside. One trip is described as selecting a number of bags which
# together do not weigh more than 3.00 pounds, dumping them in the outside trash can and returning to the school.
# Given the number of plastic bags, and the weights of each bag,
# determine the minimum number of trips the janitor has to make.

def min_trips(weights):
    weights.sort()

    left = 0
    right = len(weights) - 1
    trips = 0

    while left <= right:
         if weights[left] + weights[right] <= 3.00:
          left += 1
         right -= 1
         trips += 1
    return trips

weights = [1.01, 1,82, 2.0, 1.2, 2, 2.01]
print(min_trips(weights))