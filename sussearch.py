import sys

sus = 0 # Total amount of identified "sus" character sequences

# Search the file for each instance of "sus" and print the amount of occurrences
with open(sys.argv[1], "r") as file_to_search:
    text = file_to_search.readlines()
    for line in text:
        sus += line.lower().count('sus')
    print(sus)