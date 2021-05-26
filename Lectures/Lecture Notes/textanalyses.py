import time
import re
import threading
import multiprocessing

# helper function for retrieving all words (uninterrupted sequences of w
def get_all_words(text):
    all_words = re.findall("\w+", text)
    return all_words

# function to find the longest word in a text
def get_longest_word(text):
    words = get_all_words(text)
    longest_word = ""
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    print(f"The longest word in the text is: {longest_word}")

# function to find the most frequent word in a text
def get_most_frequent_word(text):
    words = get_all_words(text)
    word_frequencies = {}
    for word in words:
        if word in word_frequencies:
            word_frequencies[word] += 1
        else:
            word_frequencies[word] = 1
  
    max_frequency = 0
    most_frequent_word = ""
    for word in words:
        if word_frequencies[word] > max_frequency:
            max_frequency = word_frequencies[word]
            most_frequent_word = word
  
    print(f"The most frequent word in the text is: {most_frequent_word}")

# function to find all palindromes (length > 1) in a text
def get_palindromes(text):
    words = get_all_words(text)
    all_palindromes = set()
    for word in words:
        if len(word) > 1 and word == word[::-1]:
            all_palindromes.add(word)
   
    print(f"There are {len(all_palindromes)} palindromes in the text.")
    #for palindrome in all_palindromes:
        # print("\t", palindrome)


# main program
time.sleep(5)

textfile = "data/big.txt" # downloaded from https://norvig.com/big.txt
with open(textfile, "r") as file:
    text = file.read()

starttime = time.time()

get_longest_word(text)
get_most_frequent_word(text)
get_palindromes(text)

endtime = time.time()
print(f"Total time elapsed: {endtime-starttime}")

print()

time.sleep(5)

# concurrent version
starttime = time.time()

longest = threading.Thread(target=get_longest_word, args=(text,))
most_frequent = threading.Thread(target=get_most_frequent_word, args=(text,))
palindromes = threading.Thread(target=get_palindromes, args=(text,))

longest.start()
most_frequent.start()
palindromes.start()

longest.join()
most_frequent.join()
palindromes.join()

endtime = time.time()
print(f"Total time elapsed: {endtime-starttime}")
print()

time.sleep(5)

# parallel version
starttime = time.time()

longest = multiprocessing.Process(target=get_longest_word, args=(text,))
most_frequent = multiprocessing.Process(target=get_most_frequent_word, args=(text,))
palindromes = multiprocessing.Process(target=get_palindromes, args=(text,))

longest.start()
most_frequent.start()
palindromes.start()

longest.join()
most_frequent.join()
palindromes.join()

endtime = time.time()
print(f"Total time elapsed: {endtime-starttime}")
