"""
You are given n words. Some words may repeat.
For each word, output its number of occurrences.
The output order should correspond with the input order of appearance of the word.
See the sample input/output for clarification.

Note: Each input line ends with a "\n" character.

--------------------------------------------------------------------------------
* Sample Input
4
bcdef
abcdefg
bcde
bcdef

? Sample Output
3
2 1 1
--------------------------------------------------------------------------------
! Explanation: There are 3 distinct words.
! Here, "bcdef" appears twice in the input at the first and last positions.
! The other words appear once each. The order of the first appearances are 
! "bcdef", "abcdefg" and "bcde" which corresponds to the output.
"""
from collections import Counter

words_amount = int(input())
words_list = [input() for _ in range(words_amount)]

# Print how many unique words there are
print(len(Counter(words_list)))

# Print the frequencies of each unique word
print(*list(Counter(words_list).values()))