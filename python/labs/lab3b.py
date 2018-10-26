""""
Author: Yost
Title: Lab 3B
Date: 7 Sep 2018


Student Code: Lab3B
Instructions:
* You are provided with a text file that contains the best song lyrics in the world
    * Problem is... the song lyrics are encrypted with a simple XOR.
* You will need to decrypt the lyrics
    * The key is 27
    * You have been provided with a decent chunk of the code with conditionals and loops already created...
    * Feel free to create yours from scratch if you want a greater challange. 
* You will need to think outside the box. Remember what XOR is, the type of data it acts on, how much data, etc. 
"""
def studentCode():
    # TODO: Create variables and open file here
	tempString = ""
    key = 27
    finalString = ""

    # TODO: Read your file
	file = open("lab3blyrics.txt",'r')
	tempString = file.read()
	file.close()

    # Uncomment below, replacing STR with your string or datatype to loop
    
    # C/C++ style: for (int i = 0; i < STR; i++)
    for i in tempString:
        # Perform XOR here
		finalString+=chr(ord(i)^key)

    # Replace either the return or reassign your unencrypted string to finalString

    return finalString

studentSTR = studentCode()

print studentSTR

