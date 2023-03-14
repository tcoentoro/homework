Regex Quick Reference
=====================

Make your own regex cheat sheet
Format it in Markdown

RegEx cheat sheet:

regex	usage

    a     matches the letter a
    B     matches the letter B
    \w    matches any word symbol (letters, numbers, underscore)
    \W    matches any non-word symbol
    \d    matches any number
    .     matches any character
    \.    matches an actual dot
    \w+   matches any number of word symbols
    [ab]  matches the letter a or b
    [a-d] matches the letters a, b, c, d
    ()    used for capturing groups
    \(    matches a left parenthese
	\S	  matches a non-whitespace
	\s	  matches any whitespace


Functions:

string = 'abcdefg'
item = a

match = re.search(item, string) --> simple retrieval and assigns to match

for match in re.finditer(item, seq) --> multiple searches for a pattern in seq

match.group(1) --> the second group within the brackets in the regex used

match.start() --> start coordinate of where the item is
match.end() --> end coordinate of where the item is


Examples:
match = re.search(item, string)

for match in re.finditer(item,seq):

