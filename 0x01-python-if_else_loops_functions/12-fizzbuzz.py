#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        word1 = "Fizz"
        word2 = "Buzz"
        word3 = "FizzBuzz"

        if i % 3 == 0 and i % 5 == 0:
            print("{}".format(word3), end=" ")
        elif i % 3 == 0:
            print("{}".format(word1), end=" ")
        elif i % 5 == 0:
            print("{}".format(word2), end=" ")
        else:
            print("{}".format(i), end=" ")
