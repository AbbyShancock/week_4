# #############################complete slide 1 challenge from week 4 slideshow##########
# #############################20 minutes################################################

# ##########################Reviewing somethings

# indexing strings -- slide 4
my_text = 'this is a text '
result = my_text  #get the index of the letter a
print(result[0:4]) #gives you "this"
print(result[-1]) # prints the last letter
#this is called indexing
#index slicing is a way to get a substring from a string
#substrings are a sequence of characters from a string
#get the index of the third letter from the end of the text
print(result[-3])
# find the index of the letter s
print(result.find('s'))
print(result.find('text'))

prepRally ="Hancock cheerleader are the best!"
# get the index pf the word "cheerleaders" in the string prepRally
print(prepRally.find('cheerleaders'))
print(prepRally[21:34])
# if -1 pops up that means it doesnt exist.
###slide 5
# string[start:stop:step]
#example
text = "Hello, World!"
print(text[0:12:3])  # prints "World"

text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# Get the substring CDE and put in a variable
#find the index of the letter C
print(text.find('C'))
#find the index of the letter E
print(text.find('E'))
#use the index to get the subtracting
print(text[2:5])

#get the first letter all the way to the 4th letter
print(text[0:4])
#get the first letter to the final letter and skip every 3rd letter
print(text[0:25:3])
# Built-in methods:
# Python has a variety of built-in methods to work with substrings.

# a. str.find():
# This method returns the lowest index of the substring if found in the given string. If it's not found, it returns -1.
# text = "Hello, World!"
# print(text.find("World"))  # prints 7
# print(text.find("Earth"))  # prints -1

#################################Extracting Sub-Strings###################################
# Extracting Sub-Strings Practice #1
# Extract the first word of the following sentence using slicing, and display it on the screen:
# "Controlling complexity is the essence of programming"
sentence ="Controlling complexity is the essence of programming"
print(sentence[0:11])
# Hint: "Controlling" is 11 characters long.

# Extracting Sub-Strings Practice #2
# Take every third character starting from the ninth to the end of the sentence, and print the result.
# "Never trust a computer you can't throw out a window"
sentence2 ="Never trust a computer you can't throw out a window"
print(sentence2[-1:9:3])

# Extracting Sub-Strings Practice #3
# Reverses the position of all the characters in the following sentence and displays the result on the screen.
# "It's great to work with computers. They don't argue, they remember everything and they don't drink your beer"
sentence3 ="It's great to work with computers. They don't argue, they remember everything and they don't drink your beer."
# print(sentence3([::-1]))










##################################### String Methods#################################
#uppercasing method in python 
sentence = "Especially in electronic communications, writing in all caps is equivalent to yelling."
print(sentence.upper() ) #prints the sentence in uppercase
#lowercase method in python
sentence2 = "ESPN IS THE BEST SPORTS NETWORK."
print(sentence2.lower()) #prints the sentence in lowercase
print(sentence.find("communications")) #prints the index of the word communications
#uppercase the word communications in a sentence
print(sentence.replace("communications", "COMMUNICATION")) #prints the sentence and truns communications into uppercase

# String Methods Practice #1
#slieds 12 -16
# Print the following text in uppercase, using the specific string method:
# "Especially in electronic communications, writing in all caps is equivalent to yelling."
sentence3 = "Especially in electronic communications, writing in all caps is equivalent to yelling."
print(sentence3.replace("electronics", "ELECTRONICS"))
#or use the upper method
print(sentence3.replace("communications", "communications".upper()))

new_sentence = "If the implementation is hard to explain, it might be a bad idea."
#replace the word hard with easy and bad with good
print(new_sentence.replace("bad", "good").replace("hard", "easy"))


#join method
word_list =["Simple","is","better","than","complex."]
print(word_list)
joined_sentence = " ".join(word_list)

new_word_list =["apple","banana","mango","cherry","watermelon."]
joined_sentence2 = "__".join(new_word_list)


#split method
sentence4 = "I am a python programmer"
print(sentence4.split()) #splits the sentence into a list of words
#by default, this method splits the senetnce by commas
#this prints out ['I', 'am', 'a', 'python', 'programmer']

print(sentence4.split(",")) #splits the sentence into a list of words using a comma.
#this prints out ["I am a python programmer"]

print(sentence4.split("a")) 
#this prints out ['I ', 'm ', ' python progr', 'mmer']

#concatenation words in python repetition 15 times
result = "repetition" * 15
print(result)
#prints: repetitionrepetitionrepetitionrepetitionrepetitionrepetitionrepetitionrepetitionrepetitionrepetitionrepetitionrepetitionrepetitionrepetitionrepetition

#find the first paragraph in the declaration of independence
#replace the word people with citizens in the first paragraph
#print the first paragraph with the word people replaced w citizerns

