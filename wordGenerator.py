###This is a word generator tool
##Input: 1. string : set of jumbled letters 2. Length of words to be formed using letters
##output: All possible words of mentioned length


import itertools
import enchant

d = enchant.Dict("en_US")
word = raw_input("Enter word: ")
length=input("Enter length: ")


t=list(itertools.permutations(word,length))

possible_words=[]
for i in range(0,len(t)):
    new_word = ''.join(t[i])
    possible_words.append(new_word)

#print possible_words

final_words=[]
for nword in possible_words:
    if d.check(nword):
        if nword not in final_words:
            final_words.append(nword)


print "Possible words are:"

for myword in final_words:
    print myword
                                                                    








