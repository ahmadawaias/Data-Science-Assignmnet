# Ahmad Awais (123)
# Fa21-bse-123

import re

# Read the file
with open("example-text.txt", "r") as file:
    text = file.read()
    # print(text)

# 1 Extract list of all words
all_words = re.findall(r"\b\w*\b", text)
print(all_words)

# 2 Extract list of all words starting with a capital letter
capital_letters = re.findall(r"[A-Z][a-z]*", text)
print(capital_letters)

# 3 Extract list of all words of length 5
fiveLettersWords = re.findall(r"\b\w{5}\b", text)
print(fiveLettersWords)

# 4 Extract list of all words inside double quotes
quoted_words = re.findall(r'"([^"]*)"', text)
print(quoted_words)

# 5 Extract list of all vowels
vowels = re.findall(r"[aeiouAEIOU]", text)
print(vowels)

# 6 Extract list of 3 letter words ending with letter ‘e’
threeLetterAtEndEWords = re.findall(r"\b\w{2}e\b", text)
print(threeLetterAtEndEWords)

# 7 Extract list of all words starting and ending with letter ‘b’
bWordsB = re.findall(r"\b[bB]\w*[Bb]\b", text)
print(bWordsB)

# 8 Remove all the punctuation marks from the text
replaceSpace = re.sub(r"\W", " ", text)
print(replaceSpace)

# 9 Replace all words ending ‘n't’ to their full form ‘not’
replaceNot = re.sub(r"n't", " not", text)
print(replaceNot)

# 10 Replace all the new lines with a single space
replaceLinesBySpace = re.sub(r"\n", " ", text)
print(replaceLinesBySpace)
