def word_count(s):
    # Implement me.
    words = s.replace(",", "")
    words = words.replace(".", "")
    words = words.replace("\"", "")
    words = words.replace(":", "")
    words = words.replace(";", "")
    words = words.replace("-", "")
    words = words.replace("+", "")
    words = words.replace("=", "")
    words = words.replace("/", "")
    words = words.replace("\\", "")
    words = words.replace("|", "")
    words = words.replace("[", "")
    words = words.replace("]", "")
    words = words.replace("{", "")
    words = words.replace("}", "")
    words = words.replace("(", "")
    words = words.replace(")", "")
    words = words.replace("*", "")
    words = words.replace("^", "")
    words = words.replace("&", "")
    words = words.lower()
    words = words.split()
    print(words)

    count_words = {}
    for word in words:
        if word in count_words.keys():
            count_words[word] += 1
        else:
            count_words[word] = 1

    print(count_words)
    return count_words


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
