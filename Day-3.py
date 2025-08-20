# Given a sentence s (a string of space-separated words), perform the following transformation on each word:
# 1. Swap the first and last character of the word only if:
#    - The word has at least 3 characters.
#    - The first and last characters are of the same case (both lowercase or both uppercase).
# 2. Leave all other words unchanged.
# 3. Preserve the original spacing, including multiple spaces between words.
# 4. Consider only alphabetic words (skip numeric or symbol-only tokens).
#
# Test case 1:
# Input: "hello code War"
# Output: "oellh edoc War"
# Explanation: 
#    - "hello" → h and o are same case → swap → "oellh"
#    - "code" → c and e → same case → swap → "edoc"
#    - "War" → W and r → not same case → no swap
#
# Test case 2:
# Input: "Coding is easy to learn"
# Output: "Coding is yase to nearl"

#output:
sentence=input("Enter a sentence:")
w=sentence.split()
new_word=[]
for word in w:
    if word.isalpha() and  len(word)>=3:
        if(word[0].islower() and word[-1].islower()) or (word[0].isupper() and word[-1].isupper()):
            word=word[-1]+word[1:-1]+word[0]
    new_word.append(word)
result=' '.join(new_word)
print(result)
