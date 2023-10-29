def are_anagrams(word1, word2):
    # Remove spaces and convert to lowercase to ensure accurate comparison
    word1 = word1.replace(" ", "").lower()
    word2 = word2.replace(" ", "").lower()

    # Check if the sorted letters of both words are the same
    return sorted(word1) == sorted(word2)

# Input two words to check if they are anagrams
word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")

if are_anagrams(word1, word2):
    print(f"{word1} and {word2} are anagrams.")
else:
    print(f"{word1} and {word2} are not anagrams.")
