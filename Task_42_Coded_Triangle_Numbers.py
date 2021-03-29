# Function which uses formula for finding TRIANGULAR NUMBERS
f = lambda x: int(0.5*x*(x+1))
# We collect it in the list
result = list(map(f,[i for i in range(1,100)]))

# Alphabet for determining position of letter
alpha_list = ['A','B','C',
			'D','E','F',
			'G','H','I',
			'J','K','L',
			'M','N','O',
			'P','Q','R',
			'S','T','U',
			'V','W','X',
			'Y','Z']

""" We open a file for reading and remove ' "" ' from it by using "replace" method.
Also we used "strip" method to avoid ' " ' in the beginning and the end"""
with open('p042_words.txt', 'r') as file:
	cleaned_file = str(file.read()).strip('\"').replace('\",\"', ",")

# We used "split" method to add every word into new list with separating it by comma
word_list = [word for word in cleaned_file.split(",")]


count = 0
# In the range of length of file we take every word from "word_list" and sum all letters in it.
for length in range(len(word_list)):
	weight = sum([alpha_list.index(letter)+1 for letter in word_list[length]])

""" We compare if the sum of letters in word is one of triangular numbers
		 then we return this word and add +1 to count"""
	if weight in result:
		# print(word_list[length])
		count += 1

print(count)