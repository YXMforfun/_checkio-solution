"""
Our Robo-Trio need to train for future journeys and treasure hunts. Stephan has built a special flat model of a pyramid. Now the robots
can train for speed gold running. They start at the top of the pyramid and must collect gold in each room, choose to take the left or
right path and continue down to the next level. To optimise their gold runs, Stephan need to know the maximum amount of gold that can
be collected in one run.

Consider a tuple of tuples in which the first tuple has one integer and each consecutive tuple has one more integer then the last. Such
a tuple of tuples would look like a triangle. You should write a program that will help Stephan find the highest possible sum on the most 
profitable route down the pyramid. All routes down the pyramid involve stepping down and to the left or down and to the right.

Tips: Think of each step down to the left as moving to the same index location or to the right as one index location higher. Be very 
careful if you plan to use recursion here.

Input: A pyramid as a tuple of tuples. Each tuple contains integers.

Output: The maximum possible sum as an integer.
"""

def count_gold(pyramid):
    l = [pyramid[0][0]]
    for i in range(1, len(pyramid)):
        l.append(l[-1]+ pyramid[i][-1])                                      # increase list length, otherwise out of range  
        for j in range(len(pyramid[i])-2, 0 , -1):
            l[j] = max(l[j], l[j-1]) + pyramid[i][j]                        #dynamic programming
        l[0] += pyramid[i][0]
    return max(l)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_gold((
        (1,),
        (2, 3),
        (3, 3, 1),
        (3, 1, 5, 4),
        (3, 1, 3, 1, 3),
        (2, 2, 2, 2, 2, 2),
        (5, 6, 4, 5, 6, 4, 3)
    )) == 23, "First example"
    assert count_gold((
        (1,),
        (2, 1),
        (1, 2, 1),
        (1, 2, 1, 1),
        (1, 2, 1, 1, 1),
        (1, 2, 1, 1, 1, 1),
        (1, 2, 1, 1, 1, 1, 9)
    )) == 15, "Second example"
    assert count_gold((
        (9,),
        (2, 2),
        (3, 3, 3),
        (4, 4, 4, 4)
    )) == 18, "Third example"
