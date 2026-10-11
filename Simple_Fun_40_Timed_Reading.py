# Task
# Timed Reading is an educational tool used in many schools to improve and advance reading skills. A young elementary student has just finished his very first timed reading exercise. Unfortunately he's not a very good reader yet, so whenever he encountered a word longer than maxLength, he simply skipped it and read on.

# Help the teacher figure out how many words the boy has read by calculating the number of words in the text he has read, no longer than maxLength.

# Formally, a word is a substring consisting of English letters, such that characters to the left of the leftmost letter and to the right of the rightmost letter are not letters.

# Example
# For maxLength = 4 and text = "The Fox asked the stork, 'How is the soup?'", the output should be 7

# The boy has read the following words: "The", "Fox", "the", "How", "is", "the", "soup".

# Input/Output
# [input] integer maxLength

# A positive integer, the maximum length of the word the boy can read.

# Constraints: 1 ≤ maxLength ≤ 10.

# [input] string text

# A non-empty string of English letters and punctuation marks.

# [output] an integer

# The number of words the boy has read.

def timed_reading(max_length, text):
    count = 0
    current_word_length = 0
    
    for char in text:
        if char.isalpha():
            current_word_length += 1
        else:
            if current_word_length > 0 and current_word_length <= max_length:
                count += 1
            current_word_length = 0
    
    if current_word_length > 0 and current_word_length <= max_length:
        count += 1
    
    return count