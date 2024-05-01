# Python3 program to find max length
# of a word in arr

# Function that returns the max length
def countMaxLength(arr, n):
    # Hold the max length
    max_len = 0

    for i in range(n):

        # Creating a list of words from arr[i] string
        words = arr[i].split()

        # Counting the number of words in the string
        len_words = len(words)

        # Comparing the length
        if max_len < len_words:
            max_len = len_words

    # Return max words in string
    return max_len


# Driver code
if __name__ == "__main__":
    arr = ["alice and bob love leetcode", "i think so too",
           "this is great thanks very much"]
    n = len(arr)

    # Function call
    ans = countMaxLength(arr, n)
    print(ans)


sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
max_word = 0
for i in range(len(sentences)):
    word = sentences[i].split()
    # print(word)
    word_len = len(word)
    # print(word_len)
    if word_len > max_word:
        max_word = word_len

print(max_word)


# Approach 2: Without using inbuilt method split() method
sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
max_words = 0

for sentence in sentences:
    word_count = 0
    in_word = False

    for char in sentence:
        # if char is a empty string
        if char == " ":
            if in_word:
                word_count += 1
                in_word = False
        else:
            in_word = True

    # Check if the last word in the sentence
    if in_word:
        word_count += 1

    if word_count > max_words:
        max_words = word_count

print(max_words)
