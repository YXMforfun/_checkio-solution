"""
The Hamming distance between two binary integers is the number of bit positions that differs (read more about the Hamming
 distance on Wikipedia). For example:

    117 = 0 1 1 1 0 1 0 1
     17 = 0 0 0 1 0 0 0 1
      H = 0+1+1+0+0+1+0+0 = 3

You are given two positive numbers (N, M) in decimal form. You should calculate the Hamming distance between these two
numbers in binary form.

Input: Two arguments as integers.

Output: The Hamming distance as an integer.
"""
def checkio(n, m):
    result = str(bin(n ^ m)).count('1')
    return result


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(117, 17) == 3, "First example"
    assert checkio(1, 2) == 2, "Second example"
    assert checkio(16, 15) == 5, "Third example"