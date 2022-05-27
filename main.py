# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word:str, anagram:str):
    # [assignment] Add your code here
    str1=word
    str2=anagram
    sorted_word=sorted(str1)
    sorted_anagram=sorted(str2)
    if sorted_word==sorted_anagram:
        return True
    else:
        return False    
print(find_anagram("icense", "silence") )

