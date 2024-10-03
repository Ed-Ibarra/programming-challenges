"""
Game Rules

- Both players are given the same string
- Both players have to make substrings using the letters of the string
- Stuart has to make words starting with consonants
- Kevin has to make words starting with vowels
- The game ends when both players have made all possible substrings

Scoring
A player gets +1 point for each occurrence of the substring in the string
"""

def minion_game(string):
    l = len(string)
    kevin_score = sum([l - i for i in range(l) if string[i] in "AEIOU"])
    stuart_score = sum([l - i for i in range(l) if string[i] not in "AEIOU"])

    if stuart_score > kevin_score:
        print(f"Stuart {stuart_score}")
    elif kevin_score > stuart_score:
        print(f"Kevin {kevin_score}")
    else:
        print("Draw")


if __name__ == '__main__':
    minion_game(input())