# the_millionth_fibonacci_kata.py
'''
DESCRIPTION:
The year is 1214. One night, Pope Innocent III awakens to find the the archangel Gabriel floating before him. Gabriel thunders to the pope:

Gather all of the learned men in Pisa, especially Leonardo Fibonacci. 
In order for the crusades in the holy lands to be successful, these men must calculate the millionth number in Fibonacci's recurrence. 
Fail to do this, and your armies will never reclaim the holy land. It is His will.

The angel then vanishes in an explosion of white light.

Pope Innocent III sits in his bed in awe. How much is a million? he thinks to himself. He never was very good at math.

He tries writing the number down, but because everyone in Europe is still using Roman numerals at this moment in history, he cannot represent this number. 
If he only knew about the invention of zero, it might make this sort of thing easier.

He decides to go back to bed. He consoles himself, The Lord would never challenge me thus; this must have been some deceit by the devil. 
A pretty horrendous nightmare, to be sure.

Pope Innocent III's armies would go on to conquer Constantinople (now Istanbul), but they would never reclaim the holy land as he desired.

In this kata you will have to calculate fib(n) where:

fib(0) := 0
fib(1) := 1
fib(n + 2) := fib(n + 1) + fib(n)
Write an algorithm that can handle n up to 2000000.

Your algorithm must output the exact integer answer, to full precision. Also, it must correctly handle negative numbers as input.

'''


# first attempt - i got timeout error when "n" reached over 1 000 000. Correct code, but not optimized.
def fib(n):
    if -2000000 <= n <= 2000000:
        if n > 0:
            a = 0
            b = 1
            for i in range (n-1):
                a,b=b,a+b
            return b
        elif n <= 0:
            a, b = 0, 1
            for i in range(n, 0):
                a, b = b, a - b
            return a
    else:
        return "Outside of range"
