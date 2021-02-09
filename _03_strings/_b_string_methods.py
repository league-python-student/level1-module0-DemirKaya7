# Given Strings s1 and s2, return the longer String
def find_longer_string(s1, s2):
    num_characters_s1 = len(s1)
    num_characters_s2 = len(s2)
    if num_characters_s1 > num_characters_s2:
        return s1
    elif num_characters_s2 > num_characters_s1:
        return s2
    else:
        return "equal"


# If String s contains the word "underscores", change all of the spaces to underscores
def format_spaces(s1):
    if s1.count('underscores') > 0:
        return s1.replace(' ','_')
    else:
        return s1


# Return the name of the person whose LAST name would appear first if they were
# in alphabetical order.
# You cannot assume there are no extra spaces around the name, but you can
# assume there is only one space between the first and last name.
# Strings can be compared alphabetically using <, >. Be aware that capital letters
# come first alphabetically:
# "abc" < "abd"   # True
# "abc" < "abD"   # False
def line_leader(s1, s2, s3):
    space_s1 = s1.find(' ')
    space_s2 = s2.find(' ')
    space_s3 = s3.find(' ')
    character_s1 = s1[space_s1 + 1]
    character_s2 = s2[space_s2 + 1]
    character_s3 = s3[space_s3 + 1]
    if (character_s1 < character_s2) and (character_s1 < character_s3):
        return s1
    if (character_s2 < character_s1) and (character_s2 < character_s3):
        return s2
    if (character_s3 < character_s1) and (character_s3 < character_s2):
        return s3
    else:
        print("error - no if statments ran")

        #SOMETHING ABOUT "L STRIP / R STRIP" FUNCTION? <<-- note to self


# Return the sum of all numerical digits in the String
def numeral_sum(s):
    current_sum = 0
    for i in range(len(s)):
        if str(s[i].isdigit()):
            current_sum = current_sum + int(s[i])
    return current_sum



# Return the number of times String substring appears in String s
def substring_count(s, substring):
    return('\'o\' occurs ' + s.count(substring))


# Return the number of words in Strings that end with String substring
# You can assume there are no punctuation marks between words
def words_ends_with_substring(s, substring):
    num_words = s.count(" ")
    for i in range (num_words):
        num_substring = s.count(substring) + num_substring
    return num_substring



# Given String s, return the number of characters between the first occurrence
# of String substring and the final occurrence
# You can assume that substring will appear at least twice
def distance(s, substring):
    numOccurances = s.count(substring)
    lengthOfSubstring = len(substring)
    firstAppearance = s.find(substring)
    if firstAppearance == 0:
        firstAppearance = 1
    lastAppearance = s.find(substring, (lengthOfSubstring * (numOccurances - 1)))
    return (lastAppearance - (firstAppearance * lengthOfSubstring))



# Return true if String s is a palindrome
# palindromes are words or phrases are read the same forward as backward.
# HINT: ignore/remove all punctuation and spaces in the String
def palindrome(s):
    s = s.replace(' ', '')
    s = s.replace('?', '')
    s = s.replace('!', '')
    s = s.replace('.', '')
    s = s.replace(',', '')
    s = s.replace('-', '')
    s = s.replace('\'', '')
    s = s.replace('(', '')
    s = s.replace(')', '')
    s = s.upper()
    char1 = 0
    char2 = len(s) - 1
    for i in range(len(s) - 1):
        if s[char1] == s[char2]:
            char1 = char1 + 1
            char2 = char2 - 1
        else:
            return False
    return True
