##given a 6x6 2D array, arr"

##111000
##010000
#111000
#000000
#000000
#000000

#an hourglass in A is a subset of values with indices falling in this pattern in arr's graphical resresentation:

#a b c
#   d
#e f g

#there are 16 hourglasses in arr. An hourglass sun is the sum of an hourglass's values. calculate the hourglass sum for every hourglass in arr. then print the max hourglass sum. the array will always be 6 x 6

#example

#arr =

#-9 -9 -9 111
#0 -9 0 4 3 2
#-9 -9 -9 123
#008660
#000-200
#001240

#the 16 hourglass sums are:

#-63 ,-34, -9, 12,
#-10, 0, 28,23,
#-27, -11,-2,10,
#9,17,25,18

#the highest hourglass sum is 28 from the hourglass beginning at row 1 ,column 2

#0 4 3
#   1
#8 6 6


def hourglassSum(arr):
    max_sum = -float('inf')

    for i in range(4):
        for j in range(4):
            current_sum = (arr[i][j] + arr[i]
            [j + 1] + arr[i][j + 2] +
                           arr[i + 1][j + 1] +
                           arr[i + 2][j] +
                           arr[i + 2][j + 1] + arr[i + 2][j + 2])

        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum


arr = [
    [1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
]

print(hourglassSum(arr))
