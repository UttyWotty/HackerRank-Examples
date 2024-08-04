##You are in charge of the cake for a child’s birthday.
# You have decided the cake will have one candle for each year of their total age.
# They will only be able to blow out the tallest of the candles. Count how many candles are tallest.
# For example, in the array candles = [4, 4, 1, 3], return 2.

def birthdayCandles(candles):
    tallest = max(candles)

    return candles.count(tallest)

candles = [4,4,1,3]
print(birthdayCandles((candles)))