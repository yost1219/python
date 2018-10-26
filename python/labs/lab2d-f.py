>>> #lab2d
>>> def reverse():
...      userInput = raw_input("Tell me something good.\n")
...      reverseInput = userInput[::-1]
...      reverseCaps = reverseInput.upper()
...      print reverseCaps
...      return
...
>>> def reverse():
...     print raw_input("Tell me something good.\n")[::-1].upper()
...     return
...
>>> #lab2e
>>> def countWords() :
...     userInput = raw_input("I'll count your words.\n")
...     word = userInput.split(" ")
...     print len(word)
...     return
...
"""
Author: Yost
Title: Lab 2F
Date: 5 Sep 2018


Lab 2F: Man A Rag

    Instructions:
        Write a program that will be able to check if two words (strings) are anagrams.
        An anagram is a word or phrase formed by rearranging the letters of a different word or phrase
    The program should include:
        All proper comments
        Needed docstrings
        User input (only expecting one user input due to not having gone over loops yet)
"""
>>> def anagram():
... #get two words from user to compare
...     print "Enter two words to compare.\n"
...     word1 = raw_input("Input the first word.\n")
...     word2 = raw_input("Input the second word.\n")
... #convert to all caps to take case out of the situation
...     word1 = word1.upper()
...     word2 = word2.upper()
... #order the letters of the words
...     list1 = sorted(word1)
...     list2 = sorted(word2)
... #compare the two lists to see if they are equal or not
... #if they are equal then say so, if not then say that
...     if list1 == list2:
...         print "The two words are anagrams."
...     else:
...         print "The two words are not anagrams."
...     return