declaration = "WHEN in the Course of human events, it becomes necessary for one people to dissolve the political bands which have connected them with another, and to assume among the powers of the earth, the separate and equal station to which the Laws of Nature and of Nature’s God entitle them, a decent respect to the opinions of mankind requires that they should declare the causes which impel them to the separation."
print(declaration.replace("people", "citizens").replace(" ", "").replace(",", "_"))



# String Methods Practice #2
# Join the following list into a string, separating each item with a space. Use the appropriate list/string method, and display the result.
# word_list = ["Simple","is","better","than","complex."]

# String Methods Practice #3
# Replace in the following sentence:
# "If the implementation is hard to explain, it might be a bad idea."
# the following pairs of words:
# "hard" --> "easy"
# "bad" --> "good"
# and display the sentence with both words modified.

#################################string properties################################

# String Properties Practice #1
# Concatenate the text "Repetition" 15 times and display the result on the screen.
# Luckily, you know that strings are multipliable and you can do this activity in a simple and elegant way.

# String Properties Practice #2
# Check if the word "beach" is not found in the following haiku. You should print the boolean.
# "Whitecaps on the bay:
# A broken signboard banging
# In the April wind."
# — Richard Wright, collected in Haiku: This Other World, 1998

# String Properties Practice #3
# Check the Python Documentation to find the description of the len() function. Then, display on the screen the length (in number of characters) of the word electroencephalographist.

################################list###################################################
# Lists Practice #1
# Print the following list on the screen:
# ["Python", "is", "easy", "to", "learn"]

# Lists Practice #1
# Create a list with 5 elements, inside the variable my_list. You can include strings, booleans, numbers, etc.

# Lists Practice #2
# Add the element "motorcycle" to the following list of means of transportation:
# transportation_means = ["plane", "car", "ship", "bicycle"]
# You must not modify the already supplied line of code, but must use the appropriate list method to add a new element.

# Lists Practice #3
# Use the pop() method to remove the third item from the following list called fruits, and store it in a variable called deleted_item. Use list methods without altering the line of code already supplied.
# apple
# banana
# mango
# cherry
# watermelon

#######################################Dictionaries###############################
# Dictionaries Practice #1
# Create a dictionary called fruits with the following key-value pairs:
# apple --> red
# banana --> yellow
# mango --> green
# cherry --> red
# watermelon --> green
# Display the dictionary on the screen.

# Dictionaries Practice #1
# Create a dictionary called my_dict that stores the following information about a person:
# name: Karen
# surname: Jurgens
# age: 35
# occupation: Journalist
# The names of the keys and values must be equal to the ones indicated above.

#   Dictionaries Practice #2
# Use print to returns the second item of the list called points2, inside the following dictionary.
# If the value 300 were to change in the future, the code should work the same to return the value at that same position. To do this, you must refer to the names of the keys and/or indexes as appropriate.
# my_dict = {"values_1":{"v1":3,"v2":6},"points":{"points1":9,"points2":[10,300,15]}}
# print(my_dict[]) #Use dictionary indices to extract the second item of points2

# Dictionaries Practice #3
# Update the information in our dictionary called my_dict (reassigning new values to the keys as appropriate), and add a new key called "country" (without a tilde). The new data is:
# name: Karen
# surname: Jurgens
# age: 36
# occupation: Editor
# country: Colombia
# to do this, you should not change the line of code already written, but update the values using dictionary methods.
# my_dict = {"name":"Karen", "surname":"Jurgens", "age":35, "occupation":"Journalist"}

################################Tuples##################################

# Tuples Practice #1
# Use a tuple method to count the number of times the value 2 appears in the following tuple, and display the result (integer) on the screen:

# my_tuple = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)

# Tuples Practice #2
# Convert the following tuple to a list, and store it in a variable called my_list.

# my_tuple = (1, 2, 3, 2, 3, 1, 3, 2)

# Tuples Practice #3
# Extract the elements of the following tuple into four variables: a, b, c, d

# my_tuple = (1, 2, 3, 4)

###############################SETS########################################
# Sets Practice #1
# Join the following sets into one, called my_set_3:
# {1, 2, "three", "four"}
# {"three", 4, 5}
# my_set_1 = {1, 2, "three", "four"}

# my_set_2 = {"three", 4, 5}

# Sets Practice #2
# Remove a random item from the following set, using set methods.
# raffle = {"Rachel", "Monica", "Phoebe", "Joey", "Chandler", "Ross"}

# Sets Practice #3
# Add the name Gunther to the following set, using set methods:
# raffle = {"Rachel", "Monica", "Phoebe", "Joey", "Chandler", "Ross"}

###########################Booleans#######################################

# Booleans Practice #1
# Make a comparison that returns a boolean and store the result (True/False) in a variable called test

# Booleans Practice #2
# Check if 17834/34 is greater than 87*56 and print the boolean result to the screen using print()

# Booleans Practice #3
# Check if the square root of 25 is equal to 5 and display the result (boolean) on the screen using print()

###############################Proceed to last slide#################################