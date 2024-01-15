
phrase = input("please sir, enter a phrase ")

counts= {}
 
def word_count(str):

    counts = {}

    words = str.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts 
print(word_count(phrase))  


top_words = sorted(counts, key=phrase, reverse=True)     
for index in range(3): 
    if phrase in counts:
        counts[phrase] +=1

    
    print(top_words)
    









# def word_sort(sort):

#     counts = {}
    
#     frequency = sort.sorted()

# print(word_sort(phrase))
    


