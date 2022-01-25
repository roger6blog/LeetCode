'''
Level: Medium   Tag: [Design]

An abbreviation of a word follows the form <first letter><number><last letter>.
Below are some examples of word abbreviations:

a) it                      --> it    (no abbreviation)

     1
b) d|o|g                   --> d1g

              1    1  1
     1---5----0----5--8
c) i|nternationalizatio|n  --> i18n

              1
     1---5----0
d) l|ocalizatio|n          --> l10n
Assume you have a dictionary and given a word, find whether its abbreviation is unique in the dictionary.

A word's abbreviation is unique if no other word from the dictionary has the same abbreviation.


Example1

Input:
[ "deer", "door", "cake", "card" ]
isUnique("dear")
isUnique("cart")
Output:
false
true
Explanation:
Dictionary's abbreviation is ["d2r", "d2r", "c2e", "c2d"].
"dear" 's abbreviation is "d2r" , in dictionary.
"cart" 's abbreviation is "c2t" , not in dictionary.

Example2

Input:
[ "deer", "door", "cake", "card" ]
isUnique("cane")
isUnique("make")
Output:
false
true
Explanation:
Dictionary's abbreviation is ["d2r", "d2r", "c2e", "c2d"].
"cane" 's abbreviation is "c2e" , in dictionary.
"make" 's abbreviation is "m2e" , not in dictionary.

'''

class ValidWordAbbr:

    def __init__(self, dictionary):
        # do intialization if necessary
        self.abbr_word = []
        for d in dictionary:
            if len(d) > 2:
                abbr = d[0] + str(len(d)-2) + d[-1]
            else:
                abbr = d
            self.abbr_word.append(abbr)



    def isUnique(self, word):
        # write your code here
        if len(word) > 2:
            abbr = word[0] + str(len(word)-2) + word[-1]
        else:
            abbr = word

        if abbr in self.abbr_word:
            return False

        return True



# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param = obj.isUnique(word)
dictionary = [ "deer", "door", "cake", "card" ]
obj = ValidWordAbbr(dictionary)
print(obj.isUnique("dear"))
print(obj.isUnique("cart"))
print(obj.isUnique("cane"))
print(obj.isUnique("make"))
