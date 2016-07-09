"""
While Stephen is running cargo, Nicola and Sophia invented a game using the boxes.
To start the game, they put several black and white pearls in one of the boxes. Each robots have Nth moves, then initial set are restored
for a next player. For each move, the robot take a pearl out of the box and put one of the opposite color back. The winner is the one who
pulls the white pearl on the Nth step (or +1 point if they play many parties).
Our robots don't like indeterminacy and want to know the probability of a white pearl on the Nth step. The probability is a value between
0 (0% chance or will not happen) and 1 (100% chance or will happen). The result is a float from 0 to 1 with two digits precision (±0.01).
You are given a start set of pearls as a string that contains "b" (black) and "w" (white) and the number of the step (N). The order of 
the pearls does not matter.

Input: The start sequence of the pearls as a string and the step number as an integer.
Output: The probability for a white pearl as a float.
Precondition: 0 < N ≤ 20
0 < |pearls| ≤ 20

"""
# Consider the process as a decision tree. Focus on the probability
from itertools import product
def checkio(marbles, step):
    def calculate(pearls):
        length = len(marbles)
        white = marbles.count('w')
        ratio = 1
        for i in pearls:
            if i == 'w':
                ratio *= (white/length)
                white -= 1
            else :
                ratio *= 1- (white/length)
                white += 1
            if white < 0 or white > length:
                return 0
        return ratio * (white/length)
    
    return round(sum(calculate(l) for l in product(['w','b'], repeat=step-1)), 2)

#recursion
def checio1(marbles, step):
    white_rate = marbles.count('w') / len(marbles)
    black_rate = 1 - white_rate
    if step == 1:
        return white_rate
    else :
        return sum([
            white_rate * checkio1(marbles.replace('w', 'b', 1), step-1),
            black_rate * checkio1(marbles.replace('b', 'w', 1), step-1)
        ])
    
    
    if __name__ == '__main__':
        assert checkio('bbw', 3) == 0.48, "1st example"
        assert checkio('wwb', 3) == 0.52, "2nd example"
        assert checkio('www', 3) == 0.56, "3rd example"
        assert checkio('bbbb', 1) == 0, "4th example"
        assert checkio('wwbb', 4) == 0.5, "5th example"
        assert checkio('bwbwbwb', 5) == 0.48, "6th example"
