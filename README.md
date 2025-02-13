# COP3502C
Overview

In this lab, you will build three functions. The first function will calculate the nth Fibonacci number. The second function will check whether a given number is prime. The third function will print the prime factors of a given number. The lab is designed to give you an opportunity to experiment with writing functions while practicing loops and conditionals.

Submission Instructions

After completing all programs, please submit your Lab4.py file. This file should ONLY have your function definitions. PLEASE read the instructions carefully.

 Specification

Function 1: Fibonacci Numbers

Background

The Fibonacci numbers are a sequence of numbers where each number is the sum of the two numbers that appear before it. The sequence starts with 0 and 1. The first 20 numbers are as follows: 

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181

Assignment

Your task is to define a function named “fibonacci” that takes an integer and returns the Fibonacci number at that position in the sequence. The number in the first position is 0. You can assume that the parameters to the function will be positive integers. You may not use a direct mathematical formula to find the Nth Fibonacci number.

Examples

You can test your function’s correctness by checking that all the cases below are true:
fibonacci(1) == 0
fibonacci(2) == 1
fibonacci(3) == 1
fibonacci(6) == 5
fibonacci(25) == 46368



Function 2: Prime Numbers 

Background

A prime number is an integer greater than one that is only divisible by 1 and itself. You can check if N is divisible by M with the statement N % M == .0. Examples of prime numbers are 2, 3, 11, and 29. Examples of non-prime numbers are 6, 8, and 9. 6 and 8 are divisible by 2. 9 and 6 are divisible by 3.

Assignment

Your task is to define a function named “is_prime” that takes an integer as a parameter and returns True if the number is prime, and False if the number is not prime. You can assume that the parameters to the function will be integers, but they may be negative.

Examples

You can test your function’s correctness by checking that all the cases below are true:
is_prime(2) == True
is_prime(11) == True
is_prime(1741) == True
is_prime(1) == False
is_prime(9) == False
is_prime(-2) == False

Function 3: Prime Factorization

Background

All positive integers greater than 1 can be expressed as the product of a unique combination of prime numbers. This combination of prime numbers is referred to as the number’s prime factorization. For example, the number 30 can be expressed as 2 * 3 * 5. The prime factorization for a prime number is just itself.

Assignment

Your assignment is to write a function named “print_prime_factors” that will take an integer as its parameter and calculate the integer’s prime factorization. While the first two functions returned their results, this function will instead print the result and return nothing. The output should be in the format: parameter = factor1 * factor2 * factor3. Note that a prime may appear more than once in the prime factorization, and the factors should be printed in order of least to greatest. You can assume that the inputs to the function will be positive integers greater than 1.


Examples

Here is a sample program for testing your function:

print_prime_factors(10)
print_prime_factors(2)
print_prime_factors(24)
print_prime_factors(2475)
print_prime_factors(23)

This should print out the following:
10 = 2 * 5
2 = 2
24 = 2 * 2 * 2 * 3
2475 = 3 * 3 * 5 * 5 * 11
23 = 23







