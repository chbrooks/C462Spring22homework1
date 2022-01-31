from random import randint

# MonteCarlo.py
# This program uses a Monte Carlo approach to estimate the probability of winning the dice game "Approach" with different
# "hold" values.
# Recall that approach works like this:
# Both players agree on a limit n.
# Player 1 rolls first. They go until they either exceed n or hold.
# Then player 2 rolls. They go until they either exceed n or beat player 1's score.
# The player who is closest to n without going over wins.
# We can reduce this to the problem of of player 1 choosing the best value at which to hold.
# We'll estimate this by simulating all possible hold values from n-5:n

# This function should try each possible hold value 1000000 times. Once a hold value is set,
# play a random game and keep track of the number of wins for player 1.

# n is the limit.

def monte_carlo_approach(n) :
    win_table = {}
    for i in range(n-5,n+1) :
        win_table[i] = 0
    for i in range(1000000) :
        ## you do this part. My solution is under 20 lines of code. Yours can be longer, but if it's getting
        ## really big, take a step back and rethink.

    for item in win_table.keys() :
        print("%d: %f" % (item, win_table[item]/1000000))