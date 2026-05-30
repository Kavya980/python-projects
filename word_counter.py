import string

sentence=input("Enter a sentence:")
sentence=sentence.lower()    #i love bts and i stan bts
sentence=sentence.translate(str.maketrans('', '', string.punctuation))  #, , are ignored
words=sentence.split()  #space k according seperate
print("Total words: ",len(words))    #['i','love','bts',....]
print("Total characters: ",len(sentence))
word_count={}   #dictionary
for word in words:
    if word in word_count:
        word_count[word]+=1
    else:
        word_count[word]=1
        
print("Word frequency: ")
for word in word_count:
    print(word,":",word_count[word])
    
most_common=max(word_count,key=word_count.get)

print("Most common word:",most_common)
print(words)

    