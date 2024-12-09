#!/usr/bin/env python3

def return_evens(sequence):
    return [n for n in sequence if n % 2 == 0]
pass

def make_exclamation(sentences):
    return [sentence + '!' for sentence in sentences]
pass

print(return_evens([0, 1, 3, 5, 7, 8, 9]))  # Output: [0, 8]

print(make_exclamation(["Hello", "I'm doing great", "Python is fun"]))  # Output: ["Hello!", "I'm doing great!", "Python is fun!"]
