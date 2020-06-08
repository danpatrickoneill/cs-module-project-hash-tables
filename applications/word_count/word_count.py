
import string
def word_count(s):
    # Keys will be words, values will be each word's count
    word_counts = {}
    # Chars we don't want counted
    invalid_chars = ['"', ':', ';', ',', '.', '-', '+', '=', '/', '\\', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&']
    # Think we're really just looking for words; setting some valid characters
    valid_chars = set(string.ascii_lowercase)
    valid_chars.add("'")
    # Building list of words to iterate over
    words = s.split(" ")

    # for word in words:
    #     # Ignoring case
    #     word = word.lower()
    #     # If invalid char, strip off string
    #     for char in invalid_chars:
    #         if char in word:
    #             # print(char)
    #             # print(word)
    #             word = word.strip(char)
    #     # If word has no content, skip it
    #     if len(word) == 0:
    #         continue
    #     # If word already in counts dict, increment count
    #     if word in word_counts:
    #         word_counts[word] += 1
    #     # Else; set count to 1
    #     else:
    #         word_counts[word] = 1

    # Solution checking for valid words
    for word in words:
        # Ignoring case
        word = word.lower()
        word_pointer = 0
        new_word = ''
        while word_pointer < len(word):
            if word[word_pointer] in valid_chars:
                new_word += word[word_pointer]
                word_pointer += 1
            else:
                # If word already in counts dict, increment count
                if len(new_word) > 0:
                    if new_word in word_counts:
                        word_counts[new_word] += 1
                    # Else; set count to 1
                    else:
                        word_counts[new_word] = 1
                new_word = ''
                word_pointer += 1
        if len(new_word) > 0:
            # If word already in counts dict, increment count
            if new_word in word_counts:
                    word_counts[new_word] += 1
            # Else; set count to 1
            else:
                word_counts[new_word] = 1



    return word_counts

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello  hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
    print(word_count('":;,.-+=/\\|[]{}()*^&'))
    print(word_count('a a\ra\na\ta \t\r\n'))