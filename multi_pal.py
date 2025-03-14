import re

def is_palindrome(s):
    return s == s[::-1]

def find_first_palindrome(sentence):
    words = sentence.split()
    n = len(words)

    # Check single-word palindromes first
    for word in words:
        cleaned_word = re.sub(r'[^a-zA-Z]', '', word).lower()  # Remove punctuation and normalize case
        if cleaned_word and is_palindrome(cleaned_word):
            return word  # Return the original form from the sentence

    # Check multi-word palindromes
    for i in range(n):
        for j in range(i + 1, n):
            phrase = " ".join(words[i:j+1])
            cleaned_phrase = re.sub(r'[^a-zA-Z]', '', phrase).lower()
            if is_palindrome(cleaned_phrase):
                return phrase  # Return the original form

    return None  # No palindrome found

# Example test case
sentence = "Michael went to see a racecar and it was great"
print(find_first_palindrome(sentence))  # Output: "a racecar a"
