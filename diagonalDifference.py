##Given a square matrix, calculate the absolute difference between the sums of its diagonals.
#For example, the square matrix ar = [1, 2, 3, 4, 5, 6 , 7, 8, 9], arranged in a 3×3 grid resembling a phone keypad.

def diagonalDifference(arr):
    n = len(arr)
    first_diagonal_sum = 0
    second_diagonal_num = 0

    for i in range(n):
        first_diagonal_sum += arr[i][i]
        second_diagonal_num += arr[i][n-i-1]

    return abs(first_diagonal_sum - second_diagonal_num)

arr= [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(diagonalDifference(arr))