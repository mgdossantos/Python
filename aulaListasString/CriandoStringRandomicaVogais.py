import random
char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

i=0
word=''
while i<34:
	word=word+random.choice(char)
	i=i+1

i=0
numberVowels=0
while i<len(word):
	if word[i] in 'aeiou':
		numberVowels=numberVowels+1
	i=i+1
	
print("Random Word: "+word)
print("Numbers of vowels: "+str(numberVowels))