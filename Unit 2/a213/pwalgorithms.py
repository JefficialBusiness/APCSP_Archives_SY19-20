 # Module pwalgorithms
import os

# get words from password dictionary file
def get_dictionary(word_file="dictionary.txt"):
  words = []
  dirname = os.path.dirname(__file__)
  dictionary_file = open(os.path.join(dirname, word_file))
  for line in dictionary_file:
    # store word, ommitting trailing new-line
    words.append(line[:-1])
  dictionary_file.close()
  return words

# analyze a one-word password
def one_word(password):
  words = get_dictionary()
  guesses = 0
  # get each word from the dictionary file
  for w in words:
    guesses += 1
    if (w == password):
      return True, guesses
  return False, guesses
