##There is a string , s, of lowercase English letters is repeated infinitely many times.
# Given an integer, n, find and print the number of letter a,s in the first n letters of the intinite string.

##example

##s = 'abcac'
##n = 10

##the substring we donsider is abcacabcac, the first 10 caracters of the infinite strinf.
# there are 4 occurrences  of a in the substring

def repeatedString(s, n):
    count_a_in_s = s.count('a')

    full_repeats = n // len(s)

    total_a = full_repeats * count_a_in_s

    remainder = n % len(s)

    total_a += s[:remainder].count('a')
    return total_a


s = 'abcac'
n = 10
print(repeatedString(s, n))