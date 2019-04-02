**TIME SERIES EXERCISES WITH PANDAS**

This is an (incomplete) set of exercises that I wrote to introduce programmers to the slightly different form of
programming that exists in the data science.  This was written specifically for a friend of mine, and the
documentation is shaped accordingly.  But you may find it useful regardless.

**Introduction**

The main objective is to highlight the differences between traditional iterative programming (that you're used to),
and array programming (https://en.wikipedia.org/wiki/Array_programming), which is broadly used in data science.

Broadly speaking, there are two main categories of operations on arrays:
- path independent
- path dependent

Path independent is where we get all of the efficiencies.  Array-programming is more efficient speed and ease-of-use
wise doing similar operations over large subsets of data.  Within path-independent operations, there are two
broad categories:
- entire-data computation (not a formal term)
- rolling window computation

Path dependent means the outcome of the next value depends on an action we took for the previous value.  An easy
example of this is trading rules.  For example, if you have a set of rules:

    IF LONG, SELL 3x
    IF SHORT, BUY 1x
    IF FLAT, BUY 2x

For these rules, you can't tell whether to buy or sell without knowing if you were long or short in the previous time.
Furthermore, there's no way to "cut" out a window of only the most recent data, since to get the exact history
you need to start all of the way from the beginning.  Consider if you have 40 data points.  Can you figure out what
to do for the 40th data point without knowing what you did at the 39th, 38th, and so on all the way until the 1st?
(You can't.)

Contrast this to a 20-day moving average.  If you have 40 data points, you can effectively ignore the first 20 and
only need the last 20 to generate a moving average value for the 40th data point.

You already know how to write path-dependent code.  The following exercises will give you exposure on how to use
Pandas and Numpy in a path-independent manner, the way array programming is meant to be used.  You will be generating
several simple indicators over a data set I provide, and will generate two simple trading strategies using that
information - one that is path-independent, and one that is path-dependent.

Once you've figured this out, you should start to learn about regression.  That's beyond the scope of this set of
exercises.

**Getting Started**

1) This project is designed to be opened in PyCharm, using Python 3.6+.  First install the packages listed in
requirements.txt.

2) See exercises.txt for the questions.  Try to implement them yourself if you can.

3) I've written solutions up to exercise 7.  You can run any of the solutions individually from solutions.py, or run
them as a unified routine by executing unified_solution() in solutions.py.


**Authors**

Vincent Chin

**License**

This project is licenses under the MIT License - see the LICENSE.md file for details.