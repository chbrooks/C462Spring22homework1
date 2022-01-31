### Assignment 1: Introduction to AI

##### Due: Tuesday 2/16 at the start of class. (2:40pm)

##### 100 points.

Note: please make sure that your name is someplace in your assignment! This is especially true if it's not obvious from your GitHub handle.

To turn in: please submit everything to your github repo. For the written portion of the assignment, please add a document to your repository, as PDF, containing the answers to these questions.

Part 1. (20 points) Consider the following potential AI problems. For each of them, describe whether the environment is: a) static or dynamic b) fully or partially observable c) episodic or sequential d) deterministic or stochastic. Please explain your reasoning.

- A robotic medical assistant that can assist a doctor or nurse. It communicates with patients, administers bloodwork, and takes vitals.
- An agent that plays poker against a human player. Assume that the cards are digital, and that the player interacts with the agent via a touchscreen.
- An agent that can select TV shows and movies for a user. It watches the user's choices, asks the user to rate shows, and gives new shows the user is predicted to like. 
- A digital chatbot for diagnosing mental health issues. It interacts with the user via SMS and makes a prediction about their mental health based on responses.
- A robotic submarine for scientific exploration. It's able to autonomously travel to the ocean floor and collect samples.

Part 2. (20 points) Monte Carlo simulation. A common technique for estimation of complex problems is Monte Carlo simulation. We'll use it here to try to estimate 
an optimal stopping point (or policy) for a simple dice game, called approach. This will also give you some practice with Python.

Approach works like this: There are two players, and they choose a target number (n).
Player 1 repeatedly rolls a six-sided die and adds up their total. Whenever they want, they can "hold." Then player 2 must roll;' their goal is 
to beat (not tie) player 1's score without going past n. The problem we want to solve is this:

For player 1, for a given n and a particular total so far (called s) should they: 
'hold' (action 1) or 'roll' (action 2).

(note that player 2's strategy in this game is pretty boring - they just roll until they either beat player 1's score or exceed n.)

I've provided the beginnings of this program for you. 
It should: take as input a limit n.:
  For all values from n-5:n, estimate the probability of winning, given that we 'hold' at that value.

For example, if n=10, you might see:
<pre>
monte_carlo_approach(10)
5: 0.255314
6: 0.360087
7: 0.431315
8: 0.435367
9: 0.371685
10: 0.205657
</pre>

To estimate these probabilities, we'll play the game 1000000 times for each possible hold. 
A round of the game works like this:
   - player 1 sets their hold value. They then 'roll the die' (generate a random int between 1 and 6) and add to their score until:
     - They exceed n, in which case they lose.
     - Their total is >= to their hold value, and less than n. In this case player 2 goes.
       - Player 2 rolls until their total either:
         - Exceeds player 1, but is less than or equal to n. Player 1 loses.
         - Exceeds n. Player 1 wins.
         


Part 3: (20 points) Turing Test. [Kuki](https://www.pandorabots.com/kuki/) is a chatbot developed using Pandorabots chatbot technology. Kuki has won the Loebner Prize for the last five years. You can interface with Kuki in quite a few ways [here](https://www.kuki.ai/).

If you talk with Kuki, you'll see the limits of her responses pretty quickly. Try talking with her about different subjects - movies, music, games, life. 

What are places where Kuki's responses seem artificial? What sorts of responses or conversations does she have problems with?

Now try to have a conversation that generates responses that seem as human as possible. What sorts of phrases and discussions does Kuki do well with?


Part 4. (20 points) This problem will give you some experience coding in Python in an object-oriented style. 
The sample code in the assignment's github repo implements a graph as an adjacency list. I've provided code for reading a graph from a file, a simple data file, and a method for generating random graphs.
The data is in a format called MTX. If you want to get lots more graph data in this format, please check out [this link](https://networkrepository.com/).

Please add methods to implement:
- Breadth-first search
- Depth-first search
- Djikstra's shortest-path algorithm
- Prim's spanning-tree algorithm

There are comments in the code that give more detail. For each of these methods, please add a unit test (using pytest) demonstrating that it works correctly.

Part 5: (20 points) 
ZeroR. 

In this task, we'll build our first machine learning algorithm, called ZeroR. It's quite simple, but will serve as a baseline for more interesting algorithms later.

ZeroR is a supervised classification algorithm. It takes as input a labeled dataset, and returns the most common classification in the dataset. In other words, it assumes that 
all the features are irrelevant. This is, in some sense, "optimal" - if we don't know anything about the problem, the best thing we can do is guess the most common outcome.

ZeroR should do the following:
- Read in a dataset from an ARFF file and create two objects:
1. An attribute dictionary that maps attribute names to either a list of values (for discrete variables) or a descriptor for REAL variables.
2. A nested list containing the dataset.
3. Compute the most common classification.

Extend this to the slightly more interesting randR. It should work just like ZeroR, except that it should compute the probability of each classification,
and then generate a classification with that likelihood. (in other words, if 70% of the dataset are 'yes', it should say 'yes' 70% of the time.)
Note that both ZeroR and RandR do the same work in terms of processing the data file - you might want to make functions to help here. (hint!) You will need this
for future assignments.


Part 6 (686 students only): A classic thought experiment in response to the Turing Test is the Chinese Room, proposed by John Searle.
To begin, please read [this webpage](https://mind.ilstu.edu/curriculum/searle_chinese_room/searle_chinese_room.html), which presents the Chinese Room thought experiment, intended to show that a computer can manipulate symbols to produce replies without understanding what they mean.

Then, read section 2 (Replies and Rejoinders) of [this page](https://iep.utm.edu/chineser/), which summarizes many of the responses to the Chinese Room argument.

a) Summarize the Chinese Room argument. What does this have to do with computers? Why does Searle believe that it shows that a computer can pass the Turing test without understanding?

b) Do you find Searle's argument convincing? Or do you find one of the responses more appealing? Explain your position. 

Part 6. (686 students only): Add a method to the graph code from part 4 to include a method that takes as input a vertex and finds the maximal clique that this vertex belongs to. 