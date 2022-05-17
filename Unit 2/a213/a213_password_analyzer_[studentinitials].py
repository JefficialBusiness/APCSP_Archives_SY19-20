# a213_password_analyzer.py
import sys
import time
import pwalgorithms as pwa

# usage 
if len(sys.argv) != 2:
  print("Please supply a passphrase")
  sys.exit(0)
# store user password
password = sys.argv[1]

# one-word password analysis
print("Analyzing a one-word password ...")
time_start = time.time()
# attempt to find password
found, num_guesses = pwa.one_word(password)
time_end = time.time()

# report results
if (found):
  print(password, "found in", num_guesses, "guesses")
else: 
  print(password, "NOT found in", num_guesses, "guesses!")
print("Time:", format((time_end-time_start), ".8f"))