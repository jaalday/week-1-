word = input("please enter word ")

    
    
def letter_histogram(word):
    letter_count = {}
    for letter in word:
       letter_count[letter] = word.count(letter)
    return letter_count
print(letter_histogram(word))






# def word_count(sentence):
#     histogram = {}
    
#     wordlist = sentence.lower()
#     for words in wordlist:

#         if words in histogram:
#             histogram[word] += 1
#         else: histogram[word] = 1
#         return word
        
#     print(word_count(word))
        
    



# histogram = {}

# for letters in word:
    # if letters in word:
        
    
    
    

