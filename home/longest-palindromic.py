"""
Write a function that finds the longest palindromic substring of a given string. Try to be as efficient as possible!

If you find more than one substring you should return the one which is closer to the beginning.

Input: A text as a string.

Output: The longest palindromic substring.

"""

def longest_palindromic(text):
    length = len(text)
    max = 1
    head = 0
    for i in range(0, length):
        for j in range(i, length):
            if text[i:j] == text[j:i:-1]:
                lens = j-i+1
                if lens > max:
                    max = lens
                    head = i
                    
    return text[head:head+max]

if __name__ == '__main__':
    assert longest_palindromic("artrartrt") == "rtrartr", "The Longest"
    assert longest_palindromic("abacada") == "aba", "The First"
    assert longest_palindromic("aaaa") == "aaaa", "The A"
