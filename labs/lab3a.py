"""
Author: Yost
Title: Lab 3A - Mad Lib
Date: 6 Sep 2018


Lab 3A: Formatting

General

Create your own mad libs game asking the user for input to fill in the blanks. Print out using .format().

(Humor encouraged)
Background

"Mad Libs is a phrasal template word game where one player prompts others for a list of words to substitute for blanks in a story, before reading the – often comical or nonsensical – story aloud. The game is frequently played as a party game or as a pastime."
Requirments

    Adhere to PEP8 (Comments, formatting, style, etc)
    Create a handfull of pharses that require different numbers of inputs
    Prompt the user for input(s):
        Inputs can be done a number of ways...
            (SIMPLE) Ask user for input directly, tell them if the word(s) need to be a verb, noun, etc.
            (Moderate) Give the user a handful of choices per input to choose from.You will need to create a bank of verbs, nouns, etc for this.
            (Harder) Give the user cards based off the actual game. Allowing them to draw, etc following the rules. Allow them to only input those cards.
        (opitional) Implement basic user input checking:
            Check to ensure words are words, numbers are numbers (there are many ways to do this)
            Ensure symobls aren't used if they are not needed
            Check length
            etc
            Implement re-input if input is incorrect
    Output the user inputs into the given pharse
    Use formatting to not only output the user inputs, but to create a UI within the terminal. Space out certain UI elements such as title of program, choices, menu deceration, etc.
"""


def madLib1():
    #variables to hold all of the inputs
    plNoun1 = raw_input("Type a plural noun and press <Enter>\n")
    adverb1 = raw_input("Type an adverb and press <Enter>\n")
    verb1 = raw_input("Type a verb and press <Enter>\n")
    clothing1 = raw_input("Type an article of clothing and press <Enter>\n")
    bodyPart1 = raw_input("Type a body part and press <Enter>\n")
    adjective1 = raw_input("Type an adjective and press <Enter>\n")
    noun1 = raw_input("Type a noun and press <Enter>\n")
    plNoun2 = raw_input("Type another plural noun and press <Enter>\n")
    bodyPart2 = raw_input("Type another body part and press <Enter>\n")
    plNoun3 = raw_input("Type a third plural noun and press <Enter>\n")
    bodyPart3 = raw_input("Type a third body part and press <Enter>\n")
    noun2 = raw_input("Type another noun and press <Enter>\n")
    noun3 = raw_input("Type a third noun and press <Enter>\n")
    ingVerb1 = raw_input("Type a verb ending in -ing and press <Enter>\n")
    adjective2 = raw_input("Type another adjective and press <Enter>\n")
    adjective3 = raw_input("Type a third adjective and press <Enter>\n")
    verb2 = raw_input("Type another verb and press <Enter>\n")

    print "How to date the coolest kid in school!\n\n"
    print "It's simple.  Turn the *{}*.  Make them want *{}* to date you.  Make sure you're always dressed to *{}*.".format(plNoun1, adverb1, verb1)  
    print "Each and every day, wear a/an *{}* that you know shows off your *{}* to *{}* your advantage and make your *{}* look like a million *{}*.".format(clothing1, bodyPart1, adjective1, noun1, plNoun2)
    print "Even if the two of you make meaningful *{}* contact, don't admit it.  No hugs or *{}*.  Just shake their *{}* firmly.".format(bodyPart2, plNoun3, bodyPart3)
    print "And remember, when they ask you out, even though a chill may run down your *{}* and you can't stop your *{}* from *{}*, just play it *{}*.".format(noun2, noun3, ingVerb1, adjective2)
    print "Take a long pause before answering in a very *{}* voice.  I'll have to *{}* it over.".format(adjective3, verb2)


madLib1()